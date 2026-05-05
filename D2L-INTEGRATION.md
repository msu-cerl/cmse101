# D2L Brightspace Integration Guide

## Quick Start: Three Integration Options

Choose the method that works best for your institution and students.

---

## Option 1: Link to Public Website (Recommended for open courses)

**Best for:** Courses that should be publicly accessible and updated frequently

### Steps:

1. **In D2L:**
   - Go to course content area
   - Click "Insert Learning Object" > "External Link Tool"
   - Add link to your course website
   - Title: "Course Readings and Materials"
   - Target: External website

2. **Example link:**
   ```
   https://yourusername.github.io/ai-and-society/
   ```

3. **Example embedded link to specific section:**
   ```
   https://yourusername.github.io/ai-and-society/readings/week-1/
   ```

### Pros:
- ✓ Single source of truth (no duplicate content)
- ✓ Updates immediately
- ✓ Students always see latest version
- ✓ Easy to maintain

### Cons:
- ✗ Students must leave D2L to access (though link opens in new tab)
- ✗ D2L gradebook doesn't track visit
- ✗ Requires internet access

### Usage Example:
Create folder in D2L:
- Course Readings (week-1)
  - [External Link] Week 1 Readings (points to website)
  - Assignment: Week 1 Reflection
  - Discussion: Week 1 Topics

---

## Option 2: Upload Converted Documents (Best for archival/hybrid models)

**Best for:** Institutions that want content in D2L library + want offline access

### Steps:

1. **Generate documents:**
   ```bash
   bash scripts/convert-to-formats.sh
   ```

2. **In D2L:**
   - Go to Content Library > Create Folder > "AI & Society Course Materials"
   - Upload files from `output/docx/`
   - Create links in course modules to library

3. **Example structure in D2L:**
   ```
   Week 1: AI Fundamentals
   ├── Reading: AI Fundamentals (Word doc link)
   ├── Reading: ML Basics (Word doc link)
   ├── Assignment: Reading Reflection
   └── Discussion: Week 1 Topics
   ```

### Pros:
- ✓ Content stored in D2L (good for institutional records)
- ✓ Students can download and work offline
- ✓ Can track document access
- ✓ Works if website goes down

### Cons:
- ✗ Must manually update when content changes
- ✗ Version control issues (which is current?)
- ✗ Requires regenerating documents each update

### Workflow:
```
Edit markdown → Commit to GitHub → Run convert script → Upload to D2L
```

---

## Option 3: Embed Website in D2L (Seamless but limited)

**Best for:** Courses that want single interface but dynamic content

### Steps:

1. **In D2L:**
   - Go to course content
   - Click "Insert Learning Object" > "Existing Activities"
   - Select "External Learning Tool" or "IFrame"
   - Configure with course website URL

2. **Embed specific sections:**
   ```html
   <iframe src="https://yourusername.github.io/ai-and-society/readings/" 
           width="100%" height="800px" style="border:none;"></iframe>
   ```

### Pros:
- ✓ Content visible directly in D2L
- ✓ Updates automatically from website
- ✓ Single interface for students

### Cons:
- ✗ D2L's iframe security may block some features
- ✗ Navigation may be confusing within iframe
- ✗ Some university policies restrict embedded content

---

## Recommended Hybrid Approach

**Use Option 1 + 2:**

1. **Link to website in D2L** for primary access
2. **Provide downloadable Word/PDF versions** via content library for:
   - Students with connectivity issues
   - Students who want to print
   - Offline access
   - Students using assistive technology

### D2L Structure:
```
Week 1: Fundamentals
├─ 📚 Read online: [Link to website readings]
├─ 📥 Download: 
│   ├─ Readings as Word (link to content library)
│   ├─ Readings as PDF (link to content library)
├─ ✍️ Assignment: Reading Reflection
└─ 💬 Discussion: What questions do you have?
```

---

## Managing Document Updates

### When Content Changes:

1. **Edit markdown** in your GitHub repo
2. **Test locally:** `hugo server`
3. **Commit and push** to GitHub
4. **Website updates automatically** (2 min deploy)
5. **If using D2L documents:**
   - Regenerate: `bash scripts/convert-to-formats.sh`
   - Upload new versions to D2L with date stamp
   - Update links or create new entries
   - Consider adding version numbers to filenames

### Naming convention for documents:
```
Readings-Week1-v2.docx    (version 2)
Readings-Week1-2026-05-05.docx    (dated)
Readings-Week1-FINAL.docx    (stage label)
```

---

## Brightspace Content Tools

### Adding External Links:

**Create visible links:**
- Title it clearly: "Course Website - Readings"
- Use descriptive link text, not just "Click here"
- Test link before publishing
- Consider adding context: "This content is also available in PDF and Word formats below"

### Adding Files:

**Upload documents:**
- Use semantic filenames
- Add descriptions in D2L
- Test file opens in students' browsers
- Include clear instructions (e.g., "Download to edit" vs "View online")

### Content Library:

**For reusable materials:**
1. Create folder: "AI & Society Course Materials"
2. Upload all course documents
3. Link from each weekly module
4. Benefits:
   - Single source for all documents
   - Easy to update in one place
   - Students can browse library

---

## Accessibility in D2L

### When linking to website:
- Use descriptive link text: "Course readings for Week 1" not "Click here"
- Provide alternative formats in accompanying text
- Test links work in screen readers

### When uploading documents:
- Use Word documents with semantic heading structure
- Test PDFs are tagged and accessible
- Provide plain text summaries if complex
- Include alt text for any images

### Example D2L entry:
```
Readings: Week 1 - AI Fundamentals

📖 Read online: [View readings on course website]

📥 Alternative formats:
   • [Download as Word document]
   • [Download as PDF]
   • [Audio version available - email instructor]

If you have accessibility needs, contact Disability Services.
```

---

## Troubleshooting

### Students can't access website
- Confirm URL is correct
- Check if your institution blocks GitHub Pages
- Provide direct link vs shortened URL
- Offer D2L document versions as backup

### Website embed doesn't work
- Check iframe settings in D2L security
- May need to whitelist your GitHub Pages URL
- Contact D2L/IT support
- Fall back to Option 1 (link) instead

### Documents look wrong in D2L
- Test different file formats (docx vs pdf)
- Check browser compatibility
- Consider PDF instead of Word if formatting breaks
- Test on multiple devices

### Version confusion
- Clearly label versions with dates
- Keep old versions for reference
- Archive past semesters separately
- Consider adding "Current as of May 5, 2026" in header

---

## Brightspace to GitHub Sync (Advanced)

If your institution allows:

1. **Set up webhook** from GitHub to trigger D2L updates
2. **Automated workflow:**
   - Push to GitHub
   - GitHub Actions generates PDFs
   - Automatically uploads to D2L
   - Sends notification to instructor
3. **Tools:**
   - GitHub Actions + Brightspace API
   - Requires D2L integration credentials

---

## Checklist for D2L Integration

Before semester starts:

- [ ] Choose integration option (1, 2, or combo)
- [ ] Test all links work
- [ ] Verify documents display correctly
- [ ] Confirm students can download if needed
- [ ] Test on mobile device
- [ ] Run accessibility check
- [ ] Write clear instructions for students
- [ ] Send test access to teaching assistant
- [ ] Prepare documentation for student FAQ
- [ ] Set up versioning system

---

For D2L support: Contact your institution's Learning Management System team.
