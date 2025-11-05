# 📚 Quick Reference: Auto-Documentation

> **TL;DR**: When you add or update notebooks in a PR, documentation is automatically generated!

## ✨ What You Get Automatically

Every notebook you add/update gets:

| Generated File | What It Contains | Where to Find |
|----------------|------------------|---------------|
| 📖 **Wiki Page** | Complete documentation with usage examples | `wiki/your-notebook.md` |
| 🖼️ **HTML Preview** | Rendered outputs without code | `previews/html/your_notebook.html` |
| 🎨 **Thumbnail** | Preview image | `thumbnails/your_notebook.png` |
| 💬 **PR Comment** | Links to all generated docs | Your PR |

## 🚀 How to Use

### For Contributors

1. **Create a branch**
   ```bash
   git checkout -b add-my-notebook
   ```

2. **Add your notebook**
   ```bash
   # Add to appropriate directory
   notebooks/agrology/my_analysis.ipynb
   ```

3. **Add metadata to your notebook** (optional but recommended)
   
   First markdown cell should include:
   ```markdown
   # My Analysis Title
   
   Description of what this notebook does and why it's useful.
   
   **Author:** Your Name
   **Tags:** data-analysis, plants, visualization
   ```

4. **Create PR**
   ```bash
   git add notebooks/agrology/my_analysis.ipynb
   git commit -m "feat: add soil analysis notebook"
   git push origin add-my-notebook
   ```

5. **Wait ~2 minutes** ⏱️
   - GitHub Actions runs automatically
   - Documentation is generated
   - Files are committed to your PR branch
   - Comment appears on your PR with links

6. **Review and merge** ✅
   - Check the wiki page looks good
   - Verify the preview renders correctly
   - Merge when satisfied!

### For Reviewers

When reviewing PRs with notebooks:

✅ **Check auto-generated docs** - Click links in the PR comment
✅ **Verify wiki page** - Is the documentation clear and complete?
✅ **Review preview** - Do outputs render correctly?
✅ **Validate metadata** - Is category detection correct?

## 📋 Best Practices

### 1. Add Good Metadata

**Do this** ✅:
```markdown
# Greenhouse Climate Analysis

This notebook analyzes greenhouse temperature and humidity data to optimize
plant growing conditions. It includes statistical analysis and visualizations.

**Author:** Rebecca Botanical
**Tags:** greenhouse, climate, data-analysis
```

**Not this** ❌:
```markdown
# Notebook

Some analysis
```

### 2. Organize by Category

Place notebooks in appropriate directories:

```
notebooks/
  ├── agrology/          # 🌾 Agricultural science
  ├── greenhouse/        # 🏗️ Greenhouse management
  ├── regional/          # 🗺️ Regional analysis
  ├── education/         # 🎓 Educational content
  ├── templates/         # 📐 Template notebooks
  └── examples/          # 📋 Example notebooks
```

### 3. Write Clean Notebooks

- Use markdown cells to explain code
- Add section headers
- Include outputs in cells
- Keep code cells focused

### 4. Test Locally First

Before pushing, verify your notebook:
```bash
jupyter notebook notebooks/your_notebook.ipynb
```

Run all cells to ensure:
- No errors
- Outputs are generated
- Visualizations display

## 🔧 Customization

### Change Your Notebook's Category

Edit your notebook path or add to directory:
```bash
# Will be categorized as "Agrology"
notebooks/agrology/my_analysis.ipynb

# Will be categorized as "Greenhouse"
notebooks/greenhouse/my_analysis.ipynb
```

### Customize Generated Docs

Want to customize wiki page generation?
1. Edit `.github/scripts/generate_documentation.py`
2. Modify the `generate_wiki_page()` function
3. Test locally before committing

## 🐛 Troubleshooting

### "No documentation generated"

**Cause**: Notebook didn't change or path doesn't match trigger

**Fix**:
- Ensure file ends with `.ipynb`
- Verify file is actually modified in PR
- Check workflow logs in Actions tab

### "Wiki page looks wrong"

**Cause**: Metadata not detected correctly

