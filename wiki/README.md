# GitHub Wiki Setup Guide

## 📚 Wiki Pages Created

Successfully created comprehensive wiki documentation for all notebooks in the Botanical Colabs library.

### ✅ Completed Wiki Pages (10 pages)

1. **Home.md** — Main wiki landing page with navigation
2. **TEMPLATE-MyST-Scientific.md** — MyST scientific documentation template (~300 lines)
3. **TEMPLATE-Marp-Presentation.md** — Marp presentation template (~400 lines)
4. **TEMPLATE-Botanical-Notebook.md** — Original botanical template (~600 lines)
5. **TEMPLATE-Data-Analysis.md** — Data analysis framework (~400 lines)
6. **TEMPLATE-Machine-Learning.md** — ML pipeline template (~500 lines)
7. **TEMPLATE-Environmental-Monitoring.md** — Environmental sensors template (~350 lines)
8. **Examples-Plant-Card-Generator.md** — Multi-source plant cards (~500 lines)
9. **Examples-Batch-Plant-Cards.md** — Batch processing system (~450 lines)
10. **Education-Tutorial.md** — Beginner-friendly tutorial (~400 lines)

**Total:** ~3,900 lines of comprehensive documentation

---

## 🚀 How to Push to GitHub Wiki

### Method 1: Using Git (Recommended)

```powershell
# 1. Clone the wiki repository
git clone https://github.com/outobecca/botanical-colabs.wiki.git

# 2. Navigate to wiki directory
cd botanical-colabs.wiki

# 3. Copy all wiki markdown files
# From: c:\Users\pekka\OneDrive\Työpöytä\botanical-colab-notebooks\wiki\*.md
# To: botanical-colabs.wiki\

# Copy files (PowerShell)
Copy-Item "c:\Users\pekka\OneDrive\Työpöytä\botanical-colab-notebooks\wiki\*.md" -Destination . -Force

# 4. Add all files
git add *.md

# 5. Commit changes
git commit -m "Add comprehensive wiki documentation for all notebooks"

# 6. Push to GitHub
git push origin master

# 7. Visit your wiki
# https://github.com/outobecca/botanical-colabs/wiki
```

### Method 2: Manual Upload (Alternative)

1. Go to https://github.com/outobecca/botanical-colabs/wiki
2. Click "New Page" for each wiki page
3. Copy content from corresponding .md file
4. Save each page

---

## 📊 Wiki Structure

### Home Page
- Quick navigation to all notebooks (organized by category)
- What's New in Version 2.0
- Getting Started guides
- Key features overview
- Notebook statistics

### Template Pages (6 pages)
Each template page includes:
- Overview and use cases
- Key features with code examples
- What's included
- Getting started guide
- Usage examples
- Advanced features
- Troubleshooting
- Related resources

### Example Pages (2 pages)
Each example includes:
- Multi-source integration details
- API documentation
- Performance metrics
- Batch processing capabilities
- Export formats

### Education Page (1 page)
- Step-by-step tutorial
- Python basics
- Hands-on exercises
- Learning outcomes

---

## 📝 Wiki Page Naming Convention

GitHub Wiki uses the following naming:
- Spaces are replaced with hyphens: `Plant Card` → `Plant-Card`
- File extensions are optional: `Home.md` → `Home`
- Links use the page name: `[Home](Home)` or `[Template](TEMPLATE-MyST-Scientific)`

---

## 🔗 Internal Links

All wiki pages use consistent internal linking:
```markdown
[Home](Home)
[MyST Template](TEMPLATE-MyST-Scientific)
[Plant Card Generator](Examples-Plant-Card-Generator)
[Tutorial](Education-Tutorial)
```

---

## 🎨 Wiki Features Used

### Badges
- Colab badges for direct notebook access
- Status badges (Production Ready, Beta, etc.)

### Formatting
- Headers (H1-H6)
- Tables for comparisons
- Code blocks with syntax highlighting
- Lists (ordered and unordered)
- Blockquotes for important notes
- Emojis for visual organization

### Navigation
- Table of contents on each page
- "Back to" links at bottom
- Category organization
- Cross-references between pages

---

## 📈 Statistics

| Category | Notebooks | Wiki Pages | Total Lines |
|----------|-----------|------------|-------------|
| Templates | 6 | 6 | ~2,400 |
| Examples | 2 | 2 | ~950 |
| Education | 1 | 1 | ~400 |
| **Total** | **9** | **9** + Home | **~3,900** |

---

## ✨ Next Steps

### Immediate
1. ✅ Push all wiki pages to GitHub
2. ✅ Verify links work correctly
3. ✅ Check formatting on GitHub

### Future Enhancements
- 📸 Add screenshots to wiki pages
- 🎥 Add video tutorials
- 📊 Add more example outputs
- 🌍 Translate popular pages
- 📱 Optimize for mobile viewing

### Remaining Notebooks (Need Wiki Pages)
These notebooks still need comprehensive wiki pages created:
- Agrology-Data-Analysis-Exploration
- Agrology-Environmental-Management
- Agrology-Fertilizer-Calculations
- Greenhouse-ML-Yield-Prediction
- Greenhouse-Data-Visualization
- Greenhouse-Lighting-Setup-Analyzer
- Regional-Finnish-Weather-Analysis

**Note:** These can be created using similar structure to existing pages.

---

## 🤝 Contributing to Wiki

Want to improve the wiki?

1. **Fix typos or improve clarity**
   - Clone wiki repo
   - Make changes
   - Submit pull request

2. **Add screenshots**
   - Upload images to wiki repo
   - Reference in markdown: `![Alt text](image.png)`

3. **Translate pages**
   - Create language-specific pages
   - Use suffix: `Home-FI.md`, `Home-SV.md`

4. **Add examples**
   - Show real use cases
   - Include code snippets
   - Share results

---

## 📚 Wiki Resources

- [GitHub Wiki Documentation](https://docs.github.com/en/communities/documenting-your-project-with-wikis)
- [Markdown Guide](https://www.markdownguide.org)
- [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet)

---

## 🎉 Success!

Your Botanical Colabs wiki is ready to help users discover and use your notebooks effectively!

**View your wiki:** https://github.com/outobecca/botanical-colabs/wiki

---

Created: 2025-11-05  
Status: ✅ Ready to Deploy
