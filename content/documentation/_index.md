---
title: "System Documentation"
description: "Open source course infrastructure documentation"
weight: 1
---

# Course Infrastructure Documentation

This is the complete, open-source documentation for the **AI and Society Course** website infrastructure. Everything here is designed to be:

- **Accessible** — WCAG AAA compliant
- **Open source** — MIT licensed, fully transparent
- **Reproducible** — Self-contained, no external dependencies
- **Educational** — Documented for learning and reuse

## What's Documented

### 1. [Accessibility Features]({{< relref "accessibility" >}})

Complete guide to the accessibility add-on layer that makes the site WCAG AAA compliant:

- Skip navigation links
- ARIA landmarks and semantic roles
- Enhanced focus indicators
- Color contrast compliance
- Form accessibility
- Keyboard navigation
- Screen reader support

**For:** Instructors, developers, accessibility auditors

### 2. [D2L Document Generation]({{< relref "d2l-generation" >}})

Python-based system to generate professional, accessible PDFs and DOCX files from course content:

- Dual-path generation (PDF via Typst, DOCX via Pandoc)
- Combined or individual file modes
- WCAG AAA compliant output
- Batch processing for all content types
- Ready for Brightspace upload

**For:** Course instructors, content managers

### 3. [Template Customization]({{< relref "template-guide" >}})

Deep dive into the Typst template used for PDF generation:

- Design specifications and typography
- Color palette and contrast ratios
- Customization guide (fonts, colors, layout)
- Advanced styling techniques
- Accessibility compliance details

**For:** Designers, developers, template maintainers

## The Complete System

```
Hugo Site
├── Content (markdown files)
├── Accessibility Add-on Layer (CSS + JS)
└── D2L Document Generator
    ├── Typst Template (PDF)
    └── Pandoc (DOCX)
```

### Technology Stack

- **Hugo** — Static site generator
- **Typst** — Beautiful, accessible PDF generation
- **Pandoc** — Format conversion
- **Python** — D2L document pipeline
- **Accessible Minimal Template** — Terminal theme with accessibility overlays

## Quick Links

| Task | Documentation |
|------|---|
| Make site accessible | [Accessibility]({{< relref "accessibility" >}}) |
| Generate D2L documents | [D2L Generation]({{< relref "d2l-generation" >}}) |
| Customize PDF styling | [Template Guide]({{< relref "template-guide" >}}) |
| Understand the architecture | [System Overview]({{< relref "overview" >}}) |

## Getting Started

### For Instructors

1. **Add content** — Create markdown files in `content/readings/`, `content/assignments/`, etc.
2. **Generate D2L docs** — Run `python scripts/generate-d2l-docs.py --format both`
3. **Upload to Brightspace** — Take PDFs/DOCXs from `output/d2l/`

### For Developers

1. **Review architecture** — See [System Overview]({{< relref "overview" >}})
2. **Understand accessibility** — See [Accessibility Features]({{< relref "accessibility" >}})
3. **Customize templates** — See [Template Guide]({{< relref "template-guide" >}})

### For Accessibility Auditors

All documentation includes compliance details:
- WCAG AAA standards met
- Color contrast ratios (7:1+)
- Keyboard navigation support
- Screen reader compatibility

See [Accessibility Features]({{< relref "accessibility" >}}) for complete details.

## Philosophy

This system is built on the principle of **accessible by default**:

- **No compromise** — Accessibility is not an afterthought, it's foundational
- **Open source** — All code and documentation is public and MIT licensed
- **Transparent** — Every design decision is documented and reasoned
- **Educational** — Designed to be learned from and improved upon

## File Structure

```
.
├── content/
│   ├── readings/          # Course readings
│   ├── assignments/       # Course assignments
│   ├── resources/         # Additional resources
│   └── documentation/     # This documentation
├── layouts/
│   ├── _default/          # Hugo templates
│   └── partials/
│       └── accessibility/ # Accessibility features
├── scripts/
│   └── generate-d2l-docs.py  # D2L document generator
├── static/
│   └── css/
│       └── accessibility.css  # AAA-compliant styles
├── templates/
│   └── typst/
│       └── clean/          # Typst PDF template
└── venv/                   # Python virtual environment
```

## Contributing

This is an open source educational project. Contributions are welcome:

1. **Documentation improvements** — Fix typos, clarify explanations
2. **Accessibility enhancements** — Suggest improvements
3. **Feature requests** — Propose new capabilities
4. **Bug reports** — Document issues

## License

This entire system (code, documentation, templates) is provided under the **MIT License** for educational use.

## Support

- **Questions about the site** — See documentation pages below
- **Accessibility questions** — See [Accessibility Features]({{< relref "accessibility" >}})
- **D2L workflow questions** — See [D2L Generation]({{< relref "d2l-generation" >}})
- **Template customization** — See [Template Guide]({{< relref "template-guide" >}})

## Last Updated

May 2026

## About

This course infrastructure was designed with the principle that **accessibility is not optional**. Every component, from the website to the PDF generation system, has been built and audited for WCAG AAA compliance.

The documentation you're reading is itself published as open source so that others can learn from and improve upon this work.

---

**Next:** Explore the documentation sections above, or start with [System Overview]({{< relref "overview" >}}).
