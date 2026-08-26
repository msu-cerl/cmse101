# MARP Slides Workflow for CMSE 101

This document explains how to create, build, and deploy accessible MARP slides for the course.

## Setup

### Prerequisites

You need Node.js and npm installed. Then install MARP CLI:

```bash
npm install -g @marp-team/marp-cli
```

Or use npx (included in npm) to run without global installation.

### Directory Structure

```
content/
  slides/
    _theme.css            # Shared accessible theme
    lecture-01-welcome.md # First slide deck
    lecture-02-....md     # Additional lectures
    ...

public/
  slides/
    lecture-01-welcome.html  # Generated HTML for web
    lecture-01-welcome.pdf   # Generated PDF for download/D2L
    ...

build-slides.sh           # Build script
```

## Creating Slides

### File Naming
- Save markdown files in `content/slides/`
- Use lowercase with hyphens: `lecture-01-welcome.md`
- One file per lecture/topic

### Markdown Structure

Each slide file starts with frontmatter:

```markdown
---
title: "Lecture 01: Welcome to AI in the Real World"
date: 2026-08-26
marp: true
theme: default
size: 16:9
paginate: true
---
```

### Slide Types

**Content slide** (default):
```markdown
# Slide Title

Content here. Use **bold**, *italic*, and `code` as needed.

- Bullet point
- Another point
```

**Title slide** (use at start):
```markdown
<!-- _class: title -->
# Main Title
## Subtitle

Content here
```

**Break/section slide** (visual pause):
```markdown
<!-- _class: break -->
# Section Title

Next topic begins here
```

### Presenter Notes

Add speaker notes that won't appear on slides but will survive PDF export:

```markdown
# Slide Title

Visible content here.

<!--_speaker_note:
This appears in presenter view only.
Use for talking points, timing, cues.
Write naturally—these are reminders, not scripts.
-->
```

### Accessibility Features

The theme includes:

- **High contrast colors** (WCAG AA compliant)
- **Readable sans-serif fonts** (Inter, 24px minimum)
- **Semantic HTML structure** (headings, lists, proper nesting)
- **Alt text for images** (use markdown: `![alt text](image.png)`)
- **Keyboard navigation** (all interactive elements are keyboard-accessible)
- **Focus indicators** (blue outline when tabbing)

**Best practices:**
- Use semantic headings (h1 for slide title, h2/h3 for content)
- Keep text simple and direct
- Avoid animations and decorative elements
- Use lists instead of paragraphs when possible
- Provide context for images

### Emphasis & Special Boxes

Highlight important content:

```markdown
<div class="emphasize">
**This is important.**
</div>
```

### Two-Column Layout

```markdown
<div class="columns">
<div class="column">

### Left Column
- Point 1
- Point 2

</div>
<div class="column">

### Right Column
- Point A
- Point B

</div>
</div>
```

## Building Slides

### Build All Slides

```bash
./build-slides.sh
```

This generates both HTML and PDF for every `lecture-*.md` file in `content/slides/`.

### Build a Specific Slide

```bash
./build-slides.sh lecture-01-welcome
```

This builds only that slide (no `.md` extension needed).

### Output

- **HTML**: `public/slides/lecture-01-welcome.html`
  - Open in browser for in-class viewing
  - Presenter mode available (press `p` in browser)
  - All speaker notes visible in presenter mode

- **PDF**: `public/slides/lecture-01-welcome.pdf`
  - Download and share with students
  - Upload directly to D2L Brightspace
  - Embeddable in LMS

## Deployment

### Linking from Hugo Site

Add links to the schedule page or syllabus:

```markdown
# Lecture 1: Welcome

[View Slides (HTML)](../slides/lecture-01-welcome.html)
[Download PDF](../slides/lecture-01-welcome.pdf)
```

### D2L Upload

1. Build the PDF: `./build-slides.sh lecture-01-welcome`
2. Upload `public/slides/lecture-01-welcome.pdf` to D2L Content
3. Students can download or view inline

### Static Site Hosting

The `public/slides/` directory is served by Hugo. Once built, HTML slides are immediately accessible at:

```
https://yourdomain.com/slides/lecture-01-welcome.html
```

## Workflow Tips

### During Class Preparation

1. Write the markdown file in `content/slides/`
2. Run `./build-slides.sh lecture-01-welcome`
3. Open the HTML file in your browser
4. Test presenter mode (press `p`)
5. Verify all speaker notes are present
6. Check accessibility: tab through with keyboard, test with screen reader

### Iteration

- Edit the markdown file
- Rebuild: `./build-slides.sh lecture-01-welcome`
- Refresh browser (Cmd+Shift+R for hard refresh)
- Changes appear instantly

### Version Control

Commit both:
- `.md` source files (the real content)
- `.html` and `.pdf` in `public/slides/` (for easy linking)

```bash
git add content/slides/*.md
git add public/slides/*.html public/slides/*.pdf
git commit -m "Add lecture 01 slides"
```

## Troubleshooting

### "MARP command not found"

Install globally or use npx:
```bash
npm install -g @marp-team/marp-cli
# or
npx marp --version
```

### PDF generation fails

MARP's PDF export requires a Chromium/Chrome browser. If you don't have one:

```bash
# Install Puppeteer's Chromium
npm install puppeteer
```

Or skip PDF and manually export from browser:
1. Open HTML in Chrome
2. Cmd+P (or Ctrl+P)
3. Save as PDF

### HTML looks different than expected

- Hard refresh browser: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows/Linux)
- Check theme CSS is in `content/slides/_theme.css`
- Verify markdown frontmatter has `theme: default`

## Accessibility Verification

Before deploying, verify:

- [ ] All images have alt text
- [ ] Headings are nested logically (no skipping h1 → h3)
- [ ] Color is not the only way to convey information
- [ ] Text has sufficient contrast (verified in CSS)
- [ ] No flashing or animated content that could trigger seizures
- [ ] Speaker notes are complete and clear
- [ ] PDF exports readable without losing formatting

Test with:
- Keyboard navigation (Tab through all slides)
- Screen reader (VoiceOver on Mac, NVDA on Windows)
- Browser zoom (test at 200%)

## Future Enhancements

Potential improvements:
- Auto-generate slide index page from frontmatter
- Link slides to schedule automatically
- Create speaker guide PDFs (notes only)
- Batch D2L uploads with a script
- Analytics tracking for which slides are viewed

