#!/usr/bin/env python3
"""
Generate web preview snapshots from Jupyter notebooks.
Executes notebooks with dummy data and captures markdown renderings.
"""

import os
import json
import nbformat
from nbconvert import HTMLExporter, MarkdownExporter
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError
from pathlib import Path
import shutil

# Configuration
NOTEBOOKS_DIR = Path("notebooks")
PREVIEWS_DIR = Path("previews")
TIMEOUT = 600  # 10 minutes per notebook
KERNEL_NAME = "python3"

# Dummy data for common plant species
DUMMY_SPECIES = [
    "Rosa canina",
    "Taraxacum officinale",
    "Plantago major",
    "Bellis perennis",
    "Trifolium repens"
]

def setup_preview_directories():
    """Create preview directories if they don't exist."""
    PREVIEWS_DIR.mkdir(exist_ok=True)
    (PREVIEWS_DIR / "html").mkdir(exist_ok=True)
    (PREVIEWS_DIR / "markdown").mkdir(exist_ok=True)
    (PREVIEWS_DIR / "thumbnails").mkdir(exist_ok=True)

def inject_dummy_data(notebook):
    """Inject dummy data into notebook cells to enable execution."""
    # Add a cell at the beginning with dummy inputs
    dummy_cell = nbformat.v4.new_code_cell("""
# AUTO-INJECTED DUMMY DATA FOR PREVIEW GENERATION
import os
os.environ['PREVIEW_MODE'] = 'true'

# Dummy species list
DUMMY_SPECIES = ['Rosa canina', 'Taraxacum officinale', 'Plantago major']

# Mock API keys (won't actually call APIs in preview mode)
os.environ['GBIF_API_KEY'] = 'dummy_key_for_preview'
os.environ['TREFLE_API_KEY'] = 'dummy_key_for_preview'
os.environ['GOOGLE_API_KEY'] = 'dummy_key_for_preview'

# Skip API calls and use dummy data
USE_DUMMY_DATA = True
PREVIEW_MODE = True

print("✓ Preview mode enabled with dummy data")
""")
    
    # Insert at position 1 (after any title cells)
    notebook.cells.insert(1, dummy_cell)
    return notebook

