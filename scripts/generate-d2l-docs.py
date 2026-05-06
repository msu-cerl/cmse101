#!/usr/bin/env python3
"""
Generate D2L-friendly PDF and DOCX documents from Hugo content.
Uses Typst template for clean, professional formatting.

Usage:
  source venv/bin/activate.fish
  python scripts/generate-d2l-docs.py [OPTIONS]

Options:
  --format {pdf|docx|both}     Output format (default: pdf)
  --type {readings|assignments|resources|docs|all}  Content type (default: all)
  --individual                 Generate separate files per item (default: combined)

Examples:
  # Combined documents (default)
  python scripts/generate-d2l-docs.py
  python scripts/generate-d2l-docs.py --type readings              # Combined readings PDF
  python scripts/generate-d2l-docs.py --type readings --format both # + DOCX

  # Individual documents
  python scripts/generate-d2l-docs.py --individual                 # Each item separate
  python scripts/generate-d2l-docs.py --type assignments --individual
  python scripts/generate-d2l-docs.py --type readings --individual --format both
"""

import os
import sys
import argparse
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
import frontmatter
import shutil

# Configuration
CONTENT_DIR = Path(__file__).parent.parent / "content"
OUTPUT_DIR = Path(__file__).parent.parent / "output" / "d2l"
TEMPLATE_DIR = Path(__file__).parent.parent / "templates" / "typst" / "clean"
TEMPLATE_FILE = TEMPLATE_DIR / "template.typ"

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

