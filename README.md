# AI and Society Course Website

This repository contains the source materials for the "AI and Society" course. The site is built with Hugo and provides readings, assignments, and course information in an accessible, multi-format system.

## 📋 Contents

- **content/readings/** - Weekly reading materials and discussion prompts
- **content/assignments/** - Course assignments with rubrics
- **content/docs/** - Syllabus and additional resources
- **scripts/** - Conversion and setup utilities
- **config.toml** - Hugo configuration

## 🚀 Quick Start

### Prerequisites

- Hugo (extended version)
- Pandoc (for PDF/Word conversion)
- Git

### Setup

1. Clone this repository
2. Run the setup script:
   ```bash
   bash scripts/setup-hugo.sh
   ```

3. Configure `config.toml` with your course details

4. Start the development server:
   ```bash
   hugo server
   ```

5. Visit `http://localhost:1313` in your browser

## 📝 Adding Content

### Add a Reading

Create a new file in `content/readings/`:

```bash
# Week 2 readings
touch content/readings/week-2.md
```

Edit the file with frontmatter:

```yaml
---
title: "Week 2: Ethics and Bias"
weight: 2
---

# Week 2 content here...
```

### Add an Assignment

Create a new file in `content/assignments/`:

```bash
touch content/assignments/discussion-posts.md
```

### Add a Resource

Create a new file in `content/docs/`:

```bash
touch content/docs/glossary.md
```

## 🔄 Generate PDF & Word Documents

Convert all markdown to PDF and Word formats for D2L:

```bash
bash scripts/convert-to-formats.sh
```

Output files will be in the `output/` directory ready to upload to Brightspace.

## 🌐 Publishing

### GitHub Pages

1. Push to the `main` branch
2. GitHub Actions automatically builds and deploys
3. Site is available at `https://yourusername.github.io/ai-and-society/`

### Custom Domain

Update the `cname` field in `.github/workflows/build-deploy.yml` to use a custom domain.

## ♿ Accessibility Features

This site follows UDL (Universal Design for Learning) and WCAG 2.1 AA standards:

- Semantic HTML structure
- Proper heading hierarchy
- Alt text for all images
- High contrast color scheme
- Multiple format options (web, PDF, Word)
- Skip navigation links

## 📚 Integrating with D2L Brightspace

### Option 1: Link to Public Site
- Add links to course modules pointing to this site
- Students can access readings anytime

### Option 2: Upload Converted Documents
```bash
bash scripts/convert-to-formats.sh
# Upload output/docx/ files to D2L content library
```

### Option 3: Embed Content
- D2L allows embedding external HTML content
- Configure via Content > Insert Learning Object > External Learning Tool

## 🔐 Private Content

To make content private or restrict to enrolled students:

1. Use D2L's native content library
2. Host converted documents on your institution's secure server
3. Configure Hugo to build a private version

## 🛠️ Customization

### Change Theme

The default theme is [Hugo Book](https://github.com/alex-shpak/hugo-book). To use a different theme:

```bash
# Remove current theme
rm -rf themes/book

# Clone a new theme
git clone [theme-repo-url] themes/[theme-name]

# Update config.toml
# theme = "new-theme-name"
```

### Customize Colors and Styling

Edit `themes/book/assets/` or create custom CSS:

```bash
mkdir -p static/css
# Create custom-style.css
```

Update `config.toml` to reference your custom styles.

## 📖 Pandoc Customization

### Reference Document

For more control over Word output, create a reference document:

```bash
pandoc -o reference.docx --print-default-data-file reference.docx
# Edit reference.docx with your institution's styles
# Place in project root
```

### PDF Styling

Edit `pdf-header.tex` to customize PDF appearance and accessibility.

## 🐛 Troubleshooting

### Hugo Server Won't Start

```bash
# Clear cache
rm -rf resources/

# Try again
hugo server
```

### Pandoc Conversion Fails

```bash
# Check Pandoc is installed
pandoc --version

# Install missing dependencies
# macOS
brew install pandoc

# Linux
sudo apt-get install pandoc texlive-latex-base texlive-latex-extra
```

### GitHub Actions Deploy Fails

1. Check `.github/workflows/build-deploy.yml` for CNAME settings
2. Ensure `main` branch exists and is default branch
3. Enable GitHub Pages in repository settings

## 📞 Support

- **Hugo Docs:** https://gohugo.io/documentation/
- **Book Theme:** https://github.com/alex-shpak/hugo-book
- **Pandoc Manual:** https://pandoc.org/
- **UDL Resources:** https://www.cast.org/

## 📄 License

This template is provided as-is for educational use. Customize and adapt for your institution.

---

**Last Updated:** May 2026  
**Maintained By:** [Your Name]  
**Feedback:** [your.email@institution.edu]
