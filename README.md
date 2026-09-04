# CMSE 101 — AI in the Real World: Data, Power, & Society

Open-source, WCAG AAA-compliant course website with integrated MARP lecture
slides and PDF/DOCX generation for Brightspace (D2L).

```
Hugo Site → Website + Accessibility Layer
         ↓
   MARP Slides → Lecture decks (HTML + PDF)
         ↓
   D2L Generator → PDFs (Typst) + DOCXs (Pandoc)
         ↓
   Output: HTML website + Slide decks + Files for Brightspace
```

## ✨ Features

- 📖 **Static website** — Fast, secure, no database
- 🎞️ **MARP lecture slides** — Written in Markdown, built to HTML + PDF
- ♿ **WCAG AAA compliant** — Fully accessible site, slides, and documents
- 📄 **Multi-format output** — HTML website + slide decks + PDF + DOCX
- 📚 **Open source** — CC BY-NC-SA 4.0 licensed, fully documented
- 🚀 **Production ready** — Used for active course delivery

## 🚀 Quick Start

### Prerequisites

```bash
# Hugo (extended version) — builds the site
brew install hugo

# Node.js — needed to build MARP slides (via npx, nothing to install globally)
brew install node

# A Chromium-based browser — MARP renders slide PDFs through a real browser
# (Chrome/Edge/Chromium; if already on macOS with Chrome, you're set)

# Typst (for PDF generation)
brew install typst

# Pandoc (for DOCX generation)
brew install pandoc

# Python (for D2L document generation)
python3 --version  # 3.8+
```

### Setup (5 minutes)

```bash
# Clone repository
git clone git@github.com:msu-cerl/cmse101.git
cd cmse101

# Create Python environment
python3 -m venv venv
source venv/bin/activate.fish  # or: source venv/bin/activate (bash)

# Install Python dependencies
pip install python-frontmatter markdown pyyaml pypandoc

# Build the lecture slides (generates static/slides/ and data/slides.yaml)
./build-slides.sh

# Start website locally
hugo server
# Visit: http://localhost:1313
```

### Generate D2L Documents

```bash
# Generate combined PDFs and DOCXs
python scripts/generate-d2l-docs.py --format both

# Or individual files, per content type
python scripts/generate-d2l-docs.py --type assignments --individual --format both

# Output files → output/d2l/
```

## 📚 Documentation

Complete documentation is published on the site itself:

### [📖 System Documentation](/documentation/)

- **[System Architecture](documentation/overview/)** — How everything works
- **[Accessibility Features](documentation/accessibility/)** — WCAG AAA compliance
- **[D2L Generation](documentation/d2l-generation/)** — PDF/DOCX workflow
- **[Template Customization](documentation/template-guide/)** — PDF styling

Lecture slides have their own dedicated guide: **[SLIDES.md](SLIDES.md)** —
how to write, build, and publish MARP decks.

## 📁 File Structure

```
.
├── content/                    # Course content (markdown, rendered by Hugo)
│   ├── schedule/               # Weekly schedule / case studies
│   ├── assignments/            # Assignments
│   ├── resources/               # Additional resources
│   ├── learning-goals/         # Course learning goals
│   ├── syllabus/               # Syllabus
│   ├── use-cases/              # AI use-case write-ups
│   ├── slides/                 # /slides/ landing page (index only, not decks)
│   └── documentation/          # System documentation
├── slides/                     # MARP deck SOURCES — one .md per lecture
│   ├── _theme.css               #   shared accessible theme
│   └── images/                  #   deck images
├── build-slides.sh             # Builds slides/*.md → static/slides/*.{html,pdf}
├── SLIDES.md                    # Full guide to writing/building/publishing decks
├── layouts/
│   ├── _default/baseof.html    # Add a11y layer
│   └── partials/                # Hugo partials
├── static/css/
│   └── accessibility.css       # WCAG AAA styles
├── static/slides/               # GENERATED slide decks — gitignored, never edit
├── templates/typst/clean/       # PDF template
├── scripts/
│   └── generate-d2l-docs.py    # D2L generator
├── config.yaml                  # Hugo configuration
├── venv/                        # Python environment
└── output/d2l/                  # Generated PDFs/DOCXs
```

## 🎞️ Lecture Slides