class ContentGenerator:
    def __init__(self, template_path):
        self.template_path = template_path
        with open(template_path, 'r') as f:
            self.template = f.read()

    def read_markdown_file(self, path):
        """Read markdown file with frontmatter."""
        with open(path, 'r') as f:
            post = frontmatter.load(f)
        return post.metadata, post.content

    def markdown_to_typst(self, markdown_text):
        """Convert markdown to Typst-compatible text.

        Simple conversion handles:
        - Headings (# → = level)
        - Bold/italic
        - Code blocks and inline code
        - Lists
        """
        lines = markdown_text.split('\n')
        typst_lines = []

        for line in lines:
            # Convert headings: # → =, ## → ==, etc.
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                heading_text = line[level:].strip()
                typst_lines.append('=' * level + ' ' + heading_text)
            # Keep everything else as-is (Typst is mostly Markdown-compatible)
            else:
                typst_lines.append(line)

        return '\n'.join(typst_lines)

    def collect_content_by_type(self, content_type='all'):
        """Collect and sort markdown files by content type.

        Returns dict: {content_type: [(title, path, weight), ...]}
        """
        content_map = {}
        types_to_process = ['readings', 'assignments', 'resources', 'docs']

        if content_type != 'all':
            types_to_process = [content_type]

        for ctype in types_to_process:
            content_path = CONTENT_DIR / ctype
            if not content_path.exists():
                continue

            files = []
            for md_file in sorted(content_path.glob('*.md')):
                if md_file.name.startswith('_'):  # Skip _index.md files
                    continue

                metadata, _ = self.read_markdown_file(md_file)
                weight = metadata.get('weight', 999)
                title = metadata.get('title', md_file.stem.replace('-', ' ').title())

                files.append({
                    'title': title,
                    'path': md_file,
                    'weight': weight,
                    'metadata': metadata
                })

            # Sort by weight
            files.sort(key=lambda x: x['weight'])
            content_map[ctype] = files

        return content_map

    def generate_document(self, content_type, content_files):
        """Generate a single document with all content of a type."""
        doc_content = []

        # Add title page info
        doc_content.append(f"= {content_type.title()}")
        doc_content.append(f"\nCourse: AI and Society Course")
        doc_content.append(f"Generated: {datetime.now().strftime('%B %d, %Y')}")
        doc_content.append("\n" + "=" * 60 + "\n")

        # Add content files
        for file_info in content_files:
            doc_content.append(f"\n== {file_info['title']}\n")

            metadata, content = self.read_markdown_file(file_info['path'])

            # Convert markdown to Typst
            typst_content = self.markdown_to_typst(content)
            doc_content.append(typst_content)
            doc_content.append("\n" + "-" * 40 + "\n")

        # Combine with template
        full_document = self.template.replace(
            '[-CONTENT-]',
            '\n'.join(doc_content)
        )

        return full_document

    def write_typst_file(self, content_type, typst_content):
        """Write Typst content to temporary file."""
        typst_file = OUTPUT_DIR / f"{content_type}.typ"
        with open(typst_file, 'w') as f:
            f.write(typst_content)
        return typst_file

    def generate_pdf(self, typst_file):
        """Generate PDF from Typst file using Typst CLI."""
        output_pdf = typst_file.with_suffix('.pdf')

        try:
            result = subprocess.run(
                ['typst', 'compile', str(typst_file), str(output_pdf)],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                print(f"❌ Error generating PDF from {typst_file.name}:")
                print(result.stderr)
                return None

            return output_pdf
        except FileNotFoundError:
            print("❌ Typst CLI not found. Install it with: brew install typst")
            return None

    def generate_docx_from_markdown(self, content_type, markdown_content, output_name):
        """Generate DOCX directly from markdown using pandoc.

        This preserves better structure and accessibility than PDF→DOCX conversion.
        """
        # Write markdown to temporary file
        temp_md = OUTPUT_DIR / f"{output_name}.md"
        with open(temp_md, 'w') as f:
            f.write(markdown_content)

        output_docx = OUTPUT_DIR / f"{output_name}.docx"

        try:
            # Build pandoc command
            cmd = [
                'pandoc',
                str(temp_md),
                '-o', str(output_docx),
                '--from', 'markdown',
                '--to', 'docx'
            ]

            # Add reference doc if it exists
            ref_doc = self._get_reference_doc()
            if ref_doc:
                cmd.extend(['--reference-doc', str(ref_doc)])

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                print(f"❌ Error generating DOCX: {result.stderr}")
                # Clean up temp file
                temp_md.unlink(missing_ok=True)
                return None

            # Clean up temp file
            temp_md.unlink(missing_ok=True)
            return output_docx
        except FileNotFoundError:
            print("❌ Pandoc not found. Install it with: brew install pandoc")
            return None

    def _get_reference_doc(self):
        """Get or create a reference DOCX for styling."""
        ref_doc = OUTPUT_DIR / "reference.docx"

        # If reference doc doesn't exist, let pandoc use defaults
        if not ref_doc.exists():
            return None

        return ref_doc

    def process_all(self, format_type='pdf', content_type='all', individual=False):
        """Generate all documents in specified format.

        Args:
            format_type: 'pdf', 'docx', or 'both'
            content_type: 'all' or specific type
            individual: If True, generate separate file per item; if False, combine all
        """
        mode = "Individual Files" if individual else "Combined"
        print(f"\n📄 Generating D2L Documents ({format_type.upper()}, {mode})")
        print(f"{'=' * 50}")

        # Collect content
        content_map = self.collect_content_by_type(content_type)

        if not content_map:
            print(f"❌ No content found for type: {content_type}")
            return

        # Generate documents
        for ctype, files in content_map.items():
            if not files:
                continue

            print(f"\n📋 Processing {ctype}... ({len(files)} files)")

            if individual:
                # Generate individual document for each file
                self._process_individual_files(ctype, files, format_type)
            else:
                # Generate combined document for all files
                self._process_combined_files(ctype, files, format_type)

        print(f"\n{'=' * 50}")
        print(f"📁 Output directory: {OUTPUT_DIR}")
        print(f"✅ Generation complete!\n")

    def _process_combined_files(self, ctype, files, format_type):
        """Generate one combined document from multiple files.

        Generates PDF via Typst and DOCX directly from markdown for better accessibility.
        """
        # Collect all markdown content
        all_markdown = []
        all_markdown.append(f"# {ctype.title()}")
        all_markdown.append(f"\nCourse: AI and Society Course")
        all_markdown.append(f"Generated: {datetime.now().strftime('%B %d, %Y')}")
        all_markdown.append("\n" + "=" * 60 + "\n")

        for file_info in files:
            all_markdown.append(f"\n## {file_info['title']}\n")
            _, content = self.read_markdown_file(file_info['path'])
            all_markdown.append(content)
            all_markdown.append("\n" + "-" * 40 + "\n")

        markdown_content = '\n'.join(all_markdown)

        # Generate PDF via Typst
        if format_type in ['pdf', 'both']:
            typst_content = self.generate_document(ctype, files)
            typst_file = self.write_typst_file(ctype, typst_content)
            print(f"   ✓ Created {typst_file.name}")

            pdf_file = self.generate_pdf(typst_file)
            if pdf_file:
                size_kb = pdf_file.stat().st_size / 1024
                print(f"   ✓ Generated {pdf_file.name} ({size_kb:.1f} KB)")

        # Generate DOCX directly from markdown if requested
        if format_type in ['docx', 'both']:
            docx_file = self.generate_docx_from_markdown(ctype, markdown_content, ctype)
            if docx_file:
                size_kb = docx_file.stat().st_size / 1024
                print(f"   ✓ Generated {docx_file.name} ({size_kb:.1f} KB)")

    def _process_individual_files(self, ctype, files, format_type):
        """Generate separate document for each file.

        Generates PDF via Typst and DOCX directly from markdown for better accessibility.
        """
        for file_info in files:
            output_name = file_info['path'].stem
            _, markdown_content = self.read_markdown_file(file_info['path'])

            # Add title page info
            full_markdown = f"# {file_info['title']}\n\n"
            full_markdown += f"Course: AI and Society Course\n"
            full_markdown += f"Generated: {datetime.now().strftime('%B %d, %Y')}\n\n"
            full_markdown += markdown_content

            # Generate PDF via Typst
            if format_type in ['pdf', 'both']:
                typst_content = self.generate_document(ctype, [file_info])
                typst_file = OUTPUT_DIR / f"{output_name}.typ"

                with open(typst_file, 'w') as f:
                    f.write(typst_content)

                print(f"   ✓ Created {typst_file.name}")

                pdf_file = self.generate_pdf(typst_file)
                if pdf_file:
                    size_kb = pdf_file.stat().st_size / 1024
                    print(f"     → {pdf_file.name} ({size_kb:.1f} KB)")

            # Generate DOCX directly from markdown if requested
            if format_type in ['docx', 'both']:
                docx_file = self.generate_docx_from_markdown(ctype, full_markdown, output_name)
                if docx_file:
                    size_kb = docx_file.stat().st_size / 1024
                    print(f"     → {docx_file.name} ({size_kb:.1f} KB)")


def main():
    parser = argparse.ArgumentParser(
        description='Generate D2L-friendly documents from Hugo content.'
    )
    parser.add_argument(
        '--format',
        choices=['pdf', 'docx', 'both'],
        default='pdf',
        help='Output format (default: pdf)'
    )
    parser.add_argument(
        '--type',
        choices=['readings', 'assignments', 'resources', 'docs', 'all'],
        default='all',
        help='Content type to process (default: all)'
    )
    parser.add_argument(
        '--individual',
        action='store_true',
        help='Generate individual files per content item (default: combined)'
    )

    args = parser.parse_args()

    # Check dependencies
    if not TEMPLATE_FILE.exists():
        print(f"❌ Template not found: {TEMPLATE_FILE}")
        print(f"   Expected Typst template at: templates/typst/clean/template.typ")
        sys.exit(1)

    # Generate documents
    try:
        generator = ContentGenerator(TEMPLATE_FILE)
        generator.process_all(
            format_type=args.format,
            content_type=args.type,
            individual=args.individual
        )
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
