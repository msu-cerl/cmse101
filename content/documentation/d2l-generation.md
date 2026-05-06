---
title: "D2L Document Generation"
description: "Generate PDFs and DOCXs for Brightspace"
weight: 4
---

# D2L Document Generation

Python-based system to generate professional, WCAG AAA-compliant PDFs and DOCX files from course content for Brightspace (D2L) upload.

## Features

- 📄 **Dual-path generation** — PDFs via Typst (beautiful), DOCXs via Pandoc (editable)
- 🎯 **Flexible modes** — Combined or individual files per content item
- ✅ **WCAG AAA compliant** — Both formats meet accessibility standards
- 🎨 **Professional styling** — MSU green branding template
- 📊 **Multiple content types** — Readings, assignments, resources, docs
- 🔄 **Batch processing** — Generate all at once or by type

## Quick Start

### Generate readings as PDF + DOCX

```bash
cd /path/to/repo
source venv/bin/activate.fish
python scripts/generate-d2l-docs.py --type readings --format both
```

Output:
- `output/d2l/readings.pdf` — Beautiful, paginated (346 KB)
- `output/d2l/readings.docx` — Editable in Word (21 KB)

### Generate individual files

```bash
python scripts/generate-d2l-docs.py --type assignments --individual --format both
```

Output:
- `output/d2l/assignment-01.pdf` + `.docx`
- `output/d2l/assignment-02.pdf` + `.docx`
- ... (one pair per file)

## Setup

### Prerequisites

1. **Virtual environment** (one-time setup):
   ```bash
   python3 -m venv venv
   source venv/bin/activate.fish
   pip install python-frontmatter markdown pyyaml pypandoc
   ```

2. **Typst** (for PDF generation):
   ```bash
   brew install typst
   ```

3. **Pandoc** (for DOCX generation):
   ```bash
   brew install pandoc
   ```

### Verify Installation

```bash
typst --version
pandoc --version
python --version
```

## Usage

### Command Syntax

```
python scripts/generate-d2l-docs.py [OPTIONS]
```

### Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--type` | `readings`, `assignments`, `resources`, `docs`, `all` | `all` | Content type |
| `--format` | `pdf`, `docx`, `both` | `pdf` | Output format |
| `--individual` | (flag) | combined | Separate files per item |

### Common Examples

#### Combined documents
```bash
# All readings as one PDF
python scripts/generate-d2l-docs.py --type readings

# All content in both formats
python scripts/generate-d2l-docs.py --format both

# Assignments as combined PDF + DOCX
python scripts/generate-d2l-docs.py --type assignments --format both
```

#### Individual documents
```bash
# Each reading separate
python scripts/generate-d2l-docs.py --type readings --individual

# Each resource in both formats
python scripts/generate-d2l-docs.py --type resources --individual --format both

# All content as individual files
python scripts/generate-d2l-docs.py --individual --format both
```

#### Specific types
```bash
# Syllabus and docs only
python scripts/generate-d2l-docs.py --type docs --format both

# Resources only
python scripts/generate-d2l-docs.py --type resources --individual
```

## Accessibility & Compliance

### PDF (Typst-generated)

✅ **WCAG AAA Compliant:**
- Color contrast: 7:1+ minimum
- Body text: 17.4:1 ✓
- Headings: 10.75:1 ✓
- Footer: 8.06:1 ✓
- Proper heading hierarchy (h1 → h2 → h3)
- Readable fonts (11pt Roboto)
- Optimized spacing (0.7em leading)

### DOCX (Pandoc-generated)

✅ **Native Accessibility:**
- Semantic structure preserved
- Heading tags for screen readers
- Editable in Microsoft Word
- Supports annotations
- Cross-platform compatible

## Output Structure

Files are saved to: `output/d2l/`

### Combined mode
```
output/d2l/
├── readings.pdf        # All readings
├── readings.docx
├── assignments.pdf
├── assignments.docx
├── resources.pdf
├── resources.docx
└── docs.pdf
```

### Individual mode
```
output/d2l/
├── week-01.pdf         # One per item
├── week-01.docx
├── week-02.pdf
├── week-02.docx
├── assignment-01.pdf
├── assignment-01.docx
└── ...
```

## Content Requirements

Files need frontmatter:

```yaml
---
title: "Week 1: Introduction"
weight: 1
---

# Main heading

Your markdown content...
```

- **`title`** — Used as document heading
- **`weight`** — Sort order (lower = earlier)
- **Content** — Standard markdown

### File Structure

```
content/
├── readings/           # Weekly readings
│   ├── week-01.md
│   ├── week-02.md
│   └── ...
├── assignments/        # Assignments
│   ├── assignment-01.md
│   └── ...
├── resources/          # Additional resources
│   └── ...
└── docs/              # Syllabus, guides, etc.
    └── ...
```

## D2L Upload Guide

### PDF Method (Recommended)

1. In D2L, go to **Content > Learning Materials**
2. Upload `readings.pdf`, `assignments.pdf`, etc.
3. Students download and view in PDF reader
4. ✅ Maintains formatting
5. ✅ Accessible on all devices
6. ✅ Offline readable

### DOCX Method (For Editing)

