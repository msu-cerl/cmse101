---
title: "Accessibility Features"
description: "WCAG AAA and UDL compliance guide"
weight: 3
---

# Accessibility Features & WCAG AAA Compliance

This site includes a **separate accessibility layer** that provides WCAG AAA and UDL (Universal Design for Learning) compliance without modifying the base theme.

## What's Included

### 🎯 Core Features

1. **Skip Navigation Link** — Keyboard users jump to main content (Tab at page top)
2. **ARIA Landmarks** — Semantic roles for screen readers (`main`, `nav`, `contentinfo`)
3. **Enhanced Focus Styles** — 3px white outline with 2px offset for keyboard navigation
4. **Color Contrast** — All text meets 7:1+ AAA ratio (dark theme, white text)
5. **Form Accessibility** — Proper labels, 44px touch targets, error messaging
6. **Reduced Motion Support** — Respects `prefers-reduced-motion` user preference
7. **Dark/Light Mode** — Adapts to `prefers-color-scheme` setting
8. **Alt Text Validation** — Build-time checks for missing image descriptions
9. **Print-Friendly Styles** — Optimized for paper and PDF output
10. **Screen Reader Support** — Content hidden from view but available to assistive tech

## WCAG AAA Compliance

All elements meet or exceed AAA (Triple-A) standards:

| Criterion | Level | Details |
|-----------|-------|---------|
| Alternative Text | A | All images require alt text |
| Color Contrast | AAA | 7:1+ ratio on all text |
| Focus Visible | AAA | 3px outline, clearly visible |
| Keyboard Accessible | A | All features work without mouse |
| Heading Hierarchy | A | h1 → h2 → h3 (no skipping) |
| Form Labels | A | All inputs have associated labels |
| Reduced Motion | AAA | Disabled for users preferring no animation |
| Text Spacing | AAA | No restrictions on customization |

### Color Contrast Ratios

