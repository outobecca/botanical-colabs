# 🔬 MyST Scientific Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_myst_scientific.ipynb)

> **Advanced scientific notebook template with MyST markdown for publication-quality documentation**

---

## 📋 Overview

The MyST Scientific Template is a professional-grade notebook template that combines:
- **MyST Markdown** — Advanced scientific documentation features
- **Auto-Reload** — Efficient development workflow
- **Code Modularization** — %%writefile for organized code
- **Interactive Widgets** — User-friendly configuration
- **Type Hints** — Professional code quality
- **Citations** — Scientific bibliography support

Perfect for **research papers**, **scientific reports**, and **technical documentation**.

---

## 🎯 Use Cases

### Research & Academia
- ✅ Scientific research papers
- ✅ Technical reports
- ✅ Thesis chapters
- ✅ Lab notebooks
- ✅ Experimental documentation

### Professional
- ✅ Data analysis reports
- ✅ Technical documentation
- ✅ Project documentation
- ✅ Knowledge bases
- ✅ API documentation

### Publishing
- ✅ Jupyter Book chapters
- ✅ Online documentation
- ✅ PDF export
- ✅ Academic publishing
- ✅ Blog posts

---

## ⭐ Key Features

### MyST Markdown Extensions

#### Admonitions
Create professional callout boxes:

```markdown
:::{note}
This is a note for general information
:::

:::{warning}
This is a warning for important cautions
:::

:::{tip}
This is a tip for helpful suggestions
:::

:::{important}
This is for critical information
:::
```

#### Cross-References
Link sections within and across documents:

```markdown
(my-label)=
## Section Title

Reference it later: See [](my-label) for details
```

#### Math Equations
Beautiful LaTeX math rendering:

```markdown
Inline: $E = mc^2$

Display: $$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$$
```

#### Grids & Cards
Responsive layouts:

```markdown
::::{grid} 1 1 2 2
:::{grid-item-card} Card 1
Content here
:::
:::{grid-item-card} Card 2
More content
:::
::::
```

#### Dropdowns
Collapsible content:

```markdown
:::{dropdown} Click to expand
Hidden content revealed on click
:::
```

### Auto-Reload Magic

Enable efficient development:

```python
%load_ext autoreload
%autoreload 2
```

**Benefits:**
- Edit .py files and see changes immediately
- No kernel restart needed
- Cleaner notebooks with modular code

### %%writefile Magic

Organize code in separate files:

```python
%%writefile utils/helpers.py
def my_function():
    """Documented function"""
    return "Hello!"
```

**Benefits:**
- Better code organization
- Easier testing
- Version control friendly
- Reusable across notebooks

### Interactive Widgets

Professional UI configuration:

- Text inputs with validation
- Dropdowns for options
- Checkboxes for settings
- Buttons for actions
- Status outputs

### Type Hints & Docstrings

Professional code quality:

```python
def process_data(
    name: str, 
    count: int = 10
) -> Dict[str, Any]:
    """
    Process botanical data.
    
    Args:
        name: Species name
        count: Number of records
    
    Returns:
        Dictionary with results
    """
    ...
```

---

## 📦 What's Included

### Cell Structure

1. **Frontmatter** — MyST configuration, metadata
2. **Introduction** — Overview with cards and grids
3. **Auto-Reload Setup** — Development workflow
4. **Library Installation** — All dependencies
5. **Configuration UI** — Interactive widgets
6. **Helper Functions** — Utility functions
7. **%%writefile Example** — Code modularization
8. **Data Fetching** — API integration examples
9. **Analysis** — Main workflow
10. **Results** — Visualization and display
11. **Citations** — Scientific references
12. **Best Practices** — Documentation

### Example Functions

- `safe_api_call()` — Error-handled API requests
- `validate_species_name()` — Input validation
- `format_scientific_name()` — HTML formatting
- `fetch_gbif_data()` — GBIF integration
- `fetch_wikipedia_summary()` — Multi-language support
- `generate_citation()` — Bibliography creation

---

## 🚀 Getting Started

### 1. Open in Colab
Click the "Open in Colab" badge above

### 2. Run Auto-Reload Cell
Execute the first code cell to enable auto-reload

### 3. Install Libraries
Run the installation cell (already included)

### 4. Configure Settings
Use the interactive UI to set:
- Species name
- Language preference
- Output options
- API keys (via Colab Secrets)

### 5. Execute Analysis
Run cells sequentially to see results

### 6. Customize
Adapt template to your specific needs

---

## 📖 MyST Syntax Quick Reference

### Headers with Labels
```markdown
(section-label)=
## My Section

Reference: See [](section-label)
```

### Tables
```markdown
```{list-table} Table Title
:header-rows: 1

* - Column 1
  - Column 2
* - Data 1
  - Data 2
```
```

### Figures
```markdown
```{figure} image.png
:name: fig-label
:width: 500px

Caption text
```

Reference: {numref}`fig-label`
```

### Code Blocks
```markdown
```{code-block} python
:linenos:
:emphasize-lines: 2,3

def hello():
    print("Hello")
    return True
```
```

### Bibliography
```markdown
```{bibliography}
:style: plain
:filter: docname in docnames
```
```