1. Upload `.docx` file to Brightspace
2. Students download and edit in Word
3. ✅ Can add annotations
4. ✅ Can customize formatting
5. ✅ Offline access

### Hybrid Approach (Best)

1. Post PDF for reading
2. Include DOCX link for students who prefer Word
3. ✅ Covers all accessibility needs
4. ✅ Covers all device preferences

## File Naming

Script uses Hugo filename as output name:

| Source | Output (Combined) | Output (Individual) |
|--------|-------------------|-------------------|
| `content/readings/week-01.md` | `readings.pdf` | `week-01.pdf` |
| `content/assignments/project-a.md` | `assignments.pdf` | `project-a.pdf` |

## Troubleshooting

### `typst: command not found`

Install Typst:
```bash
brew install typst
typst --version
```

### `pandoc: command not found`

Install Pandoc:
```bash
brew install pandoc
pandoc --version
```

### Empty output directory

1. Check content exists:
   ```bash
   ls -la content/readings/
   ls -la content/assignments/
   ```

2. Ensure files have `title:` in frontmatter

3. Check script can find template:
   ```bash
   ls -la templates/typst/clean/template.typ
   ```

### DOCX looks plain

This is intentional — minimal styling ensures cross-platform compatibility. You can:

1. Use PDF version for rich formatting
2. Edit DOCX in Word to add styles
3. Create custom reference document

### PDF font rendering issues

```bash
# Clear cache
rm -rf output/d2l/*.typ

# Regenerate
python scripts/generate-d2l-docs.py --type readings --format pdf
```

## Performance

Approximate generation times:

| Task | Time |
|------|------|
| Single reading PDF | 2-3 seconds |
| Combined readings (12 files) | 3-5 seconds |
| Single DOCX | 1-2 seconds |
| Full regenerate (all types, both) | 30-60 seconds |

## Automation

### Shell Script

```bash
# Create scripts/regenerate-d2l.sh
cat > scripts/regenerate-d2l.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")/.."
source venv/bin/activate.fish
python scripts/generate-d2l-docs.py --format both
echo "✅ D2L documents regenerated"
EOF

chmod +x scripts/regenerate-d2l.sh
./scripts/regenerate-d2l.sh
```

### CI/CD Pipeline

Add to your GitHub Actions workflow:

```yaml
- name: Generate D2L Documents
  run: |
    source venv/bin/activate
    python scripts/generate-d2l-docs.py --format both
```

## Advanced: Custom DOCX Template

Create a reference document for custom styling:

```bash
# Generate default reference
pandoc -o output/d2l/reference.docx --print-default-data-file reference.docx

# Edit reference.docx with Word styles
# Save as output/d2l/reference.docx
# Script automatically uses it
```

## Template Customization

Edit `templates/typst/clean/template.typ` to customize PDFs:

- Font: Change from Roboto to any system font
- Colors: Modify MSU green or text colors
- Margins: Adjust page margins
- Heading sizes: Increase/decrease heading sizes

See [Template Guide](../template-guide/) for details.

## Maintenance

### Update Template

```bash
# Edit template
nano templates/typst/clean/template.typ

# Regenerate documents
python scripts/generate-d2l-docs.py --format both

# Commit changes
git add templates/
git commit -m "Update PDF template styling"
```

### Add New Content Type

Edit `scripts/generate-d2l-docs.py`:

```python
types_to_process = ['readings', 'assignments', 'resources', 'docs', 'new-type']
```

Then run script with `--type new-type`.

## Key Features Explained

### Dual-Path Generation

**Why two different tools?**

- **Typst** → Beautiful PDFs with professional typography
- **Pandoc** → Direct markdown→DOCX with native Word compatibility

This gives you:
- ✅ Professional PDFs for distribution
- ✅ Editable DOCXs for student work

### Combined vs Individual

**Combined:** All readings in one PDF
- ✅ Single file to manage
- ❌ Harder to organize updates

**Individual:** One PDF per reading
- ✅ Easy to update one section
- ✅ Student downloads only what needed
- ❌ More files to manage

**Use case:** Combined for printing, individual for online.

### Format Options

**PDF only:**
- Fast generation
- Beautiful output
- Read-only

**DOCX only:**
- Fast generation
- Editable
- Native Word format

**Both:**
- Complete flexibility
- Students choose format
- Slightly longer generation

## Related Documentation

- See [System Overview](../overview/) for architecture
- See [Accessibility Features](../accessibility/) for compliance
- See [Template Guide](../template-guide/) for PDF customization

## Support

### Common Questions

**Q: Can I customize the PDF styling?**  
A: Yes! Edit `templates/typst/clean/template.typ`

**Q: Can students edit the PDF?**  
A: No, use DOCX format for editing. Or use both—let students choose.

**Q: How do I update one assignment?**  
A: Edit the markdown file, regenerate with `--type assignments --individual`

**Q: Can I automate regeneration?**  
A: Yes, use the shell script or CI/CD pipeline approach

**Q: How big are the files?**  
A: PDFs: 150-350 KB, DOCXs: 10-50 KB per document

---

**Last Updated:** May 2026  
**Status:** Production ready  
**Accessibility:** WCAG AAA compliant
