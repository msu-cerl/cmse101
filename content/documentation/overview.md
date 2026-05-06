---
title: "System Overview"
description: "Architecture and design of the course infrastructure"
weight: 2
---

# System Architecture Overview

This page explains how all the pieces of the course infrastructure fit together.

## The Big Picture

```
                    Hugo Site (Content)
                          │
                ┌─────────┼─────────┐
                │         │         │
            Markdown    Theme      CSS
            Content   (Terminal)  (A11y)
                │         │         │
                └─────────┼─────────┘
                          │
                    [Website Output]
                    (HTML, CSS, JS)
                          │
                ┌─────────┴─────────┐
                │                   │
           [Browser]         [D2L Generator]
           (Website)               │
                         ┌─────────┴──────────┐
                         │                    │
                    Typst PDF           Pandoc DOCX
                    (Beautiful)         (Editable)
                         │                    │
                    [PDF Output]         [DOCX Output]
                    (For Reading)        (For Editing)
                         │                    │
                         └─────────┬──────────┘
                                   │
                          [Brightspace Upload]
                          (PDF + DOCX Files)
```

## Component Breakdown

### 1. Hugo Site Generator

**What it does:** Converts markdown content + templates into a static website

**Key files:**
- `config.yaml` — Site configuration
- `themes/terminal/` — Website theme
- `layouts/` — Custom Hugo templates
- `content/` — Course material (markdown)

**Output:** Static HTML/CSS/JS website

### 2. Accessibility Add-On Layer

**What it does:** Makes the website WCAG AAA compliant without modifying the theme

**Key files:**
- `layouts/_default/baseof.html` — Override base template
- `layouts/partials/accessibility/` — Accessibility partials
- `static/css/accessibility.css` — Accessibility styles
- `layouts/shortcodes/img-a11y.html` — Enforced alt text shortcode
- `layouts/shortcodes/form-input.html` — Accessible form inputs

**Features:**
- Skip navigation link
- ARIA landmarks
- Enhanced focus styles (AAA-compliant)
- Dark mode color scheme (18.92:1 contrast)
- Keyboard navigation
- Screen reader support
- Form accessibility
- Reduced motion support

**Output:** Website meets WCAG AAA standards

### 3. D2L Document Generation System

**What it does:** Converts course content to professional PDFs and DOCXs for Brightspace

**Key files:**
- `scripts/generate-d2l-docs.py` — Main generator script
- `templates/typst/clean/template.typ` — Typst PDF template
- `venv/` — Python environment with Typst, Pandoc, dependencies

**Process:**
1. Read markdown files from `content/`
2. Extract frontmatter (title, weight, metadata)
3. Sort by weight
4. **For PDF:** Convert to Typst → Compile with Typst CLI
5. **For DOCX:** Convert directly to DOCX with Pandoc

**Output:** `output/d2l/` contains PDFs and DOCXs ready for upload

### 4. Typst PDF Template

**What it does:** Provides professional, accessible PDF styling

**Key files:**
- `templates/typst/clean/template.typ` — Template design
- `templates/typst/clean/template.yml` — Template metadata

