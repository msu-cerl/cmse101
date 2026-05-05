# Project Structure & File Guide

## Quick Navigation

This template includes everything you need to build an accessible, multi-format AI and Society course site. Here's what each file/folder does:

---

## 📁 Directory Structure

```
ai-and-society/
├── 📄 README.md                    ← START HERE: Overview and setup
├── 📄 CUSTOMIZATION.md             ← How to customize Hugo and markdown
├── 📄 D2L-INTEGRATION.md           ← How to integrate with Brightspace
├── 📄 LAUNCH-CHECKLIST.md          ← Pre-launch verification checklist
├── 📄 GETTING-STARTED-STUDENT.md   ← Handout for students
│
├── 📋 config.toml                  ← Hugo site configuration
├── 📋 .gitignore                   ← Git ignore patterns
│
├── 📚 content/
│   ├── _index.md                   ← Homepage
│   ├── readings/
│   │   ├── _index.md               ← Readings overview page
│   │   ├── week-1.md               ← Example: Week 1 readings
│   │   └── week-2.md               ← Add more weeks as needed
│   ├── assignments/
│   │   ├── _index.md               ← Assignments overview
│   │   ├── reading-reflections.md  ← Weekly reflection assignment
│   │   ├── midterm-assignment.md   ← Midterm project
│   │   └── final-project.md        ← Capstone project
│   └── docs/
│       ├── syllabus.md             ← Course syllabus
│       ├── resources.md            ← Links and references
│       └── getting-started.md      ← Student getting started guide
│
├── 🔨 scripts/
│   ├── setup-hugo.sh               ← Initialize Hugo with theme
│   └── convert-to-formats.sh       ← Generate PDF/Word from markdown
│
├── ⚙️ .github/
│   └── workflows/
│       └── build-deploy.yml        ← GitHub Actions deployment
│
├── 🎨 themes/
│   └── book/                       ← Hugo theme (downloaded)
│       └── [theme files]
│
└── 📦 output/ (generated)
    ├── pdf/                        ← Generated PDFs
    └── docx/                       ← Generated Word documents
```

---

## 📄 Important Files Explained

### Configuration & Setup

**`config.toml`**
- Main Hugo configuration
- Edit here to:
  - Change site title
  - Add navigation menu items
  - Configure theme options
  - Set GitHub edit links
- **Edit this first!**

**`.gitignore`**
- Tells Git what to ignore
- Don't commit: `output/`, `resources/`, `themes/book/.git`
- Already configured; usually no changes needed

### Documentation

**`README.md`**
- Main documentation
- How to setup, customize, publish
- Troubleshooting section
- **Read first if you're confused**

**`CUSTOMIZATION.md`**
- Markdown syntax guide
- Hugo/Hugo Book customization
- Accessibility best practices
- Frontmatter reference

**`D2L-INTEGRATION.md`**
- Three ways to integrate with Brightspace
- Recommended hybrid approach
- D2L-specific tips

**`LAUNCH-CHECKLIST.md`**
- Pre-launch verification
- GitHub setup
- Accessibility testing
- Brightspace integration steps

**`GETTING-STARTED-STUDENT.md`**
- Handout for students
- How to navigate the site
- Accessibility features
- FAQs

### Course Content

**`content/_index.md`**
- Homepage content
- First thing students see
- Update with course overview

**`content/readings/`**
- Weekly reading materials
- `_index.md` = overview page
- `week-1.md`, `week-2.md`, etc. = individual weeks
- **Add/edit week files here**

**`content/assignments/`**
- All assignment details
- `_index.md` = list of all assignments
- Individual files for each assignment type
- **Edit assignment deadlines and rubrics here**

**`content/docs/`**
- Course syllabus
- Resources and links
- Getting started guide
- **Edit syllabus with your actual policies**

### Scripts

**`scripts/setup-hugo.sh`**
- One-time setup script
- Downloads Hugo Book theme
- Creates necessary files
- Run once with: `bash scripts/setup-hugo.sh`

**`scripts/convert-to-formats.sh`**
- Converts all markdown to PDF and Word
- Creates `output/` directory with documents
- Run with: `bash scripts/convert-to-formats.sh`
- Run every time you update content before uploading to D2L

### GitHub Actions

