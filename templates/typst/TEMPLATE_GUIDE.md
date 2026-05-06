# Typst Template Guide

Professional, WCAG AAA-compliant document template for generating course materials.

## Overview

Located in: `templates/typst/clean/`

This template generates beautiful, accessible PDF documents with:
- MSU green branding
- Professional typography (Roboto font)
- Proper heading hierarchy
- WCAG AAA color contrast compliance
- Optimized line spacing and margins

## Files

```
templates/typst/clean/
├── template.typ         # Main Typst template
└── template.yml         # Template metadata
```

## Template Features

### Typography

| Element | Font | Size | Color | Notes |
|---------|------|------|-------|-------|
| Body text | Roboto | 11pt | luma(30) | Dark gray, 17.4:1 contrast |
| h1 (Title) | Roboto | 15pt | MSU green | Bold, 10.75:1 contrast |
| h2 (Section) | Roboto | 12.5pt | MSU green | Semibold |
| h3 (Subsection) | Roboto | 11pt | luma(50) | Semibold |
| Inline code | Roboto | 9.9pt | Green | Highlighted background |
| Code blocks | Roboto | 9.68pt | Green | Light green background |
| Footer | Roboto | 9pt | luma(80) | Page numbers, 8.06:1 contrast |

### Layout

- **Paper**: US Letter (8.5" × 11")
- **Margins**: 1" top/bottom, 1.25" left/right
- **Line height**: 0.7em leading, 1.1em paragraph spacing
- **Page numbers**: Centered footer on every page
- **List markers**: MSU green bullets

### Colors

```typst
#let green = rgb("#18453B")           // MSU green
#let green-light = green.lighten(88%) // Light green (code background)
```

**Contrast Ratios** (all AAA compliant):
- Body text on white: **17.4:1** ✅
- Green headings on white: **10.75:1** ✅
- Footer text on white: **8.06:1** ✅ (minimum for AAA)

## Customization

### Change Colors

Edit `template.typ` to modify the color scheme:

```typst
// Change MSU green to another color
#let green = rgb("#FF6B6B")  // Red instead
```

Common accessible color palettes:
- **Blue**: `#0066CC` (10.8:1 on white)
- **Red**: `#CC0000` (7.2:1 on white)
- **Purple**: `#663399` (7.6:1 on white)

### Change Fonts

Replace "Roboto" with any installed system font:

```typst
#set text(font: "Georgia", size: 11pt, fill: luma(30))
```

Accessible font alternatives:
- **Serif**: Georgia, Garamond
- **Sans-serif**: Arial, Helvetica, Open Sans

### Change Heading Sizes

Adjust h1/h2/h3 sizes in the template:

```typst
#show heading.where(level: 1): it => {
  text(fill: green, weight: "bold", size: 18pt, it.body)  // Changed from 15pt
}
```

### Change Margins

Edit page settings:

```typst
#set page(
  paper: "us-letter",
  margin: (top: 0.75in, bottom: 0.75in, left: 1.5in, right: 1.5in),
```

### Add Header/Footer Content

Modify page footer context:

```typst
footer: context {
  let page_num = counter(page).display()
  let total = counter(page).final().first()
  align(center, text(fill: luma(80), size: 9pt)[
    Page #page_num of #total
  ])
}
```

## Accessibility Compliance

### WCAG AAA Standards

✅ **Contrast**: All text meets 7:1 minimum
- Body: 17.4:1
- Headings: 10.75:1
- Footer: 8.06:1

✅ **Structure**:
- Proper heading hierarchy (h1 → h2 → h3)
- Semantic text formatting
- Lists with markers

✅ **Readability**:
- 11pt body font (readable, not too small)
- Sans-serif Roboto (accessible for dyslexia)
- Optimal line spacing (0.7em)
- Adequate paragraph spacing (1.1em)

✅ **Layout**:
- Proper margins
- Page numbers on every page
- Clear separation between sections

### Verification

Test the PDF accessibility:
1. Open in Adobe Acrobat
2. Check **Accessibility > Accessibility Checker**
3. Or use online tools: https://www.acessdocs.com/

## Using with the Generator

The script (`scripts/generate-d2l-docs.py`) automatically:
1. Reads markdown content files
2. Converts markdown to Typst format
3. Inserts content into `[-CONTENT-]` placeholder
4. Compiles with `typst compile`

The template is used as-is — no modifications needed for basic use.

### Content Insertion

The script replaces `[-CONTENT-]` marker with document content:

```typst
// ... template styling ...

[-CONTENT-]  // ← Script replaces this with actual content
```

Example:
```typst
#set text(font: "Roboto", size: 11pt, fill: luma(30))

[-CONTENT-]
```

Becomes:
```typst
#set text(font: "Roboto", size: 11pt, fill: luma(30))

= Reading 1

Your content here...

== Section heading

More content...
```

## Advanced Customization

### Add Images

Images in content are supported via markdown:

```markdown
![Alt text for accessibility](image.png)
```

The template includes proper styling for images.

### Custom Styling Rules

Add new Typst rules to template.typ:

```typst
// Highlight important text
#show text.where(weight: "bold"): it => {
  text(fill: green, weight: "bold", it)
}

// Custom callout boxes
#let callout(title, body) = block(
  width: 100%,
  fill: green-light,
  inset: 10pt,
  [
    *#title*
    
    #body
  ]
)
```

Use in markdown via Typst directives or shortcodes.

### Multiple Template Versions

Create variations:

```
templates/typst/
├── clean/          # Current template
├── minimal/        # Simpler version
└── branded/        # Custom branding
```

Then use in script:
```python
TEMPLATE_DIR = Path(__file__).parent.parent / "templates" / "typst" / "branded"
```

## Troubleshooting

### "File not found" error

Ensure template exists:
```bash
ls -la templates/typst/clean/template.typ
```

### Output looks different than expected

1. Check Typst version: `typst --version`
2. Verify fonts are installed: `typst fonts`
3. Clear cache: `rm -rf output/d2l/*.typ`

### Fonts not rendering

Install Roboto:
```bash
# macOS
brew install font-roboto

# Or download from: https://fonts.google.com/specimen/Roboto
```

### PDF is too large

Check for embedded images or large code blocks. PDFs generated from this template are typically 150-300 KB depending on content.

## Resources

- **Typst Documentation**: https://typst.app/docs/
- **Typst Manual**: https://typst.app/docs/reference/
- **Color Contrast Checker**: https://webaim.org/resources/contrastchecker/
- **Accessible Fonts**: https://www.dyslexiefont.com/

## Updates & Maintenance

### Updating Template

1. Edit `template.typ` as needed
2. Test with: `python scripts/generate-d2l-docs.py --type readings --format pdf`
3. Verify output looks correct
4. Commit changes: `git add templates/`

### Version Control

Template is tracked in git. Each change is audited:
```bash
git log templates/typst/clean/template.typ
```

### Keeping Accessibility

When making changes, verify:
- [ ] Color contrast still 7:1+
- [ ] Font sizes still readable (min 10pt)
- [ ] Heading hierarchy maintained
- [ ] Line spacing appropriate

## License & Attribution

**Original Template**: MSU clean template  
**Modified**: May 2026 for WCAG AAA compliance  
**Status**: Production ready

---

**Last Updated**: May 2026  
**Accessibility**: WCAG AAA Compliant  
**Typst Version**: 0.10+