---

## 🔧 Advanced Usage

### Building Jupyter Book

1. **Install Jupyter Book:**
   ```bash
   pip install jupyter-book
   ```

2. **Build documentation:**
   ```bash
   jupyter-book build .
   ```

3. **View output:**
   - Open `_build/html/index.html`

### Export to PDF

1. **Install dependencies:**
   ```bash
   pip install jupyter-book
   ```

2. **Build PDF:**
   ```bash
   jupyter-book build . --builder pdflatex
   ```

### Version Control

**Best practices:**
- Commit notebooks with cleared outputs
- Use `.gitignore` for `_build/` and `utils/__pycache__/`
- Track `.py` files separately from notebooks
- Use meaningful commit messages

---

## 💡 Tips & Best Practices

### Organization
- ✅ Use clear section headers with labels
- ✅ Add table of contents with MyST
- ✅ Group related functions in modules
- ✅ Keep notebooks focused on one topic

### Documentation
- ✅ Write comprehensive docstrings
- ✅ Use admonitions for context
- ✅ Add cross-references liberally
- ✅ Include citations for data sources

### Code Quality
- ✅ Enable auto-reload from start
- ✅ Use type hints for all functions
- ✅ Handle errors gracefully
- ✅ Validate user inputs

### Publishing
- ✅ Clear outputs before committing
- ✅ Test in clean environment
- ✅ Include usage examples
- ✅ Add copyright and license

---

## 📊 Comparison with Other Templates

| Feature | MyST Scientific | General Botanical | Data Analysis |
|---------|----------------|-------------------|---------------|
| MyST Markdown | ✅ Full support | ❌ No | ❌ No |
| Auto-Reload | ✅ Yes | ❌ No | ❌ No |
| %%writefile | ✅ Examples | ❌ No | ❌ No |
| Type Hints | ✅ All functions | ⚠️ Partial | ⚠️ Partial |
| Cross-References | ✅ Yes | ❌ No | ❌ No |
| Bibliography | ✅ BibTeX | ⚠️ Manual | ⚠️ Manual |
| Jupyter Book | ✅ Ready | ❌ No | ❌ No |
| **Best for** | Papers, docs | General use | Data work |

---

## 🔗 Related Resources

### Documentation
- [MyST Parser Docs](https://myst-parser.readthedocs.io)
- [Jupyter Book Guide](https://jupyterbook.org)
- [MyST & Marp Integration Guide](https://github.com/outobecca/botanical-colabs/blob/main/MYST_MARP_GUIDE.md)

### Examples
- [Jupyter Book Gallery](https://executablebooks.org/en/latest/gallery.html)
- [MyST Examples](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html)

### Tools
- [MyST Markdown Cheat Sheet](https://jupyterbook.org/reference/cheatsheet.html)
- [Sphinx Design Components](https://sphinx-design.readthedocs.io)

---

## 🐛 Troubleshooting

### Common Issues

**MyST syntax not rendering:**
- Ensure `myst-parser` is installed
- Check frontmatter configuration
- Verify `:::` fence syntax

**Auto-reload not working:**
- Run `%load_ext autoreload` first
- Check that `%autoreload 2` is executed
- Verify .py file paths

**Import errors:**
- Create `utils/` directory first
- Run %%writefile cells before importing
- Check Python path includes workspace

**Citations not showing:**
- Verify `references.bib` file exists
- Check BibTeX syntax
- Ensure `sphinxcontrib-bibtex` installed

---

## 📝 Example Output

The template produces:

### HTML (Jupyter Book)
- Professional website
- Navigation sidebar
- Search functionality
- Mobile responsive

### PDF
- Publication-quality typesetting
- Numbered equations and figures
- Cross-references as page numbers
- Bibliography

### Notebook
- Interactive widgets
- Live code execution
- Inline visualizations
- Error handling

---

## 🎓 Learning Resources

### Beginner
1. Start with [General Botanical Template](TEMPLATE-Botanical-Notebook)
2. Read [MyST Basics](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
3. Try simple admonitions and cross-references

### Intermediate
1. Learn %%writefile workflow
2. Practice auto-reload development
3. Build a simple Jupyter Book

### Advanced
1. Create custom Sphinx themes
2. Write Sphinx extensions
3. Publish to academic journals

---

## 📄 License

MIT License — Free to use, modify, and distribute

**Citation:**
```bibtex
@software{botanical_myst_template_2025,
  author = {Sihvonen, Pekka},
  title = {MyST Scientific Template - Botanical Colabs},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/outobecca/botanical-colabs}
}
```

---

## 🤝 Contributing

Found a bug or have a suggestion?

- 🐛 [Report Issue](https://github.com/outobecca/botanical-colabs/issues/new)
- 💬 [Start Discussion](https://github.com/outobecca/botanical-colabs/discussions)
- 🔀 [Submit Pull Request](https://github.com/outobecca/botanical-colabs/pulls)

---

**Created:** 2025-11-04  
**Version:** 2.0  
**Status:** ✅ Production Ready

[← Back to Templates](Home#-templates) | [View on GitHub](https://github.com/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_myst_scientific.ipynb)
