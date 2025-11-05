# 📖 MyST and Marp Integration Guide

## Overview

This guide explains how to use MyST (Markedly Structured Text) and Marp presentation features in the Botanical Colabs notebooks, following best practices from the article ["Top 3 Jupyter Extensions to Make it Perfect IDE"](https://medium.com/@koypish/top-3-jupyter-extensions-to-make-it-perfect-ide-48e0f39d549).

## Table of Contents

1. [Auto-Reload Magic](#auto-reload-magic)
2. [%%writefile Magic](#writefile-magic)
3. [VS Code Integration](#vs-code-integration)
4. [MyST Markdown Features](#myst-markdown-features)
5. [Marp Presentations](#marp-presentations)
6. [Jupyter Book](#jupyter-book)
7. [Best Practices](#best-practices)

---

## 🔄 Auto-Reload Magic

### What is it?

Auto-reload automatically reloads imported Python modules whenever you execute a cell, eliminating the need to restart the kernel when you modify external `.py` files.

### Why use it?

- **Efficient development** — Edit code in separate files, changes apply immediately
- **Cleaner notebooks** — Move utility functions to `.py` files
- **Better organization** — Separate concerns between exploration (notebook) and code (modules)
- **Version control** — Easier to track changes in `.py` files than notebook cells

### How to use it?

**1. Enable at the start of your notebook:**
```python
# Load the autoreload extension
%load_ext autoreload

# Set to mode 2: reload all modules before executing code
%autoreload 2

print("✅ Auto-reload enabled!")
```

**2. Create utility files:**
```python
# Create directory structure
import os
os.makedirs('utils', exist_ok=True)
```

**3. Write your functions to files:**
```python
%%writefile utils/data_processing.py
def clean_species_name(name: str) -> str:
    """Standardizes species name format"""
    return name.strip().title()

def validate_coordinates(lat: float, lon: float) -> bool:
    """Validates geographic coordinates"""
    return -90 <= lat <= 90 and -180 <= lon <= 180
```

**4. Import and use:**
```python
from utils.data_processing import clean_species_name, validate_coordinates

# Now you can edit utils/data_processing.py
# Changes will apply on next cell execution!
result = clean_species_name("rosa canina")
print(result)  # "Rosa Canina"
```

### Auto-Reload Modes

- `%autoreload 0` — Disable auto-reload
- `%autoreload 1` — Reload modules imported with `%aimport`
- `%autoreload 2` — Reload all modules (recommended)

---

## 📝 %%writefile Magic

### What is it?

`%%writefile` is a cell magic command that writes the cell contents directly to a file on disk.

### Why use it?

- **Code organization** — Keep related functions in separate modules
- **Reusability** — Share code between notebooks
- **Testing** — Easier to unit test functions in `.py` files
- **Documentation** — Functions in files can have proper docstrings
- **Visibility** — Show code in notebook while saving to file

### Basic Usage

```python
%%writefile utils/api_helpers.py
"""
API helper functions for botanical data retrieval
"""

import requests
from typing import Optional, Dict, Any

def safe_api_call(url: str, params: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
    """
    Makes a safe API call with error handling.
    
    Args:
        url: API endpoint
        params: Query parameters
    
    Returns:
        JSON response or None on error
    """
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
```

### Advanced: Append Mode

```python
%%writefile -a utils/api_helpers.py
# This will APPEND to the existing file

def fetch_gbif_data(species: str) -> Optional[Dict]:
    """Fetches species data from GBIF"""
    url = "https://api.gbif.org/v1/species/search"
    return safe_api_call(url, {"q": species})
```

### Important Notes

⚠️ **Caveats:**
1. Cell only **writes** to file — doesn't execute in notebook context
2. Must **import** the function to use it in notebook
3. Include all necessary **imports** in the file
4. Re-running cell **overwrites** file (use `-a` flag to append)

✅ **Benefits:**
1. Code is **both visible** in notebook and **saved** to file
2. Combine with **auto-reload** for instant updates
3. Create **modular**, **reusable** code structure
4. Easier **version control** of utility functions

### Best Practice Workflow

```python
# Step 1: Write function to file
%%writefile utils/validators.py
def validate_species_name(name: str) -> bool:
    """Validates species name format"""
    return len(name) > 2 and ' ' in name

# Step 2: Import (auto-reload handles updates)
from utils.validators import validate_species_name

# Step 3: Use the function
is_valid = validate_species_name("Rosa canina")
print(f"Valid: {is_valid}")

# Step 4: Edit the %%writefile cell above and re-run
# Step 5: Re-run import cell — changes apply immediately!
```

---

## 💻 VS Code Integration

### Why use VS Code for Jupyter?

The article highlights these benefits over Jupyter browser interface:

1. **Unified environment** — All coding in one app, not browser tabs
2. **Better shortcuts** — Use your familiar VS Code shortcuts
3. **Code navigation** — Go to definition (Cmd/Ctrl+Click), find references
4. **Outline view** — Auto-generated table of contents from headers
5. **Git integration** — Stage, commit, diff directly in IDE
6. **Formatters** — Use Black, autopep8, etc.
7. **Debugging** — Set breakpoints, step through code
8. **Extensions** — Thousands of VS Code extensions available

### Setup

1. **Install VS Code**
   - Download from [code.visualstudio.com](https://code.visualstudio.com)

2. **Install Jupyter Extension**
   - Open VS Code
   - Go to Extensions (Ctrl/Cmd+Shift+X)
   - Search "Jupyter"
   - Install Microsoft's official extension

3. **Open Notebook**
   - File → Open → Select `.ipynb` file
   - Or drag-and-drop into VS Code

4. **Select Kernel**
   - Click "Select Kernel" in top-right
   - Choose your Python environment

### Important Settings

Add to `.vscode/settings.json`:

```json
{
  // Set notebook file root to workspace folder
  "jupyter.notebookFileRoot": "${workspaceFolder}",
  
  // This allows notebooks in subdirectories to import from project root
  // No more: from ..src.module import X
  
  // Auto-save
  "files.autoSave": "afterDelay",
  
  // Format on save
  "notebook.formatOnSave.enabled": true,
  
  // Show line numbers in cells
  "notebook.lineNumbers": "on"
}
```

### Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Run cell | Ctrl+Enter | Cmd+Enter |
| Run cell and advance | Shift+Enter | Shift+Enter |
| Insert cell below | Ctrl+Shift+Alt+Enter | Cmd+Shift+Option+Enter |
| Delete cell | DD (twice) | DD (twice) |
| Go to definition | Ctrl+Click | Cmd+Click |
| Find references | Shift+F12 | Shift+F12 |

### Outline View

VS Code automatically generates an outline from your markdown headers:

1. Open notebook in VS Code
2. Click "Outline" in Explorer sidebar
3. See table of contents with clickable links
4. Navigate large notebooks easily

**No need for table of contents extensions!**

---

## 📖 MyST Markdown Features

MyST (Markedly Structured Text) extends standard Markdown with powerful features for scientific writing.

### Admonitions

Create styled callout boxes:

```markdown
:::{note}
This is a note. Use for general information.
:::

:::{warning}
This is a warning. Use for important cautionary information.
:::

:::{tip}
This is a tip. Use for helpful suggestions.
:::

:::{important}
This is important. Use for critical information.
:::

:::{seealso}
This is a "see also". Use for cross-references.
:::

:::{attention}
This is attention. Use for things requiring focus.
:::
```

### Cross-References

Link to sections within and across notebooks:

```markdown
(my-section-label)=
## My Section Title

Some content here.

Later in the document:
See [](my-section-label) for details.

Or with custom text:
Check out [this section](my-section-label) for more info.
```

### Math Equations

```markdown
Inline math: $E = mc^2$

Display math:
$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$

Numbered equations:
```{math}
:label: euler
e^{i\pi} + 1 = 0
```

Reference equation: see Equation {eq}`euler`
```

### Grids and Cards

Create responsive grid layouts:

```markdown
::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Card Title 1
:class-header: bg-primary text-white

Card content goes here.
:::

:::{grid-item-card} Card Title 2
:class-header: bg-success text-white

More content here.
:::

::::
```

Parameters:
- `1 1 2 2` = columns at different breakpoints (mobile, tablet, desktop, wide)
- `:gutter:` = spacing between items

### Dropdowns

Create collapsible content:

```markdown
:::{dropdown} Click to expand
Hidden content goes here.

Can include:
- Lists
- Code blocks
- Images
- Anything else!
:::
```

### Tables

Advanced table features:

```markdown
```{list-table} My Table Title
:header-rows: 1
:name: my-table-label

* - Column 1
  - Column 2
  - Column 3
* - Row 1, Cell 1
  - Row 1, Cell 2
  - Row 1, Cell 3
* - Row 2, Cell 1
  - Row 2, Cell 2
  - Row 2, Cell 3
```

Reference: See [](my-table-label)
```

### Code Blocks with Options

```markdown
```{code-block} python
:linenos:
:emphasize-lines: 2,3
:caption: Example function

def hello(name):
    """Greet someone"""
    return f"Hello, {name}!"
```
```

### Figures

```markdown
```{figure} path/to/image.png
:name: my-figure
:alt: Alternative text
:width: 400px
:align: center

This is the figure caption.
```

Reference: See {numref}`my-figure`
```

### Substitutions

Define variables in frontmatter:

```markdown
---
myst:
  substitutions:
    version: "2.0"
    author: "Pekka"
---

Current version: {{ version }}
Created by: {{ author }}
```

---

## 🎨 Marp Presentations

Marp converts Markdown to beautiful presentations.

### Basic Slide Deck

Create a markdown cell with frontmatter:

```markdown
---
marp: true
theme: default
paginate: true
header: 'My Presentation'
footer: '© 2025'
---

# Title Slide

Your presentation starts here

---

# Second Slide

Content for second slide

- Bullet point 1
- Bullet point 2

---

# Third Slide with Image

![width:500px](image.jpg)

More content...
```

### Slide Breaks

- `---` creates a new slide
- Three hyphens on their own line
- Everything between `---` is one slide

### Themes

Built-in themes:
- `theme: default` — Clean, professional
- `theme: gaia` — Modern with gradients
- `theme: uncover` — Centered, minimalist

Custom theme:
```markdown
---
marp: true
theme: custom
style: |
  section {
    background-color: #2e7d32;
    color: white;
  }
  h1 {
    border-bottom: 2px solid white;
  }
---
```

### Slide Classes

Apply special formatting:

```markdown
<!-- _class: lead -->
# Big Centered Title

<!-- _class: invert -->
# Dark Background Slide

<!-- _class: lead invert -->
# Big Centered Dark Slide
```

### Background Images

```markdown
# Slide with Background

![bg](background.jpg)

---

# Split Background

![bg left:40%](image.jpg)

Content on the right side

---

# Transparent Background

![bg opacity:0.3](image.jpg)

Content over transparent image

---

# Fit Options

![bg fit](image.jpg)
![bg contain](image.jpg)
![bg cover](image.jpg)
```

### Exporting Slides

Install Marp CLI:
```bash
npm install -g @marp-team/marp-cli
```

Export to HTML:
```bash
marp presentation.md -o slides.html
```

Export to PDF:
```bash
marp presentation.md --pdf -o slides.pdf
```

Export to PowerPoint:
```bash
marp presentation.md --pptx -o slides.pptx
```

### VS Code Marp Extension

1. Install "Marp for VS Code" extension
2. Open `.md` file with Marp frontmatter
3. Preview: Ctrl/Cmd+Shift+V
4. Export: Command Palette → "Marp: Export slide deck"

---

## 📚 Jupyter Book

Build publication-quality documentation from your notebooks.

### Setup

Install Jupyter Book:
```bash
pip install jupyter-book
```

### Project Structure

```
botanical-colabs/
├── _config.yml          # Configuration
├── _toc.yml            # Table of contents
├── references.bib      # Bibliography
├── README.md           # Homepage
└── notebooks/
    ├── templates/
    ├── examples/
    └── ...
```

### Build Documentation

```bash
# Build HTML
jupyter-book build .

# Output: _build/html/index.html

# Clean previous builds
jupyter-book clean .
```

### Configuration (_config.yml)

See `_config.yml` in repository root for full configuration.

Key settings:
- MyST extensions enabled
- Repository integration
- Execution caching
- Theme customization

### Table of Contents (_toc.yml)

See `_toc.yml` for structure.

Defines:
- Chapter organization
- Navigation hierarchy
- Page ordering

### Publishing to GitHub Pages

```bash
# Install ghp-import
pip install ghp-import

# Build docs
jupyter-book build .

# Publish to gh-pages branch
ghp-import -n -p -f _build/html

# Site available at: https://username.github.io/repository
```

---

## ✅ Best Practices

### Notebook Organization

1. **Start with auto-reload**
   ```python
   %load_ext autoreload
   %autoreload 2
   ```

2. **Use %%writefile for utilities**
   - Create `utils/` directory
   - Write helper functions to `.py` files
   - Import and use with auto-reload

3. **Structure with MyST headers**
   - Use clear section headers
   - Add labels for cross-references
   - Create outline-friendly structure

4. **Add admonitions for context**
   - `:::{note}` for general info
   - `:::{warning}` for caveats
   - `:::{tip}` for best practices

### Code Quality

1. **Type hints**
   ```python
   def process_species(name: str, count: int) -> Dict[str, Any]:
       ...
   ```

2. **Docstrings**
   ```python
   def validate_data(data: pd.DataFrame) -> bool:
       """
       Validates data quality.
       
       Args:
           data: DataFrame to validate
       
       Returns:
           True if valid, False otherwise
       """
   ```

3. **Error handling**
   ```python
   try:
       result = api_call()
   except Exception as e:
       print(f"❌ Error: {e}")
       return None
   ```

### Workflow

1. **Explore in notebook**
   - Experiment with code
   - Visualize results
   - Document findings

2. **Refactor to modules**
   - Extract reusable functions
   - Write to `.py` files with %%writefile
   - Add tests

3. **Document with MyST**
   - Add clear explanations
   - Use cross-references
   - Include citations

4. **Share as presentation**
   - Convert key findings to Marp slides
   - Present to stakeholders
   - Export to PDF/PowerPoint

---

## 📚 Resources

### Documentation
- [MyST Parser](https://myst-parser.readthedocs.io)
- [Jupyter Book](https://jupyterbook.org)
- [Marp](https://marp.app)
- [IPython Magic Commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

### Articles
- [Top 3 Jupyter Extensions](https://medium.com/@koypish/top-3-jupyter-extensions-to-make-it-perfect-ide-48e0f39d549)

### Repository
- [Botanical Colabs](https://github.com/outobecca/botanical-colabs)

---

**Last Updated:** 2025-11-04  
**Version:** 2.0