Slides are written in Markdown using [MARP](https://marp.app/) and live in
`slides/`, not `content/` (Hugo would otherwise try to render each slide break
as part of a normal page).

```bash
./build-slides.sh                     # build every deck
./build-slides.sh lecture-01-welcome  # build one deck

./build-slides.sh && hugo server      # preview at /slides/ as students see it
```

Each run writes an HTML deck and a PDF per lecture into `static/slides/`
(gitignored — generated, not committed) and regenerates `data/slides.yaml`,
which feeds the `/slides/` index page and **is** committed.

See **[SLIDES.md](SLIDES.md)** for deck frontmatter, slide types, images,
speaker notes, accessibility checklist, and troubleshooting.

## 🎓 Adding Content

### Create a Schedule Entry

```bash
# Create file
touch content/schedule/week-13.md

# Add frontmatter and content
cat > content/schedule/week-13.md << 'EOF'
---
title: "Week 13: Future of AI"
date: 2026-11-30
description: "Week 13 Materials CMSE 101, Fall 2026"
---

Your content here...
EOF

# Hugo automatically updates site at localhost:1313
```

### Generate D2L Documents

Documents are auto-generated from the same markdown files:

```bash
python scripts/generate-d2l-docs.py --type assignments --format both
# Creates: output/d2l/assignments.pdf and .docx
```

## ♿ Accessibility

**Site meets WCAG AAA standards:**

- 18.92:1 text contrast (pure white on dark background)
- Skip navigation link (Tab to see it)
- Keyboard-only navigation (no mouse required)
- Screen reader support (NVDA, JAWS, VoiceOver, TalkBack)
- Reduced motion support
- Form accessibility

**Slides meet WCAG AA standards** — see the accessibility checklist in
[SLIDES.md](SLIDES.md).

**Documents also AAA compliant:**
- Color contrast 7:1+ on all PDFs
- Accessible DOCX format (native structure preserved)
- Alt text enforcement

See [Accessibility Features](documentation/accessibility/) for complete details.

## 🔧 Configuration

### Enable/Disable Accessibility

In `config.yaml`:

```yaml
params:
  a11y:
    enabled: true    # Master switch
```

### Customize PDF Template

Edit `templates/typst/clean/template.typ`:

```typst
// Change fonts, colors, margins, etc.
#let green = rgb("#FF6B6B")  // Custom color
```

See [Template Guide](documentation/template-guide/) for details.

## 📤 Publishing

### GitHub Pages (Automatic via CI)

```bash
git push origin main
```

`.github/workflows/build-deploy.yml` runs on every push/PR to `main`:

1. **`build` job** — installs Hugo + Node, runs `./build-slides.sh` (rebuilds
   every deck from `slides/*.md`; `static/slides/` is never committed), then
   builds the Hugo site into `public/`, and uploads it as a build artifact.
2. **`deploy` job** — only on push to `main` (or manual dispatch); downloads
   that artifact and publishes it to GitHub Pages. It does **not** rebuild
   anything, so the site is only built once per push.

Site is available at `https://msucerl.org/cmse101/` (see `baseURL` in
`config.yaml`).

### Custom Domain

Update `config.yaml`:

```yaml
baseURL: "https://your-domain.edu/"
```

### Brightspace Integration

Upload from `output/d2l/`:

1. Go to **Brightspace > Content > Learning Materials**
2. Upload PDFs for reading
3. Upload DOCXs for students to download/edit
4. Upload `static/slides/lecture-NN-topic.pdf` (built via `./build-slides.sh`)
   for lecture decks — see [SLIDES.md](SLIDES.md#d2l)

## 🐛 Troubleshooting

### "typst: command not found"

```bash
brew install typst
typst --version
```

### "pandoc: command not found"

```bash
brew install pandoc
pandoc --version
```

### Hugo won't start

```bash
rm -rf resources/
hugo server
```

### Slides fail to build or PDF export fails

See the Troubleshooting section of [SLIDES.md](SLIDES.md#troubleshooting) —
common causes are a missing Chromium-based browser or `CHROME_PATH` not set.

### Python environment issues

```bash
# Reactivate environment
source venv/bin/activate.fish
# or: source venv/bin/activate (bash)
```

## 📞 Support

- **Questions about the site?** See [System Documentation](documentation/)
- **Accessibility questions?** See [Accessibility Features](documentation/accessibility/)
- **D2L workflow?** See [D2L Generation](documentation/d2l-generation/)
- **PDF styling?** See [Template Guide](documentation/template-guide/)
- **Lecture slides?** See [SLIDES.md](SLIDES.md)

## 🔗 Resources

- **Hugo Docs:** https://gohugo.io/
- **MARP Docs:** https://marp.app/
- **Typst Docs:** https://typst.app/docs/
- **Pandoc Manual:** https://pandoc.org/
- **WCAG Guidelines:** https://www.w3.org/WAI/WCAG21/quickref/

## 📄 License

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

You are free to share and adapt this material for non-commercial purposes, provided you give attribution and distribute any derivatives under the same license.

## Status

- ✅ **Production Ready** — Active course deployment
- ✅ **WCAG AAA** — Full accessibility compliance
- ✅ **Documented** — Complete system documentation
- ✅ **Open Source** — CC BY-NC-SA 4.0 licensed

---

For detailed documentation, visit the [System Documentation](documentation/) page on the live site.
