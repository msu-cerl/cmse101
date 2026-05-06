# AI and Society Course

Open-source, WCAG AAA-compliant course website with integrated PDF/DOCX generation for Brightspace.

```
Hugo Site → Website + Accessibility Layer
         ↓
    D2L Generator → PDFs (Typst) + DOCXs (Pandoc)
         ↓
   Output: HTML website + Files for Brightspace
```

## ✨ Features

- 📖 **Static website** — Fast, secure, no database
- ♿ **WCAG AAA compliant** — Fully accessible site and documents
- 📄 **Multi-format output** — HTML website + PDF + DOCX
- 📚 **Open source** — CC BY-NC-SA 4.0 licensed, fully documented
- 🚀 **Production ready** — Used for active course delivery

## 🚀 Quick Start

### Prerequisites

```bash
# Hugo (extended version)
brew install hugo

# Typst (for PDF generation)
brew install typst

# Pandoc (for DOCX generation)
brew install pandoc

# Python (for document generation)
python3 --version  # 3.8+
```

### Setup (5 minutes)

```bash
# Clone repository
git clone <repo-url>
cd cmse101

# Create Python environment
python3 -m venv venv
source venv/bin/activate.fish  # or: source venv/bin/activate (bash)

# Install Python dependencies
pip install python-frontmatter markdown pyyaml pypandoc

# Start website locally
hugo server
# Visit: http://localhost:1313
```

### Generate D2L Documents

```bash
# Generate combined PDFs and DOCXs
python scripts/generate-d2l-docs.py --format both

# Or individual files
python scripts/generate-d2l-docs.py --type readings --individual --format both

# Output files → output/d2l/
```

## 📚 Documentation

Complete documentation is published on the site itself:

### [📖 System Documentation](/documentation/)

- **[System Architecture](documentation/overview/)** — How everything works
- **[Accessibility Features](documentation/accessibility/)** — WCAG AAA compliance
- **[D2L Generation](documentation/d2l-generation/)** — PDF/DOCX workflow
- **[Template Customization](documentation/template-guide/)** — PDF styling

## 📁 File Structure

```
.
├── content/                    # Course content (markdown)
│   ├── readings/              # Weekly readings
│   ├── assignments/           # Assignments
│   ├── resources/             # Additional resources
│   └── documentation/         # System documentation
├── layouts/
│   ├── _default/baseof.html   # Add a11y layer
│   └── partials/              # Hugo partials
├── static/css/
│   └── accessibility.css      # WCAG AAA styles
├── templates/typst/clean/     # PDF template
├── scripts/
│   └── generate-d2l-docs.py   # D2L generator
├── config.yaml                # Hugo configuration
├── venv/                       # Python environment
└── output/d2l/                # Generated PDFs/DOCXs
```

## 🎓 Adding Content

### Create a Reading

```bash
# Create file
touch content/readings/week-13.md

# Add frontmatter and content
cat > content/readings/week-13.md << 'EOF'
---
title: "Week 13: Future of AI"
weight: 13
---

# Week 13: Future of AI

Your content here...
EOF

# Hugo automatically updates site at localhost:1313
```

### Generate D2L Documents

Documents are auto-generated from the same markdown files:

```bash
python scripts/generate-d2l-docs.py --type readings --format both
# Creates: output/d2l/readings.pdf and .docx
```

## ♿ Accessibility

**Site meets WCAG AAA standards:**

- 18.92:1 text contrast (pure white on dark background)
- Skip navigation link (Tab to see it)
- Keyboard-only navigation (no mouse required)
- Screen reader support (NVDA, JAWS, VoiceOver, TalkBack)
- Reduced motion support
- Form accessibility

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

### GitHub Pages (Automatic)

```bash
git push origin main
# GitHub Actions automatically builds and deploys
# Site available at: your-repo.github.io
```

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

## 🔗 Resources

- **Hugo Docs:** https://gohugo.io/
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

**Last Updated:** May 2026  
**Status:** Production Ready  
**Accessibility:** WCAG AAA Compliant

For detailed documentation, visit the [System Documentation](documentation/) page on the live site.
