# 📸 Notebook Preview Generator

Generate static HTML previews of Jupyter notebooks for web demonstration.

## Quick Start

### Option 1: Simple Preview (Recommended)

Generates HTML previews without executing notebooks (shows structure and markdown only):

```bash
python generate_simple_previews.py
```

**Requirements:**
```bash
pip install jupyter nbconvert
```

**Output:**
- `previews/html/*.html` - HTML previews for each notebook
- `previews/index.html` - Gallery index page

### Option 2: Full Preview with Execution

Executes notebooks with dummy data and captures outputs:

```bash
pip install jupyter nbconvert nbformat
python generate_previews.py
```

**Output:**
- `previews/html/*.html` - HTML previews with outputs
- `previews/markdown/*.md` - Markdown exports
- `previews/index.html` - Gallery index page

## Manual Conversion

Convert a single notebook:

```bash
# HTML (no code cells)
jupyter nbconvert --to html --no-input notebook.ipynb

# HTML (with code)
jupyter nbconvert --to html notebook.ipynb

# Markdown
jupyter nbconvert --to markdown notebook.ipynb

# PDF (requires LaTeX)
jupyter nbconvert --to pdf notebook.ipynb
```

## Preview Options

### Hide Code Cells
```bash
jupyter nbconvert --to html --no-input notebook.ipynb
```

### Custom Template
```bash
jupyter nbconvert --to html --template classic notebook.ipynb
```

### Execute Before Converting
```bash
jupyter nbconvert --to html --execute notebook.ipynb
```

## Viewing Previews

After generation, open the index page:

```bash
# Windows
start previews/index.html

# macOS
open previews/index.html

# Linux
xdg-open previews/index.html
```

Or use a local server:

```bash
cd previews
python -m http.server 8080
# Visit: http://localhost:8080
```

## Directory Structure

```
previews/
├── index.html              # Gallery index
├── html/
│   ├── templates_TEMPLATE_botanical_notebook.html
│   ├── examples_generator-plant-card.html
│   └── ...
└── markdown/               # (if using full preview)
    ├── templates_TEMPLATE_botanical_notebook.md
    └── ...
```

## Customization

### Custom CSS

Edit `generate_simple_previews.py` and modify the `<style>` section in `create_preview_index()`.

### Template Selection

Available templates:
- `classic` - Traditional Jupyter style
- `lab` - JupyterLab style  
- `basic` - Minimal HTML

Change in script:
```python
cmd = [
    "jupyter", "nbconvert",
    "--to", "html",
    "--template", "lab",  # Change here
    ...
]
```

## Troubleshooting

### "jupyter: command not found"

Install Jupyter:
```bash
pip install jupyter
```

### "Template not found"

Install nbconvert templates:
```bash
pip install --upgrade nbconvert
```

### Execution Errors

Use simple mode if notebooks fail to execute:
```bash
python generate_simple_previews.py
```

## Integration with Website

Add preview links to `index.html`:

```html
<a href="previews/html/examples_generator-plant-card.html" target="_blank">
    View Preview →
</a>
```

Or embed in iframe:

```html
<iframe src="previews/html/notebook.html" width="100%" height="600px"></iframe>
```

## Automated Generation

Add to GitHub Actions (`.github/workflows/previews.yml`):

```yaml
name: Generate Previews

on:
  push:
    paths:
      - 'notebooks/**/*.ipynb'

jobs:
  previews:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install jupyter nbconvert
      - run: python generate_simple_previews.py
      - uses: actions/upload-artifact@v3
        with:
          name: notebook-previews
          path: previews/
```

## Notes

- Previews are static snapshots - they don't reflect live edits
- Code cells are hidden by default (use `--no-input` flag)
- Large notebooks may take time to convert
- Previews don't require Python/Jupyter to view

## License

Same as main repository (MIT)
