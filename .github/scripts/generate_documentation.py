#!/usr/bin/env python3
"""
Auto-generate wiki pages and preview images for Jupyter notebooks.
Designed to run in GitHub Actions on pull requests.
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
import subprocess

try:
    import nbformat
    from nbconvert import HTMLExporter, MarkdownExporter
    from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError
    from PIL import Image, ImageDraw, ImageFont
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "jupyter", "nbconvert", "nbformat", "pillow"])
    import nbformat
    from nbconvert import HTMLExporter, MarkdownExporter
    from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError
    from PIL import Image, ImageDraw, ImageFont


# Category mapping based on directory structure
CATEGORY_MAPPING = {
    'templates': '📐 Templates',
    'examples': '📋 Examples',
    'agrology': '🌾 Agrology',
    'greenhouse': '🏗️ Greenhouse',
    'regional': '🗺️ Regional',
    'education': '🎓 Education',
    'other': '📓 Other Notebooks'
}


def setup_directories():
    """Create necessary directories for output."""
    dirs = [
        'wiki',
        'previews/html',
        'previews/markdown',
        'thumbnails'
    ]
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    print(f"✓ Created output directories")


def get_changed_notebooks():
    """Get list of changed notebook files from environment."""
    changed_file = os.environ.get('CHANGED_NOTEBOOKS_FILE', 'changed_notebooks.txt')
    
    if not Path(changed_file).exists():
        print(f"No changed notebooks file found: {changed_file}")
        return []
    
    with open(changed_file, 'r') as f:
        notebooks = [line.strip() for line in f if line.strip() and line.strip().endswith('.ipynb')]
    
    print(f"✓ Found {len(notebooks)} changed notebook(s)")
    return notebooks


def extract_notebook_metadata(notebook_path):
    """Extract metadata from notebook for wiki page generation."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Extract title from first markdown cell or filename
        title = Path(notebook_path).stem.replace('_', ' ').replace('-', ' ').title()
        description = ""
        author = "Botanical Research Team"
        tags = []
        
        # Try to extract from first few cells
        for cell in nb.cells[:5]:
            if cell.cell_type == 'markdown':
                lines = cell.source.split('\n')
                for line in lines:
                    # Look for title (# heading)
                    if line.startswith('# ') and not title:
                        title = line[2:].strip()
                    # Look for description
                    elif line and not line.startswith('#') and len(line) > 20:
                        if not description:
                            description = line.strip()
                    # Look for author
                    elif 'author:' in line.lower():
                        author = line.split(':', 1)[1].strip()
                    # Look for tags
                    elif 'tags:' in line.lower() or 'keywords:' in line.lower():
                        tags_str = line.split(':', 1)[1].strip()
                        tags = [t.strip() for t in tags_str.split(',')]
        
        # Infer tags from path
        path_parts = Path(notebook_path).parts
        for part in path_parts:
            if part in CATEGORY_MAPPING:
                tags.append(CATEGORY_MAPPING[part].split(' ', 1)[1])
        
        # Get cell count
        code_cells = len([c for c in nb.cells if c.cell_type == 'code'])
        markdown_cells = len([c for c in nb.cells if c.cell_type == 'markdown'])
        
        metadata = {
            'title': title,
            'description': description or f"Jupyter notebook for {title.lower()}",
            'author': author,
            'tags': list(set(tags)),
            'code_cells': code_cells,
            'markdown_cells': markdown_cells,
            'total_cells': len(nb.cells),
            'filename': Path(notebook_path).name,
            'path': notebook_path
        }
        
        return metadata
    
    except Exception as e:
        print(f"⚠ Error extracting metadata from {notebook_path}: {e}")
        return None


