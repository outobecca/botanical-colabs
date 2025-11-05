# 📐 Templates Notebooks

Professional notebook templates for different scientific workflows — now with **MyST** and **Marp** support!

## 🌟 What's New: Enhanced Features

All templates now include best practices from the article ["Top 3 Jupyter Extensions to Make it Perfect IDE"](https://medium.com/@koypish/top-3-jupyter-extensions-to-make-it-perfect-ide-48e0f39d549):

- ✅ **Auto-reload** — Edit .py files and see changes immediately
- ✅ **%%writefile** — Modularize code into separate files
- ✅ **MyST markdown** — Advanced scientific documentation
- ✅ **Marp presentations** — Convert notebooks to slides
- ✅ **VS Code integration** — Optimal IDE experience

## 📚 Included Templates

### 🔬 MyST Scientific Template ⭐ NEW!
- **File:** `TEMPLATE_myst_scientific.ipynb`
- **Features:** 
  - MyST markdown with admonitions, cross-references, and directives
  - Auto-reload for efficient development
  - %%writefile for code modularization
  - Scientific citations and bibliography
  - Interactive widgets with type hints
  - Cross-platform compatibility (Colab + local)
- **Use for:** Research papers, scientific reports, documentation
- **Open in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_myst_scientific.ipynb)

### 🎤 Marp Presentation Template ⭐ NEW!
- **File:** `TEMPLATE_marp_presentation.ipynb`
- **Features:**
  - Marp markdown for beautiful slides
  - Export to HTML, PDF, or PowerPoint
  - Live demo code cells
  - Professional visualizations
  - Speaker notes and presenter mode
  - Customizable themes
- **Use for:** Conference presentations, teaching, demos
- **Open in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_marp_presentation.ipynb)

### 🌿 Template Botanical Notebook
- **File:** `TEMPLATE_botanical_notebook.ipynb`
- **Features:** General-purpose botanical research template
- **Open in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_botanical_notebook.ipynb)

### 📊 Template Data Analysis
- **File:** `TEMPLATE_data_analysis.ipynb`
- **Features:** Statistical analysis and data exploration
- **Open in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_data_analysis.ipynb)

### 🤖 Template Machine Learning
- **File:** `TEMPLATE_machine_learning.ipynb`
- **Features:** ML model development and evaluation
- **Open in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_machine_learning.ipynb)

### 🌍 Template Environmental Monitoring
- **File:** `TEMPLATE_environmental_monitoring.ipynb`
- **Features:** Environmental data analysis and sustainability metrics
- **Open in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_environmental_monitoring.ipynb)

---

## 🚀 Getting Started

### Quick Start (Recommended)
1. Click "Open in Colab" on any template above
2. Run the auto-reload cell first
3. Configure your settings using interactive widgets
4. Start analyzing!

### Local Development in VS Code
1. Clone repository: `git clone https://github.com/outobecca/botanical-colabs`
2. Open in VS Code with Jupyter extension
3. Select Python kernel
4. Enjoy full IDE features: auto-complete, debugging, Git integration

## 📖 Using MyST Features

MyST (Markedly Structured Text) extends Markdown with scientific publishing features:

### Admonitions
```markdown
:::{note}
This is a note admonition
:::

:::{warning}
This is a warning
:::

:::{tip}
Pro tip goes here!
:::
```

### Cross-References
```markdown
(my-section-label)=
## My Section

See [](my-section-label) for details.
```

### Math
```markdown
Inline: $E = mc^2$

Block:
$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$
```

### Grids & Cards
```markdown
::::{grid} 1 1 2 2
:::{grid-item-card} Card 1
Content here
:::
:::{grid-item-card} Card 2
Content here
:::
::::
```

## 🎨 Creating Presentations with Marp

Marp converts Markdown to beautiful slide decks:

### Export Options
```bash
# Install Marp CLI
npm install -g @marp-team/marp-cli

# Export to HTML
marp notebook.md -o slides.html

# Export to PDF
marp notebook.md --pdf -o slides.pdf

# Export to PowerPoint
marp notebook.md --pptx -o slides.pptx
```

### Slide Syntax
```markdown
---
marp: true
theme: default
---

# Title Slide

Content goes here

---

# Next Slide

More content
```

## ⚡ Best Practices (from Article)

### 1. Auto-Reload Magic
Always start notebooks with:
```python
%load_ext autoreload
%autoreload 2
```

**Benefits:**
- Edit Python files and see changes immediately
- No kernel restart needed
- Cleaner notebooks with modular code
- Better version control

### 2. %%writefile Magic
Modularize your code:
```python
%%writefile utils/helpers.py
def my_function():
    return "Hello!"
```

**Benefits:**
- Organize code in separate files
- Easy to test and reuse
- Import with auto-reload
- Better code organization

### 3. VS Code Integration
Work in VS Code instead of Jupyter browser:
- ✅ Better keyboard shortcuts
- ✅ Code navigation (Cmd/Ctrl+Click)
- ✅ Integrated Git
- ✅ Outline view auto-generated
- ✅ Same formatters and linters
- ✅ No browser tabs clutter

## 🔧 Installation

### Required Packages
```bash
# Core packages (already in requirements.txt)
pip install requests pandas numpy matplotlib seaborn ipywidgets

# MyST packages
pip install myst-parser myst-nb jupytext sphinx-design

# Jupyter Book (for building docs)
pip install jupyter-book

# Marp (for presentations)
npm install -g @marp-team/marp-cli
```

### VS Code Extensions
- **Jupyter** — Microsoft's official Jupyter extension
- **Marp for VS Code** — Preview and export Marp slides
- **MyST Markdown** — Syntax highlighting for MyST

## 📚 Additional Resources

- 📖 [MyST Parser Documentation](https://myst-parser.readthedocs.io)
- 📕 [Jupyter Book Guide](https://jupyterbook.org)
- 🎨 [Marp Documentation](https://marp.app)
- 🛠️ [Jupyter Extensions Article](https://medium.com/@koypish/top-3-jupyter-extensions-to-make-it-perfect-ide-48e0f39d549)
- 🔗 [Repository](https://github.com/outobecca/botanical-colabs)

## 💡 Template Selection Guide

| Your Goal | Recommended Template |
|-----------|---------------------|
| Research paper / Scientific report | 🔬 MyST Scientific |
| Conference presentation | 🎤 Marp Presentation |
| General botanical analysis | 🌿 Botanical Notebook |
| Statistical analysis | 📊 Data Analysis |
| Machine learning project | 🤖 ML Template |
| Environmental assessment | 🌍 Environmental Monitoring |

## 🤝 Contributing

To add notebooks to this category, ensure they:
- Include auto-reload setup
- Use MyST markdown where appropriate
- Follow best practices from the article
- Have comprehensive documentation
- Include type hints and docstrings

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for detailed guidelines.

---

**Updated:** 2025-11-04 | **Version:** 2.0 with MyST & Marp support
