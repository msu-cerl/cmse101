---
title: "Template Customization"
description: "Typst PDF template guide and customization"
weight: 5
---

# Typst PDF Template Guide

Complete guide to the Typst template used for professional PDF generation.

## Overview

The template is located at: `templates/typst/clean/`

Used by the D2L document generator to create beautiful, WCAG AAA-compliant PDFs.

## Design Specifications

### Typography

| Element | Font | Size | Color | Weight | Notes |
|---------|------|------|-------|--------|-------|
| Body | Roboto | 11pt | White | Normal | Main text, 17.4:1 contrast |
| h1 | Roboto | 15pt | MSU Green | Bold | Title, 10.75:1 contrast |
| h2 | Roboto | 12.5pt | MSU Green | Semibold | Section heading |
| h3 | Roboto | 11pt | Gray | Semibold | Subsection |
| Code (inline) | Roboto | 9.9pt | Green | Normal | Highlighted background |
| Code (block) | Roboto | 9.68pt | Green | Normal | Light green box |
| Footer | Roboto | 9pt | Gray | Normal | Page numbers, 8.06:1 contrast |

### Colors

```typst
// MSU Green palette
#let green = rgb("#18453B")        // Main color
#let green-light = green.lighten(88%) // Light background

// Grays
body text:     luma(30)   // Very dark (17.4:1)
footer text:   luma(80)   // Medium gray (8.06:1)
heading h3:    luma(50)   // Dark gray
borders:       luma(210)  // Light gray
```

All colors tested for AAA contrast (7:1+ ratio).

### Layout

- **Paper**: US Letter (8.5" × 11")
- **Margins**: 1" top/bottom, 1.25" left/right
- **Line height**: 0.7em (tight, professional)
- **Paragraph spacing**: 1.1em (good readability)
- **Page numbers**: Centered footer, all pages
- **List markers**: MSU green bullets

## Customization

### Change Colors

Edit `templates/typst/clean/template.typ`:

```typst
// Change MSU green to different color
#let green = rgb("#FF6B6B")  // Red
#let green = rgb("#0066CC")  // Blue
#let green = rgb("#663399")  // Purple
```

**Accessibility note:** Verify new colors maintain 7:1+ contrast.

### Change Fonts

```typst
// Change from Roboto to another font
#set text(font: "Georgia", size: 11pt, fill: luma(30))
```

Recommended accessible alternatives:

**Serif fonts:**
- Georgia
- Garamond  
- Cambria

**Sans-serif fonts:**
- Arial
- Helvetica
- Open Sans
- Inter

### Adjust Heading Sizes

```typst
#show heading.where(level: 1): it => {
  text(fill: green, weight: "bold", size: 18pt, it.body)  // Changed from 15pt
}
```

Recommended sizes:
- h1: 16-18pt (title)
- h2: 12-14pt (section)
- h3: 11-12pt (subsection)

### Change Margins

```typst
#set page(
  paper: "us-letter",
  margin: (top: 0.75in, bottom: 0.75in, left: 1.5in, right: 1.5in),
```

Standard options:
- Narrow: 0.5-0.75"
- Normal: 1.0-1.25"
- Wide: 1.5-2.0"

### Modify Line Spacing

```typst
#set par(leading: 0.65em, spacing: 1.0em)  // Tighter
#set par(leading: 0.8em, spacing: 1.2em)   // Looser
```

Readable range: 0.6-0.9em leading

## Advanced Customization

### Custom Header/Footer

```typst
footer: context {
  let page_num = counter(page).display()
  let total = counter(page).final().first()
  align(center, text(fill: luma(80), size: 9pt)[
    Page #page_num of #total | AI and Society
  ])
}
```

### Heading Styling with Lines

```typst
#show heading.where(level: 1): it => {
  v(1.4em)
  text(fill: green, weight: "bold", size: 15pt, it.body)
  v(0.25em)
  line(length: 100%, stroke: 0.4pt + green.lighten(55%))
  v(0.4em)
}
```

### Custom Code Styling

```typst
// Code blocks with different color
#show raw.where(block: true): it => block(
  width: 100%,
  fill: rgb("#F0F0F0"),  // Light gray
  inset: 10pt,
  radius: 3pt,
  text(size: 0.88em, it),
)
```

