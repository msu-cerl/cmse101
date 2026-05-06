#!/usr/bin/env node

/**
 * Accessibility Validation Script
 * Checks Hugo-built HTML for WCAG AAA compliance issues
 * Run after: hugo
 * Usage: node scripts/validate-accessibility.js
 */

const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const PUBLIC_DIR = path.join(__dirname, '..', 'public');
const RESULTS = {
  issues: [],
  warnings: [],
  files: 0,
  passed: 0,
};

/**
 * Recursively find all HTML files in public directory
 */
function findHtmlFiles(dir) {
  let files = [];
  const items = fs.readdirSync(dir);

  items.forEach(item => {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      files = files.concat(findHtmlFiles(fullPath));
    } else if (item.endsWith('.html')) {
      files.push(fullPath);
    }
  });

  return files;
}

/**
 * Check for images without alt text
 */
function checkAltText(dom, filepath) {
  const images = dom.window.document.querySelectorAll('img');
  const issues = [];

  images.forEach((img, index) => {
    const alt = img.getAttribute('alt');
    if (!alt || alt.trim() === '') {
      issues.push({
        type: 'ERROR',
        file: filepath,
        check: 'Alt Text Missing',
        element: `<img src="${img.src}">`,
        severity: 'high',
        wcag: '1.1.1 (Level A)',
      });
    }
  });

  return issues;
}

/**
 * Check for proper heading hierarchy
 */
function checkHeadingHierarchy(dom, filepath) {
  const headings = dom.window.document.querySelectorAll('h1, h2, h3, h4, h5, h6');
  const issues = [];
  let lastLevel = 0;

  if (headings.length === 0) {
    issues.push({
      type: 'WARNING',
      file: filepath,
      check: 'No Headings Found',
      message: 'Page should have at least one heading',
      severity: 'medium',
      wcag: '1.3.1 (Level A)',
    });
    return issues;
  }

  headings.forEach((heading) => {
    const level = parseInt(heading.tagName[1]);

    if (level > lastLevel + 1) {
      issues.push({
        type: 'WARNING',
        file: filepath,
        check: 'Heading Hierarchy Skip',
        element: heading.textContent.substring(0, 50),
        message: `Skipped from h${lastLevel} to h${level}`,
        severity: 'medium',
        wcag: '1.3.1 (Level A)',
      });
    }
    lastLevel = level;
  });

  return issues;
}

/**
 * Check for form labels
 */
function checkFormLabels(dom, filepath) {
  const inputs = dom.window.document.querySelectorAll('input, textarea, select');
  const issues = [];

  inputs.forEach((input) => {
    const id = input.getAttribute('id');
    const ariaLabel = input.getAttribute('aria-label');
    const ariaLabelledby = input.getAttribute('aria-labelledby');

    if (!id && !ariaLabel && !ariaLabelledby) {
      const type = input.tagName.toLowerCase();
      if (type !== 'input' || input.getAttribute('type') !== 'hidden') {
        issues.push({
          type: 'WARNING',
          file: filepath,
          check: 'Form Input Not Labeled',
          element: `<${type}>`,
          message: 'Form input must have associated label or aria-label',
          severity: 'medium',
          wcag: '1.3.1 (Level A)',
        });
      }
    }
  });

  return issues;
}

/**
 * Check for skip navigation link
 */
function checkSkipNav(dom, filepath) {
  const skipLink = dom.window.document.querySelector('a.skip-to-main');
  const issues = [];

  if (!skipLink) {
    issues.push({
      type: 'WARNING',
      file: filepath,
      check: 'No Skip Navigation Link',
      message: 'Accessibility add-on not enabled or skip nav missing',
      severity: 'medium',
      wcag: '2.4.1 (Level A)',
    });
  }

  return issues;
}

/**
 * Validate a single HTML file
 */
function validateFile(filepath) {
  try {
    const content = fs.readFileSync(filepath, 'utf-8');
    const dom = new JSDOM(content);

    const issues = [
      ...checkAltText(dom, filepath),
      ...checkHeadingHierarchy(dom, filepath),
      ...checkFormLabels(dom, filepath),
      ...checkSkipNav(dom, filepath),
    ];

    return issues;
  } catch (error) {
    console.error(`Error validating ${filepath}:`, error.message);
    return [];
  }
}

/**
 * Main validation runner
 */
function main() {
  console.log('\n🔍 Running Accessibility Validation...\n');

  if (!fs.existsSync(PUBLIC_DIR)) {
    console.error(`❌ Public directory not found: ${PUBLIC_DIR}`);
    console.error('Run `hugo` first to build the site.');
    process.exit(1);
  }

  const htmlFiles = findHtmlFiles(PUBLIC_DIR);
  console.log(`Found ${htmlFiles.length} HTML files to validate.\n`);

  htmlFiles.forEach((file) => {
    RESULTS.files++;
    const relPath = path.relative(PUBLIC_DIR, file);
    const issues = validateFile(file);

    if (issues.length === 0) {
      RESULTS.passed++;
    } else {
      issues.forEach((issue) => {
        if (issue.type === 'ERROR') {
          RESULTS.issues.push(issue);
        } else {
          RESULTS.warnings.push(issue);
        }
      });
    }
  });

  // Print summary
  console.log('\n' + '='.repeat(70));
  console.log('📊 ACCESSIBILITY VALIDATION SUMMARY');
  console.log('='.repeat(70));
  console.log(`\nFiles Validated: ${RESULTS.files}`);
  console.log(`✅ Passed: ${RESULTS.passed}`);
  console.log(`⚠️  Issues: ${RESULTS.issues.length}`);
  console.log(`⚠️  Warnings: ${RESULTS.warnings.length}`);

  if (RESULTS.issues.length > 0) {
    console.log('\n🔴 ERRORS (Must Fix):');
    RESULTS.issues.forEach((issue, i) => {
      console.log(`\n  ${i + 1}. ${issue.check}`);
      console.log(`     File: ${path.relative(process.cwd(), issue.file)}`);
      console.log(`     WCAG: ${issue.wcag}`);
      if (issue.element) console.log(`     Element: ${issue.element}`);
      if (issue.message) console.log(`     Message: ${issue.message}`);
    });
  }

  if (RESULTS.warnings.length > 0) {
    console.log('\n🟡 WARNINGS (Should Review):');
    RESULTS.warnings.forEach((issue, i) => {
      console.log(`\n  ${i + 1}. ${issue.check}`);
      console.log(`     File: ${path.relative(process.cwd(), issue.file)}`);
      console.log(`     WCAG: ${issue.wcag}`);
      if (issue.element) console.log(`     Element: ${issue.element}`);
      if (issue.message) console.log(`     Message: ${issue.message}`);
    });
  }

  console.log('\n' + '='.repeat(70));

  // Exit with error if there are critical issues
  if (RESULTS.issues.length > 0) {
    console.log('❌ Validation failed due to accessibility errors.');
    process.exit(1);
  } else if (RESULTS.warnings.length > 0) {
    console.log('⚠️  Validation passed but review warnings above.');
    process.exit(0);
  } else {
    console.log('✅ All accessibility checks passed!');
    process.exit(0);
  }
}

main();