**`.github/workflows/build-deploy.yml`**
- Automated deployment workflow
- When you push to GitHub:
  1. Hugo builds the site
  2. Publishes to GitHub Pages
  3. Generates PDF/Word (optional)
- No changes usually needed; GitHub Actions does it automatically

---

## 🚀 Common Tasks

### Add a New Week of Readings

1. Create file: `content/readings/week-4.md`
2. Copy frontmatter from existing week
3. Change title and weight
4. Add content
5. Save and push to GitHub
6. Website updates automatically

### Update Assignment Details

1. Open: `content/assignments/reading-reflections.md`
2. Edit deadline, rubric, or instructions
3. Save and push to GitHub
4. Auto-updates on website

### Generate Documents for D2L

1. Run: `bash scripts/convert-to-formats.sh`
2. Check output/ folder for PDFs and Word docs
3. Upload to D2L
4. Update D2L links if needed

### Change Site Colors/Theme

1. Open: `config.toml`
2. Modify theme settings in `[params]` section
3. See `CUSTOMIZATION.md` for options
4. Save and rebuild locally: `hugo server`

### Fix a Typo or Formatting Issue

1. Edit the markdown file
2. Save
3. Commit and push to GitHub
4. Site updates in ~2 minutes (no action needed)

---

## 📝 Editing Workflow

### For Content Updates:

```
1. Open file in your editor
2. Make changes
3. Save file
4. git add .
5. git commit -m "Updated Week 2 readings"
6. git push origin main
7. Website auto-updates (GitHub Pages does this)
8. If using D2L documents: bash scripts/convert-to-formats.sh
9. Upload new files to D2L
```

### For Configuration Changes:

```
1. Edit config.toml
2. Test locally: hugo server
3. Check http://localhost:1313
4. Commit and push
5. Website updates automatically
```

---

## ✅ Maintenance Tasks

### Weekly
- Check website for any broken links
- Monitor D2L discussion for technical issues
- Review student feedback on navigation

### Before Each New Content Week
- Create new week file with readings
- Add assignment details
- Generate updated PDFs/Word docs
- Upload to D2L
- Test all links work

### Monthly
- Check for Hugo/theme updates
- Update Pandoc if needed
- Archive old document versions
- Review accessibility metrics

### End of Semester
- Archive course materials with version number
- Save generated PDFs in institution repository
- Document any issues/improvements for next semester
- Update CHANGELOG

---

## 🔗 File Dependencies

```
config.toml
    ↓
Defines site structure and theme
    ↓
themes/book/ (Hugo theme)
    ↓
Renders markdown files into HTML
    ↓
content/ (markdown files)
    ↓
Generates public/ (website)
    ↓
GitHub Pages (deploys automatically)

Separately:
content/ (markdown)
    ↓
Pandoc (conversion tool)
    ↓
output/pdf/ & output/docx/
    ↓
Manual upload to D2L
```

---

## 🎯 Most Likely Files You'll Edit

**Edit frequently:**
- `content/readings/*.md` - Add weekly readings
- `content/assignments/*.md` - Update due dates, instructions
- `config.toml` - Site-wide settings once

**Edit occasionally:**
- `content/docs/syllabus.md` - Semester policies
- `README.md` - Update project documentation
- `.github/workflows/build-deploy.yml` - Deployment settings

**Rarely edit:**
- `.gitignore` - Only if adding new file types to ignore
- `scripts/` - Only if customizing conversion process
- `themes/` - Only if changing to different theme

---

## 📦 Package Structure Summary

| Category | Purpose | Edit Frequency |
|----------|---------|-----------------|
| **Config** | Site settings | Once per semester |
| **Content** | Course materials | Weekly |
| **Scripts** | Build tools | As needed |
| **Workflows** | Auto-deploy | Rarely |
| **Docs** | Instructions | As needed |
| **Theme** | Visual design | Rarely |

---

## 🆘 If You're Stuck

1. **Site won't build?** → Check `README.md` troubleshooting
2. **Markdown syntax?** → See `CUSTOMIZATION.md`
3. **D2L questions?** → Check `D2L-INTEGRATION.md`
4. **Content organization?** → This file (file guide)
5. **Pre-launch checks?** → Use `LAUNCH-CHECKLIST.md`

---

**Pro tip:** Read `README.md` first. It answers most questions about setup and basic operations.

Keep this file bookmarked for reference!