**Fix**:
- Add proper markdown headers in first cell
- Use `# Title` format for title
- Add `Author:` and `Tags:` fields

### "Preview is empty"

**Cause**: No outputs in notebook cells

**Fix**:
- Run all cells before committing
- Ensure cells produce output (prints, plots, etc.)
- Save notebook with outputs

### "Thumbnail is generic"

**Cause**: Auto-generated thumbnail is simple

**Fix**:
- This is expected! Thumbnails are simple by design
- They show notebook name and icon
- You can customize in the generator script

## 💡 Tips & Tricks

### 1. Preview Before Merging

After workflow runs:
```bash
# Checkout PR branch
git checkout pr-branch-name

# View generated files
open previews/html/your_notebook.html
open wiki/your-notebook.md
```

### 2. Batch Add Multiple Notebooks

The workflow handles multiple notebooks in one PR:
```bash
git add notebooks/*.ipynb
git commit -m "feat: add multiple analysis notebooks"
git push
```

Each gets its own wiki page, preview, and thumbnail!

### 3. Update Documentation

To regenerate docs for existing notebooks:
```bash
# Make a small change to notebook
# Commit and push
git add notebooks/existing.ipynb
git commit -m "docs: trigger documentation update"
git push
```

Workflow detects the change and regenerates all docs!

## 📊 Example Workflow

Here's a real example from start to finish:

```bash
# 1. Create feature branch
git checkout -b add-soil-analysis

# 2. Create notebook with good metadata
cat > notebooks/agrology/soil_ph_analysis.ipynb << 'EOF'
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Soil pH Analysis\n",
        "\n",
        "Analyze soil pH levels and their impact on plant growth.\n",
        "\n",
        "**Author:** Research Team\n",
        "**Tags:** soil, pH, agrology, data-analysis"
      ]
    }
  ]
}
EOF

# 3. Commit and push
git add notebooks/agrology/soil_ph_analysis.ipynb
git commit -m "feat: add soil pH analysis notebook"
git push origin add-soil-analysis

# 4. Create PR on GitHub
gh pr create --title "Add Soil pH Analysis" --body "New notebook for soil analysis"

# 5. Wait for workflow (~2 min)
# ⏱️ GitHub Actions runs
# 📝 Generates wiki/soil-ph-analysis.md
# 🖼️ Creates previews/html/soil_ph_analysis.html
# 🎨 Creates thumbnails/soil_ph_analysis.png
# 💬 Comments on PR with links

# 6. Review generated docs
gh pr view --web  # Click links in comment

# 7. Merge when satisfied
gh pr merge --squash
```

## 🎓 Learning More

- **Full Documentation**: [AUTO_DOCUMENTATION.md](./AUTO_DOCUMENTATION.md)
- **Preview Guide**: [PREVIEW_GENERATION.md](../PREVIEW_GENERATION.md)
- **Contributing**: [CONTRIBUTING.md](../CONTRIBUTING.md)
- **Workflow File**: [auto-documentation.yml](./auto-documentation.yml)
- **Generator Script**: [generate_documentation.py](../scripts/generate_documentation.py)

## ❓ FAQ

**Q: Do I need to do anything special?**  
A: No! Just add/update notebooks in a PR. Documentation is automatic.

**Q: Can I customize the generated docs?**  
A: Yes! Edit `.github/scripts/generate_documentation.py` or add better metadata to your notebooks.

**Q: What if I don't want auto-docs for a notebook?**  
A: You can skip it by not including `.ipynb` in the PR, or modify the workflow trigger paths.

**Q: How long does it take?**  
A: Usually 2-3 minutes for the workflow to complete.

**Q: Can I see the workflow run?**  
A: Yes! Go to **Actions** tab → **Auto-Generate Documentation** → Click the run.

**Q: Will old notebooks get docs?**  
A: Not automatically. But you can trigger it by making a small change and creating a PR.

---

**Happy documenting!** 📚✨

If you have questions, check the [full documentation](./AUTO_DOCUMENTATION.md) or [open an issue](https://github.com/outobecca/botanical-colabs/issues).
