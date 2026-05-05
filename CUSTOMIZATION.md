# Hugo Book Theme Configuration Guide

## Quick Customization

### 1. Sidebar Navigation

Edit `config.toml` menu sections:

```toml
[[menu.main]]
  name = "Syllabus"
  url = "/docs/syllabus/"
  weight = 1
```

Weight determines order (lower = appears first).

### 2. Site Colors

Add to `config.toml`:

```toml
[params]
  ThemeColorMode = "light"  # or "dark"
  BookToc = true
  BookSearch = true
```

### 3. Edit This Page Links

Enable "Edit on GitHub":

```toml
[params]
  editURL = "https://github.com/yourusername/ai-and-society/edit/main/content/"
```

## Markdown Syntax

### Headings
```markdown
# H1 - Page title
## H2 - Section
### H3 - Subsection
```

### Lists
```markdown
- Bullet point
  - Nested bullet
  
1. Numbered item
2. Another item
```

### Tables
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

### Links
```markdown
[Link text](https://example.com)
[Internal link](../assignments/midterm-assignment/)
```

### Emphasis
```markdown
*italic* or _italic_
**bold** or __bold__
~~strikethrough~~
```

### Code
```markdown
Inline: `code snippet`

Code block:
\`\`\`python
print("hello")
\`\`\`
```

### Blockquotes
```markdown
> This is a quote
> - Attribution
```

## Accessibility Tips

### 1. Heading Structure
- Start with `# H1` for page title
- Use `##` for major sections
- Don't skip heading levels
- ✗ Don't do: H1 → H3 (skip H2)
- ✓ Do: H1 → H2 → H3

### 2. Links
- Use descriptive link text
- ✗ Don't: "Click here"
- ✓ Do: "Read the syllabus"

### 3. Images
- Always include alt text
- Describe image purpose, not just content

```markdown
![Graph showing AI adoption over time](../images/adoption-graph.png)
```

### 4. Lists
- Use proper markdown syntax
- Screen readers announce list structure

### 5. Color
- Don't convey information by color alone
- Use bold, italics, or labels too

### 6. Tables
- Keep structure simple
- Use clear headers
- Avoid merged cells

## Frontmatter Reference

Every markdown file should start with:

```yaml
---
title: "Page Title"           # Required
weight: 1                      # Optional: determines order
bookCollapseSection: false    # Optional: collapse in sidebar
description: "Page summary"   # Optional: for SEO
draft: false                  # Optional: hide from site
---
```

## Creating Collections

### Readings by Week

**Structure:**
```
content/
  readings/
    _index.md (overview)
    week-1.md
    week-2.md
    week-3.md
```

**_index.md example:**
```yaml
---
title: "Course Readings"
bookCollapseSection: true
weight: 10
---
```

### Assignments with Sections

**Structure:**
```
content/
  assignments/
    _index.md (list of all)
    reading-reflections.md
    midterm-assignment.md
    final-project.md
```

## Adding Metadata for Pandoc

Include in frontmatter for better PDF/Word output:

```yaml
---
title: "Assignment Title"
author: "Course Name"
date: 2026-05-05
keywords: "AI, ethics, assignment"
---
```

## Local Testing

### Build Site Locally

```bash
hugo server --buildDrafts
```

Visit: `http://localhost:1313`

### Build for Production

```bash
hugo --minify
```

Output in `public/` directory.

## Pandoc Conversion Options

### Convert Single File

```bash
# To PDF
pandoc input.md -o output.pdf --pdf-engine=xelatex

# To Word
pandoc input.md -o output.docx

# To HTML
pandoc input.md -o output.html
```

### Batch Convert

Use `scripts/convert-to-formats.sh` (see README).

## Advanced: Custom Shortcodes

Create reusable components in `layouts/shortcodes/`:

**Example: Alert box**
```
{{< alert "warning" >}}
Important note here
{{< /alert >}}
```

In markdown:
```markdown
{{< alert "warning" >}}
This is important!
{{< /alert >}}
```

---

For more Book theme options, see: https://github.com/alex-shpak/hugo-book/wiki