**Features:**
- MSU green branding (#18453B)
- Roboto font (accessible for dyslexia)
- Proper heading hierarchy (h1 → h2 → h3)
- Color contrast compliance (all 7:1+ ratio)
- Code block highlighting
- Proper margins and spacing

**Output:** Beautiful, accessible PDFs

## Data Flow

### Publishing Content

```
1. Author creates markdown file in content/readings/week-01.md
   - Includes frontmatter: title, weight, date
   - Includes content: markdown text

2. Hugo generates website
   - Reads markdown + frontmatter
   - Applies theme + accessibility layer
   - Generates HTML/CSS/JS
   - Output: Hugo site at localhost:1313

3. D2L document generator reads same markdown
   - Extracts frontmatter
   - Converts to Typst (PDF) or DOCX
   - Generates in output/d2l/

4. Instructor uploads to Brightspace
   - PDF for reading
   - DOCX for editing/annotation
```

### Content Processing

```markdown
Source: content/readings/week-01.md
│
├─→ [Hugo] ──→ website/readings/week-01/index.html
│
└─→ [D2L Gen] ──→ [Typst] ──→ output/d2l/week-01.pdf
                ──→ [Pandoc] ──→ output/d2l/week-01.docx
```

## The Three Outputs

### 1. Website (Hugo)

**When to use:** Students browsing on any device

**Characteristics:**
- Interactive, responsive
- Keyboard accessible
- WCAG AAA compliant
- Dark theme
- Online or offline (can save HTML)

### 2. PDF (Typst)

**When to use:** Professional, formatted reading

**Characteristics:**
- Beautiful typography
- Consistent branding
- Page numbers
- Works offline
- Print-friendly
- AAA accessible

### 3. DOCX (Pandoc)

**When to use:** Students want to edit/annotate

**Characteristics:**
- Native Microsoft Word format
- Editable in Word, Google Docs, etc.
- Can be annotated
- Accessible structure
- Works offline

## Technology Decisions

### Why Typst for PDF?

- ✅ Generates beautiful PDFs
- ✅ Accessible output (contrast, fonts, structure)
- ✅ Self-contained (no external web services)
- ✅ Fast compilation
- ✅ Version control friendly (text-based)

### Why Hugo for Website?

- ✅ Static site (secure, fast, no database)
- ✅ Content in markdown (human-readable)
- ✅ Theme support (professional looking)
- ✅ Built-in accessibility (semantic HTML)
- ✅ GitHub Pages compatible

### Why Pandoc for DOCX?

- ✅ Direct markdown → DOCX (preserves structure)
- ✅ Maintains accessibility (native Word format)
- ✅ Cross-platform (works on Mac, Linux, Windows)
- ✅ Open source

### Why Custom Accessibility Layer?

- ✅ Keeps theme untouched (easier to update)
- ✅ Centralized accessibility improvements
- ✅ Easy to disable if needed
- ✅ Demonstrates accessibility best practices

## File Organization

```
.
├── config.yaml                  # Hugo config
├── README.md                    # Getting started
├── ACCESSIBILITY.md             # A11y documentation
├── A11Y_QUICKSTART.md          # A11y quick reference
├── D2L_GENERATION.md           # D2L docs
├── content/
│   ├── _index.md               # Home page
│   ├── readings/               # Course readings
│   ├── assignments/            # Assignments
│   ├── resources/              # Resources
│   ├── schedule/               # Schedule
│   ├── learning-goals/         # Learning goals
│   └── documentation/          # This documentation
├── layouts/
│   ├── _default/baseof.html    # Override base (adds a11y)
│   ├── partials/accessibility/ # Accessibility partials
│   └── shortcodes/             # Custom shortcodes
├── static/
│   └── css/accessibility.css   # A11y styles
├── templates/
│   └── typst/clean/            # Typst PDF template
├── scripts/
│   └── generate-d2l-docs.py    # D2L generator
├── themes/
│   └── terminal/               # Hugo theme (untouched)
└── venv/                        # Python environment
```

## Workflow Examples

### Adding a New Reading

```bash
1. Create content/readings/week-07.md
   - Write markdown
   - Add frontmatter: title, weight

2. Push to GitHub
   - Hugo Auto-builds (if using GitHub Pages)
   - Site updates automatically

3. Generate D2L PDFs
   python scripts/generate-d2l-docs.py --type readings

4. Upload reading.pdf to Brightspace
```

### Customizing the Website

```bash
1. Edit static/css/accessibility.css
   - Change colors, fonts, spacing

2. Test locally
   hugo serve

3. Verify accessibility
   - Check keyboard navigation
   - Check screen reader
   - Check color contrast

4. Commit and push
   git add static/css/accessibility.css
   git commit -m "Adjust styling"
```

### Updating the PDF Template

```bash
1. Edit templates/typst/clean/template.typ
   - Change fonts, margins, colors

2. Test generation
   python scripts/generate-d2l-docs.py --type readings --format pdf

3. Review PDF output
   - Check typography
   - Check contrast
   - Check formatting

4. Commit changes
   git add templates/
   git commit -m "Update template styling"
```

## Key Design Principles

### 1. Accessibility First

- Every decision considers WCAG AAA compliance
- Color contrast verified (7:1+)
- Keyboard navigation from day one
- Screen reader testing included

### 2. Content-Focused

- Markdown is the source of truth
- No database complexity
- Version control all content
- Same content → multiple outputs

### 3. Open Source

- All code is public
- All documentation is included
- No vendor lock-in
- MIT licensed

### 4. Self-Contained

- No external services required
- Works offline (except for fonts)
- Single git repository
- Easy to clone and customize

## Performance Metrics

- **Website build:** ~40ms
- **Single PDF generation:** 2-3 seconds
- **Single DOCX generation:** 1-2 seconds
- **Full regenerate (all types, both formats):** 30-60 seconds

## Scalability

The system handles:
- ✅ 50+ content files
- ✅ Multiple content types
- ✅ Batch document generation
- ✅ 1000+ page PDFs
- ✅ 100+ students (no database bottleneck)

## Next Steps

- Explore [Accessibility Features](../accessibility/)
- Learn [D2L Generation](../d2l-generation/)
- Customize [PDF Template](../template-guide/)

---

**Last Updated:** May 2026  
**Status:** Production ready
