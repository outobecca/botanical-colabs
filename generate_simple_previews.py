#!/usr/bin/env python3
"""
Simple notebook to HTML converter for preview generation.
Uses nbconvert command-line tool to generate static previews.
"""

import subprocess
import os
from pathlib import Path
import json

NOTEBOOKS_DIR = Path("notebooks")
PREVIEWS_DIR = Path("previews")

def setup_directories():
    """Create preview directories."""
    PREVIEWS_DIR.mkdir(exist_ok=True)
    (PREVIEWS_DIR / "html").mkdir(exist_ok=True)
    print(f"✓ Created preview directories in: {PREVIEWS_DIR.absolute()}")

def convert_notebook_to_html(nb_path, output_path):
    """Convert a notebook to HTML using nbconvert."""
    try:
        cmd = [
            "jupyter", "nbconvert",
            "--to", "html",
            "--output", str(output_path.absolute()),
            "--template", "classic",
            "--no-input",  # Hide code cells, show only outputs
            str(nb_path.absolute())
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"  ✓ {nb_path.name} → {output_path.name}")
            return True
        else:
            print(f"  ❌ Failed: {nb_path.name}")
            print(f"     {result.stderr[:100]}")
            return False
    
    except FileNotFoundError:
        print("❌ Error: jupyter not found. Install with: pip install jupyter nbconvert")
        return False
    except Exception as e:
        print(f"  ❌ Error converting {nb_path.name}: {str(e)[:100]}")
        return False

def create_preview_index(processed_files):
    """Create index.html listing all previews."""
    
    # Group by category
    categories = {}
    for nb_path, html_path in processed_files:
        parts = nb_path.relative_to(NOTEBOOKS_DIR).parts
        category = parts[0] if len(parts) > 1 else 'root'
        
        if category not in categories:
            categories[category] = []
        
        categories[category].append({
            'name': nb_path.stem,
            'path': html_path.relative_to(PREVIEWS_DIR)
        })
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notebook Previews - Botanical Colabs</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #f6f8fa;
            color: #24292f;
        }
        h1 {
            color: #24292f;
            border-bottom: 3px solid #0969da;
            padding-bottom: 15px;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #57606a;
            margin-bottom: 40px;
        }
        .category {
            margin: 50px 0;
        }
        .category h2 {
            color: #0969da;
            text-transform: capitalize;
            border-left: 4px solid #0969da;
            padding-left: 15px;
            margin-bottom: 20px;
        }
        .preview-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 20px;
        }
        .preview-card {
            background: white;
            border: 1px solid #d0d7de;
            border-radius: 8px;
            padding: 24px;
            transition: all 0.3s ease;
            text-decoration: none;
            display: block;
        }
        .preview-card:hover {
            border-color: #0969da;
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
            transform: translateY(-4px);
        }
        .preview-title {
            color: #24292f;
            font-weight: 600;
            font-size: 16px;
            margin-bottom: 8px;
        }
        .preview-card:hover .preview-title {
            color: #0969da;
        }
        .badge {
            display: inline-block;
            background: #ddf4ff;
            color: #0969da;
            padding: 4px 12px;
            border-radius: 16px;
            font-size: 12px;
            font-weight: 600;
        }
        .icon {
            font-size: 32px;
            margin-bottom: 12px;
        }
        .notice {
            background: #fff8c5;
            border: 2px solid #fbbf24;
            border-radius: 8px;
            padding: 16px 20px;
            margin-bottom: 40px;
        }
        .notice strong {
            color: #92400e;
        }
    </style>
</head>
<body>
    <h1>📓 Notebook Preview Gallery</h1>
    <p class="subtitle">Static snapshots of Jupyter notebooks from the Botanical Colabs collection</p>
    
    <div class="notice">
        <strong>ℹ️ Note:</strong> These are static HTML exports showing notebook structure and markdown content. 
        Code cells are hidden to focus on documentation and output visualization.
    </div>
"""
    
    for category, items in sorted(categories.items()):
        category_icons = {
            'templates': '📐',
            'examples': '📋',
            'agrology': '🌾',
            'greenhouse': '🏗️',
            'regional': '🗺️',
            'education': '🎓'
        }
        icon = category_icons.get(category, '📓')
        
        html += f"""
    <div class="category">
        <h2>{icon} {category.replace('_', ' ').title()}</h2>
        <div class="preview-grid">
"""
        for item in sorted(items, key=lambda x: x['name']):
            display_name = item['name'].replace('_', ' ').replace('-', ' ').title()
            html += f"""
            <a href="{item['path']}" class="preview-card">
                <div class="icon">📄</div>
                <div class="preview-title">{display_name}</div>
                <span class="badge">Preview</span>
            </a>
"""
        html += """
        </div>
    </div>
"""
    
    html += f"""
    <hr style="margin: 60px 0; border: none; border-top: 1px solid #d0d7de;">
    <p style="text-align: center; color: #57606a;">
        Generated {len(processed_files)} preview(s) | 
        <a href="https://github.com/outobecca/botanical-colabs" style="color: #0969da;">View Repository</a>
    </p>
</body>
</html>
"""
    
    index_path = PREVIEWS_DIR / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"\n✓ Created preview index: {index_path.absolute()}")

def main():
    print("🎨 Notebook Preview Generator (Simple Mode)")
    print("=" * 60)
    
    # Setup
    setup_directories()
    
    # Find notebooks
    notebooks = list(NOTEBOOKS_DIR.rglob("*.ipynb"))
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    print(f"\nFound {len(notebooks)} notebooks\n")
    
    # Convert each
    processed = []
    for nb_path in sorted(notebooks):
        relative_path = nb_path.relative_to(NOTEBOOKS_DIR)
        output_name = str(relative_path).replace(os.sep, '_').replace('.ipynb', '.html')
        output_path = PREVIEWS_DIR / "html" / output_name
        
        if convert_notebook_to_html(nb_path, output_path):
            processed.append((nb_path, output_path))
    
    # Create index
    if processed:
        create_preview_index(processed)
    
    print("\n" + "=" * 60)
    print(f"✓ Complete! Processed {len(processed)}/{len(notebooks)} notebooks")
    print(f"📂 Preview directory: {PREVIEWS_DIR.absolute()}")
    print(f"🌐 Open: file:///{(PREVIEWS_DIR / 'index.html').absolute()}")

if __name__ == "__main__":
    main()