def generate_wiki_page(notebook_path, metadata):
    """Generate a comprehensive wiki page for the notebook."""
    wiki_name = Path(notebook_path).stem.replace('_', '-')
    wiki_path = f"wiki/{wiki_name}.md"
    
    # Determine category
    category = 'other'
    for cat in CATEGORY_MAPPING.keys():
        if cat in notebook_path.lower():
            category = cat
            break
    
    # Generate wiki content
    content = f"""# {metadata['title']}

> {metadata['description']}

## 📊 Overview

**Category:** {CATEGORY_MAPPING[category]}  
**Author:** {metadata['author']}  
**Cells:** {metadata['total_cells']} ({metadata['code_cells']} code, {metadata['markdown_cells']} markdown)  
**File:** `{metadata['filename']}`

"""
    
    if metadata['tags']:
        content += f"**Tags:** {', '.join(f'`{tag}`' for tag in metadata['tags'])}\n\n"
    
    content += f"""## 📝 Description

{metadata['description']}

This notebook is part of the Botanical Research collection, providing tools and analysis for plant science research.

## 🚀 Quick Start

### Running in Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/{metadata['path']})

### Running Locally
```bash
# Clone the repository
git clone https://github.com/outobecca/botanical-colabs.git
cd botanical-colabs

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook {metadata['path']}
```

## 📚 Contents

This notebook contains {metadata['total_cells']} cells organized into sections:

- **Code Cells:** {metadata['code_cells']} - Python code for data processing and analysis
- **Markdown Cells:** {metadata['markdown_cells']} - Documentation and explanations

## 🔬 Features

"""
    
    # Add category-specific features
    if category == 'templates':
        content += """- 📐 Template structure for new notebooks
- 🎨 Standardized formatting and styling
- 📋 Best practices and guidelines
- 🔧 Reusable code patterns
"""
    elif category == 'agrology':
        content += """- 🌾 Agricultural data analysis
- 📊 Crop yield predictions
- 🧪 Soil analysis and recommendations
- 📈 Environmental monitoring
"""
    elif category == 'greenhouse':
        content += """- 🏗️ Greenhouse environment monitoring
- 💡 Lighting optimization
- 🌡️ Climate control analysis
- 📊 Growth tracking and prediction
"""
    elif category == 'regional':
        content += """- 🗺️ Regional climate analysis
- 🌍 Location-specific plant recommendations
- 📍 Geographic data visualization
- 🌤️ Weather pattern analysis
"""
    elif category == 'education':
        content += """- 🎓 Educational content and tutorials
- 📚 Step-by-step learning materials
- 🔍 Interactive examples
- 💡 Practical exercises
"""
    else:
        content += """- 📊 Data analysis and visualization
- 🔬 Scientific computations
- 📈 Statistical analysis
- 🎨 Interactive plots and charts
"""
    
    content += f"""
## 🛠️ Requirements

### Python Packages
This notebook requires the following Python packages:

```python
jupyter
numpy
pandas
matplotlib
seaborn
```

Install all requirements:
```bash
pip install -r requirements.txt
```

### Data Requirements
- Input data format specifications (if applicable)
- Required API keys or credentials (if applicable)
- External data sources (if applicable)

## 📖 Usage Examples

### Basic Usage
1. Open the notebook in Jupyter or Google Colab
2. Run cells sequentially from top to bottom
3. Modify parameters in configuration cells as needed
4. Analyze results in output cells

### Advanced Usage
- Customize analysis parameters
- Integrate with your own datasets
- Extend functionality with additional code
- Export results in various formats

## 📊 Preview

[View HTML Preview](../previews/html/{Path(notebook_path).stem}.html)

![Notebook Preview](../thumbnails/{Path(notebook_path).stem}.png)

## 🤝 Contributing

Contributions to improve this notebook are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test thoroughly
5. Submit a pull request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

## 🔍 Peer Review

This notebook is part of our peer review system. Check the current review status:

- Review status badge on main repository page
- Scientific accuracy verification
- Community feedback and ratings

## 📄 License

This notebook is part of the Botanical Research collection.  
See [LICENSE](../LICENSE) for details.

## 🔗 Related Resources

- [Project Documentation](../)
- [API Reference](../docs/api/)
- [Contributing Guidelines](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)

## 📞 Support

- 🐛 [Report Issues](https://github.com/outobecca/botanical-colabs/issues)
- 💬 [Discussions](https://github.com/outobecca/botanical-colabs/discussions)
- 📧 Contact: [Repository Maintainers](https://github.com/outobecca/botanical-colabs)

---

*Last updated: {datetime.now().strftime('%Y-%m-%d')}*  
*Auto-generated by Documentation Workflow*
"""
    
    # Write wiki page
    with open(wiki_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Generated wiki page: {wiki_path}")
    return wiki_path


def generate_html_preview(notebook_path):
    """Generate HTML preview of the notebook."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Configure HTML exporter
        html_exporter = HTMLExporter()
        html_exporter.template_name = 'classic'
        html_exporter.exclude_input = True  # Hide code cells
        
        # Convert to HTML
        (body, resources) = html_exporter.from_notebook_node(nb)
        
        # Add preview badge
        preview_badge = '''
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; padding: 15px; margin-bottom: 20px; border-radius: 8px;
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
            <h2 style="margin: 0 0 10px 0;">📖 Notebook Preview</h2>
            <p style="margin: 0; opacity: 0.9;">
                This is a preview showing only the rendered outputs. 
                <a href="https://github.com/outobecca/botanical-colabs" 
                   style="color: #fff; text-decoration: underline;">
                   View full notebook on GitHub
                </a>
            </p>
        </div>
        '''
        body = body.replace('<body>', f'<body>{preview_badge}')
        
        # Save HTML
        output_path = f"previews/html/{Path(notebook_path).stem}.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(body)
        
        print(f"✓ Generated HTML preview: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"⚠ Error generating HTML preview for {notebook_path}: {e}")
        return None


def generate_thumbnail(notebook_path):
    """Generate a thumbnail image for the notebook preview."""
    try:
        # Create a simple thumbnail with notebook info
        img = Image.new('RGB', (800, 400), color=(13, 17, 23))
        draw = ImageDraw.Draw(img)
        
        # Try to use a nice font, fall back to default if not available
        try:
            title_font = ImageFont.truetype("arial.ttf", 48)
            text_font = ImageFont.truetype("arial.ttf", 24)
        except:
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
        
        # Add gradient-like effect (simple)
        for y in range(400):
            color_value = int(13 + (y / 400) * 10)
            draw.line([(0, y), (800, y)], fill=(color_value, color_value + 4, color_value + 10))
        
        # Add notebook name
        notebook_name = Path(notebook_path).stem.replace('_', ' ').replace('-', ' ').title()
        
        # Draw text with shadow
        draw.text((52, 152), notebook_name, fill=(0, 0, 0), font=title_font)
        draw.text((50, 150), notebook_name, fill=(88, 166, 255), font=title_font)
        
        # Add subtitle
        subtitle = "Jupyter Notebook Preview"
        draw.text((52, 252), subtitle, fill=(0, 0, 0), font=text_font)
        draw.text((50, 250), subtitle, fill=(139, 148, 158), font=text_font)
        
        # Add emoji/icon
        draw.text((52, 52), "📓", font=title_font)
        
        # Save thumbnail
        output_path = f"thumbnails/{Path(notebook_path).stem}.png"
        img.save(output_path, 'PNG')
        
        print(f"✓ Generated thumbnail: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"⚠ Error generating thumbnail for {notebook_path}: {e}")
        return None


def main():
    """Main execution function."""
    print("=" * 60)
    print("Auto-Documentation Generator")
    print("=" * 60)
    
    # Setup
    setup_directories()
    
    # Get changed notebooks
    notebooks = get_changed_notebooks()
    
    if not notebooks:
        print("No notebooks to process. Exiting.")
        return 0
    
    print(f"\nProcessing {len(notebooks)} notebook(s)...\n")
    
    # Process each notebook
    success_count = 0
    for notebook_path in notebooks:
        print(f"\n📓 Processing: {notebook_path}")
        print("-" * 60)
        
        # Check if file exists
        if not Path(notebook_path).exists():
            print(f"⚠ File not found: {notebook_path}")
            continue
        
        try:
            # Extract metadata
            metadata = extract_notebook_metadata(notebook_path)
            if not metadata:
                print(f"⚠ Skipping {notebook_path} due to metadata extraction failure")
                continue
            
            # Generate documentation
            wiki_page = generate_wiki_page(notebook_path, metadata)
            html_preview = generate_html_preview(notebook_path)
            thumbnail = generate_thumbnail(notebook_path)
            
            success_count += 1
            print(f"✅ Successfully processed: {notebook_path}")
        
        except Exception as e:
            print(f"❌ Error processing {notebook_path}: {e}")
            import traceback
            traceback.print_exc()
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Documentation Generation Complete")
    print("=" * 60)
    print(f"✓ Successfully processed: {success_count}/{len(notebooks)} notebooks")
    print(f"✓ Wiki pages created in: wiki/")
    print(f"✓ HTML previews created in: previews/html/")
    print(f"✓ Thumbnails created in: thumbnails/")
    
    return 0 if success_count == len(notebooks) else 1


if __name__ == '__main__':
    sys.exit(main())