def modify_notebook_for_preview(nb_path):
    """Modify notebook to use dummy data instead of real API calls."""
    with open(nb_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Inject dummy data
    notebook = inject_dummy_data(notebook)
    
    # Modify cells to skip API calls
    for cell in notebook.cells:
        if cell.cell_type == 'code':
            source = cell.source
            
            # Skip cells with API calls
            if any(keyword in source for keyword in ['requests.get', 'API', 'fetch']):
                # Add condition to use dummy data
                cell.source = f"""
if 'PREVIEW_MODE' in os.environ:
    # Using dummy data for preview
    pass
else:
{chr(10).join('    ' + line for line in source.split(chr(10)))}
"""
    
    return notebook

def execute_notebook(nb_path, output_path=None):
    """Execute a notebook and optionally save the result."""
    try:
        print(f"  Executing: {nb_path.name}")
        
        with open(nb_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        
        # Modify for preview
        notebook = modify_notebook_for_preview(nb_path)
        
        # Execute with preprocessor
        ep = ExecutePreprocessor(
            timeout=TIMEOUT,
            kernel_name=KERNEL_NAME,
            allow_errors=True  # Continue on errors for preview
        )
        
        try:
            ep.preprocess(notebook, {'metadata': {'path': nb_path.parent}})
        except CellExecutionError as e:
            print(f"    ⚠️  Warning: Some cells failed to execute: {str(e)[:100]}")
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                nbformat.write(notebook, f)
        
        return notebook
    
    except Exception as e:
        print(f"    ❌ Error executing {nb_path.name}: {str(e)[:100]}")
        return None

def generate_html_preview(notebook, output_path):
    """Generate HTML preview from executed notebook."""
    try:
        html_exporter = HTMLExporter()
        html_exporter.template_name = 'classic'
        
        (body, resources) = html_exporter.from_notebook_node(notebook)
        
        # Add custom CSS for better preview
        custom_css = """
        <style>
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #ffffff;
        }
        .preview-badge {
            background: #fef3c7;
            border: 2px solid #fbbf24;
            border-radius: 8px;
            padding: 10px 15px;
            margin: 20px 0;
            font-weight: 600;
            color: #92400e;
        }
        </style>
        """
        
        # Add preview notice
        preview_notice = """
        <div class="preview-badge">
            📸 Preview Mode - This is a static snapshot generated with dummy data for demonstration purposes.
        </div>
        """
        
        body = body.replace('<body>', f'<body>{custom_css}{preview_notice}')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(body)
        
        print(f"    ✓ HTML preview saved: {output_path.name}")
        return True
    
    except Exception as e:
        print(f"    ❌ Error generating HTML: {str(e)[:100]}")
        return False

def generate_markdown_preview(notebook, output_path):
    """Generate Markdown preview from executed notebook."""
    try:
        md_exporter = MarkdownExporter()
        (body, resources) = md_exporter.from_notebook_node(notebook)
        
        # Add preview notice
        preview_notice = """
---
**📸 Preview Mode**  
This is a static snapshot generated with dummy data for demonstration purposes.

---

"""
        body = preview_notice + body
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(body)
        
        print(f"    ✓ Markdown preview saved: {output_path.name}")
        return True
    
    except Exception as e:
        print(f"    ❌ Error generating Markdown: {str(e)[:100]}")
        return False

def create_preview_index():
    """Create an index.html page listing all previews."""
    html_previews = list((PREVIEWS_DIR / "html").glob("*.html"))
    
    preview_items = []
    for preview_path in sorted(html_previews):
        name = preview_path.stem
        category = name.split('_')[0] if '_' in name else 'other'
        preview_items.append({
            'name': name,
            'category': category,
            'path': f'html/{preview_path.name}'
        })
    
    # Group by category
    categories = {}
    for item in preview_items:
        cat = item['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item)
    
    # Generate HTML
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notebook Previews - Botanical Colabs</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #f6f8fa;
        }
        h1 {
            color: #24292f;
            border-bottom: 2px solid #d0d7de;
            padding-bottom: 10px;
        }
        .category {
            margin: 40px 0;
        }
        .category h2 {
            color: #0969da;
            text-transform: capitalize;
        }
        .preview-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .preview-card {
            background: white;
            border: 1px solid #d0d7de;
            border-radius: 8px;
            padding: 20px;
            transition: all 0.2s;
        }
        .preview-card:hover {
            border-color: #0969da;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }
        .preview-card a {
            color: #24292f;
            text-decoration: none;
            font-weight: 600;
            display: block;
        }
        .preview-card a:hover {
            color: #0969da;
        }
        .badge {
            display: inline-block;
            background: #ddf4ff;
            color: #0969da;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 12px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>📓 Notebook Previews</h1>
    <p>Static snapshots of executed notebooks with dummy data for demonstration purposes.</p>
"""
    
    for category, items in sorted(categories.items()):
        html += f"""
    <div class="category">
        <h2>{category.replace('_', ' ').title()}</h2>
        <div class="preview-grid">
"""
        for item in items:
            display_name = item['name'].replace('_', ' ').replace('-', ' ').title()
            html += f"""
            <div class="preview-card">
                <a href="{item['path']}">{display_name}</a>
                <span class="badge">Preview</span>
            </div>
"""
        html += """
        </div>
    </div>
"""
    
    html += """
</body>
</html>
"""
    
    with open(PREVIEWS_DIR / "index.html", 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"\n✓ Preview index created: previews/index.html")

def process_notebook(nb_path):
    """Process a single notebook and generate previews."""
    print(f"\n📓 Processing: {nb_path.relative_to(NOTEBOOKS_DIR)}")
    
    # Create output filename
    relative_path = nb_path.relative_to(NOTEBOOKS_DIR)
    output_name = str(relative_path).replace('/', '_').replace('\\', '_').replace('.ipynb', '')
    
    # Execute notebook
    executed_nb = execute_notebook(nb_path)
    
    if executed_nb is None:
        print(f"    ⏭️  Skipping preview generation (execution failed)")
        return False
    
    # Generate HTML preview
    html_path = PREVIEWS_DIR / "html" / f"{output_name}.html"
    generate_html_preview(executed_nb, html_path)
    
    # Generate Markdown preview
    md_path = PREVIEWS_DIR / "markdown" / f"{output_name}.md"
    generate_markdown_preview(executed_nb, md_path)
    
    return True

def main():
    """Main execution function."""
    print("🎨 Notebook Preview Generator")
    print("=" * 50)
    
    # Setup directories
    setup_preview_directories()
    
    # Find all notebooks
    notebooks = list(NOTEBOOKS_DIR.rglob("*.ipynb"))
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    print(f"\nFound {len(notebooks)} notebooks to process\n")
    
    # Process each notebook
    success_count = 0
    for nb_path in notebooks:
        if process_notebook(nb_path):
            success_count += 1
    
    # Create index page
    create_preview_index()
    
    print("\n" + "=" * 50)
    print(f"✓ Preview generation complete!")
    print(f"  Processed: {success_count}/{len(notebooks)} notebooks")
    print(f"  Output directory: {PREVIEWS_DIR.absolute()}")
    print(f"  View previews: {(PREVIEWS_DIR / 'index.html').absolute()}")

if __name__ == "__main__":
    main()