| Element | Color | Ratio | Standard |
|---------|-------|-------|----------|
| Body text | White (#ffffff) | 18.92:1 | AAA ✓ |
| Links | Cyan (#58a6ff) | 7.49:1 | AAA ✓ |
| Link hover | Bright cyan (#79c0ff) | 9.73:1 | AAA ✓ |
| Link visited | Purple (#bc8ef8) | 7.54:1 | AAA ✓ |
| Success text | Green (#3fb950) | 7.45:1 | AAA ✓ |
| Error text | Red (#ff8888) | 8.23:1 | AAA ✓ |
| Warning text | Yellow (#d29922) | 7.50:1 | AAA ✓ |
| Footer text | Gray (luma 80) | 8.06:1 | AAA ✓ |

**Background:** #0d1117 (very dark)

## File Structure

```
/layouts/partials/accessibility/
  ├── skip-nav.html              # Skip to main content link
  └── aria-landmarks.html        # Semantic role support

/layouts/shortcodes/
  ├── img-a11y.html              # Enforces alt text on images
  └── form-input.html            # Accessible form fields

/layouts/_default/
  └── baseof.html                # Override: adds a11y CSS + partials

/static/css/
  └── accessibility.css          # All WCAG AAA styles

/scripts/
  └── validate-accessibility.js  # Build-time validation

config.yaml                        # a11y configuration
```

## Configuration

### Enable/Disable

In `config.yaml`:

```yaml
params:
  a11y:
    enabled: true                 # Master switch
    enforceAltText: true          # Validate alt text
    enableSkipNav: true           # Show skip link
    enableLandmarks: true         # Add ARIA roles
```

### Toggle at Build Time

```bash
# Disable accessibility temporarily
hugo -c 'params.a11y.enabled=false'
```

## For Content Authors

### Images (Markdown)

Always include descriptive alt text:

```markdown
# Good ✓
![Student working at a computer with course materials open](learning-image.png)

# Bad ✗
![image](learning-image.png)
```

Or use the shortcode that enforces alt text:

```markdown
{{< img-a11y src="image.png" alt="Clear description" title="Optional title" >}}
```

### Forms

Use the accessible form shortcode:

```markdown
{{< form-input type="email" name="email" label="Email Address" required="true" >}}
```

### Heading Hierarchy

Never skip heading levels:

```markdown
# Title (h1)           ← Top level

## Section (h2)        ← Second level (correct)

### Subsection (h3)    ← Third level (correct)

# Another h1           ✓ Correct: go back to h1

### Skipped h2 (h3) ✗  ✗ Wrong: skipped level
```

## For Developers

### Custom Components

Use semantic HTML and ARIA roles:

```html
<!-- ✓ Correct -->
<nav role="navigation">
  <a href="/" aria-current="page">Home</a>
</nav>

<main role="main">
  Content here
</main>

<!-- Skip link support -->
{{ partial "accessibility/skip-nav.html" . }}

<!-- Screen reader only text -->
<span class="sr-only">Additional context for screen readers</span>
```

### Form Structure

```html
<div class="form-group">
  <label for="user-email">Email Address</label>
  <input id="user-email" name="email" type="email" required>
  <div class="form-error" role="alert" id="email-error"></div>
</div>
```

### CSS Classes Available

```css
.sr-only              /* Screen reader only (hidden visually) */
.print-hidden         /* Hide from print */
.keyboard-focus       /* Enhance focus visibility */
.form-group           /* Form field wrapper */
.form-error           /* Error message styling */
.form-success         /* Success message styling */
```

## Keyboard Navigation

### Full site works without a mouse

| Key | Action |
|-----|--------|
| `Tab` | Move to next element (shows skip link) |
| `Shift+Tab` | Move to previous element |
| `Enter` | Activate link or button |
| `Space` | Toggle checkbox/button |
| `Escape` | Close menu (if implemented) |

### Skip Link

1. Press `Tab` when page loads
2. "Skip to main content" link appears at top
3. Press `Enter` to jump to content
4. Reduces keyboard navigation time by 50+%

## Screen Reader Testing

Tested with:

- ✅ **NVDA** (Windows) — Free, open source
- ✅ **JAWS** (Windows) — Industry standard
- ✅ **VoiceOver** (macOS/iOS) — Built-in
- ✅ **TalkBack** (Android) — Built-in

## Browser Support

- ✅ Chrome/Edge (99+)
- ✅ Firefox (97+)
- ✅ Safari (15+)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Accessibility Validation

### Manual Testing

1. **Keyboard only**: Navigate entire site without mouse
2. **Color contrast**: Check with [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
3. **Screen reader**: Test with VoiceOver (Mac) or NVDA (Windows)
4. **Zoom**: Test at 200% zoom level
5. **Reduced motion**: Test with `prefers-reduced-motion` enabled

### Automated Testing

Run validation script:

```bash
hugo
node scripts/validate-accessibility.js
```

Checks for:
- ❌ Missing alt text (errors)
- ⚠️ Broken heading hierarchy (warnings)
- ⚠️ Form labels missing (warnings)
- ⚠️ Skip navigation link present (warnings)

## UDL (Universal Design for Learning)

This site implements principles of UDL:

### Multiple Means of Representation

- **Text** — All content in accessible markdown
- **Color + icons** — Redundant coding (not color-only)
- **Headings** — Proper hierarchy for structure
- **Multiple formats** — PDF, DOCX, HTML

### Multiple Means of Engagement

- **Student choice** — Dark/light mode
- **Keyboard + mouse** — Both work fully
- **Adjustable text** — Can zoom to 200%
- **Skip options** — Jump to main content

### Multiple Means of Expression

- **D2L uploads** — PDF, DOCX, web
- **Different devices** — Phone, tablet, desktop
- **Offline access** — Download PDFs
- **Editable formats** — Can annotate DOCX

## Common Accessibility Issues & Fixes

### Problem: Images have no alt text

```markdown
# Bad ✗
![](screenshot.png)

# Good ✓
![Course dashboard showing weekly schedule and assignments](screenshot.png)
```

### Problem: Buttons not keyboard accessible

```html
# Bad ✗
<div onClick="doSomething()">Click me</div>

# Good ✓
<button onclick="doSomething()">Click me</button>
```

### Problem: Color is the only indicator

```markdown
# Bad ✗
Red text = error

# Good ✓
⚠️ Error: [red text with icon and message]
```

### Problem: Form fields lack labels

```html
# Bad ✗
<input type="email">

# Good ✓
<label for="email">Email Address</label>
<input id="email" type="email">
```

## Further Resources

### Standards & Guidelines

- **[WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)** — Official standard
- **[UDL Guidelines](https://udlguidelines.cast.org/)** — Learning design
- **[WebAIM](https://webaim.org/)** — Practical guides

### Testing Tools

- **[axe DevTools](https://www.deque.com/axe/devtools/)** — Browser extension
- **[WAVE](https://wave.webaim.org/)** — Web accessibility tool
- **[Lighthouse](https://developers.google.com/web/tools/lighthouse)** — Google's audit tool

### Color Checkers

- **[WebAIM Contrast](https://webaim.org/resources/contrastchecker/)** — Check contrast
- **[Color Brewer](https://colorbrewer2.org/)** — Accessible color palettes

## Support

### Questions?

- Check [System Overview](../overview/)
- See specific documentation pages
- Review code comments in `static/css/accessibility.css`

### Report Issues

Found an accessibility problem?

1. Test in multiple browsers
2. Document the issue clearly
3. Report with steps to reproduce

### Get Involved

This is open source! Contributions welcome:

- Suggest accessibility improvements
- Report bugs
- Improve documentation
- Test with assistive technologies

## Standards Compliance Summary

| Standard | Level | Status |
|----------|-------|--------|
| WCAG 2.1 | AAA | ✅ Compliant |
| Section 508 | - | ✅ Compliant |
| ADA | - | ✅ Accessible |
| UDL | - | ✅ Implemented |

---

**Last Updated:** May 2026  
**Status:** WCAG AAA Compliant  
**Tested:** Chrome, Firefox, Safari, Edge, Mobile