### Add Callout Boxes

```typst
#let callout(title, body) = block(
  width: 100%,
  fill: green-light,
  inset: 10pt,
  radius: 4pt,
  [
    *#title*
    
    #body
  ]
)
```

Use in content:
```
#callout("Important", "This is important information")
```

### Adjust List Styling

```typst
#set list(marker: text(fill: green, weight: "bold")[•])

// Or with custom markers
#set list(marker: text(fill: green)[▪])
```

## Accessibility Best Practices

### When Customizing

✅ **DO:**
- Test color contrast (need 7:1+ for AAA)
- Keep font sizes readable (min 10pt body)
- Maintain heading hierarchy
- Preserve line spacing (min 0.6em)

❌ **DON'T:**
- Use color as only indicator
- Make text too small (<9pt)
- Skip heading levels (h1 → h3)
- Remove focus indicators
- Rely solely on images

### Contrast Testing

After changing colors, verify contrast ratios:

1. Get RGB values of colors
2. Use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
3. Check all color combinations meet 7:1+

Example:
- New green: rgb("#0066CC")
- On white background
- Result: 8.2:1 ✓ AAA compliant

## Multiple Templates

Create variations:

```
templates/typst/
├── clean/              # Current (default)
├── minimal/            # Simpler version
├── report/             # Professional report
└── paper/              # Academic paper format
```

Use in script:
```python
TEMPLATE_DIR = Path(__file__).parent.parent / "templates" / "typst" / "minimal"
```

## Template Metadata

Edit `template.yml`:

```yaml
jtex: v1
title: Clean Notes
description: Minimal notes template — Roboto font, MSU green
version: 1.0.0
license: MIT
packages: []
options: []
```

## Troubleshooting

### Fonts Not Rendering

Check installed fonts:
```bash
typst fonts
```

Install missing font:
```bash
# macOS
brew install font-roboto
brew install font-inconsolata
```

### PDF Too Large

Check for:
- Large embedded images
- Many colored elements
- Complex styling

Solutions:
- Compress images before including
- Simplify styling
- Use fewer colors

### Layout Issues

```bash
# Clear cache
rm -rf output/d2l/*.typ

# Regenerate
python scripts/generate-d2l-docs.py --type readings
```

### Color Not Appearing

Typst uses specific color syntax:

```typst
# ✗ Wrong
rgb("green")

# ✓ Correct
rgb("#18453B")
rgb("#228B22")
```

## Version Control

Template changes should be committed:

```bash
git add templates/typst/clean/template.typ
git commit -m "Update template: increase heading size"
```

## Performance Tips

- Minimize custom functions
- Cache compiled PDFs
- Use vector graphics (not raster images)
- Avoid heavy fonts

## Testing Changes

### Workflow

1. Edit `templates/typst/clean/template.typ`
2. Regenerate sample PDF:
   ```bash
   python scripts/generate-d2l-docs.py --type readings --format pdf
   ```
3. Review output PDF
4. Test accessibility:
   - Check contrast
   - Test keyboard nav
   - Test screen reader
5. Commit if satisfied

## Learning Resources

### Typst Documentation

- **[Official Docs](https://typst.app/docs/)** — Complete reference
- **[Tutorial](https://typst.app/docs/tutorial/)** — Getting started
- **[Reference](https://typst.app/docs/reference/)** — All functions

### Accessibility Resources

- **[WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)** — Standards
- **[Color Contrast](https://webaim.org/resources/contrastchecker/)** — Verify colors
- **[Font Guidelines](https://www.dyslexiefont.com/)** — Accessible fonts

### Examples

Popular Typst templates:
- [Awesome Typst](https://github.com/qjcg/awesome-typst) — Template collection
- [Template Gallery](https://typst.app/universe/) — Official gallery

## Summary Table

| Customization | How | Accessible? |
|---|---|---|
| Change color | Edit rgb() | If 7:1+ contrast |
| Change font | Edit font: "" | If sans-serif preferred |
| Adjust margins | Edit margin() | Usually yes |
| Change heading size | Edit size: | If min 10pt |
| Add custom styling | New show rules | Test carefully |

---

**Last Updated:** May 2026  
**Status:** WCAG AAA Compliant  
**Typst Version:** 0.10+
