#!/usr/bin/env python3
"""
GitHub Wiki Page Generator for Botanical Colabs Notebooks

This script generates comprehensive wiki pages for all notebooks in the repository.
Each wiki page includes:
- Overview and description
- Use cases
- Key features
- Getting started guide
- Code examples
- Troubleshooting
- Related resources

Usage:
    python generate_wiki_pages.py

Output:
    Creates .md files in wiki/ directory
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional

# Notebook metadata
NOTEBOOKS = {
    # Templates
    "TEMPLATE-Botanical-Notebook": {
        "file": "notebooks/templates/TEMPLATE_botanical_notebook.ipynb",
        "title": "📐 General Botanical Template",
        "category": "Templates",
        "description": "Comprehensive general-purpose template for botanical science notebooks",
        "features": [
            "Literature review sections",
            "Data collection framework", 
            "Analysis templates",
            "Visualization examples",
            "GBIF and Trefle integration"
        ],
        "use_cases": [
            "General botanical research",
            "Species documentation",
            "Data exploration",
            "Student projects",
            "Educational materials"
        ]
    },
    "TEMPLATE-Data-Analysis": {
        "file": "notebooks/templates/TEMPLATE_data_analysis.ipynb",
        "title": "📊 Data Analysis Template",
        "category": "Templates",
        "description": "Specialized template for analyzing environmental sensors, soil tests, and plant measurements",
        "features": [
            "Statistical analysis tools",
            "Outlier detection",
            "Correlation analysis",
            "Automated reporting",
            "Data quality assessment"
        ],
        "use_cases": [
            "Greenhouse sensor data",
            "Field measurements",
            "Soil test analysis",
            "Environmental monitoring",
            "Quality control"
        ]
    },
    
    # Agrology
    "Agrology-Data-Analysis-Exploration": {
        "file": "notebooks/agrology/data_analysis_exploration.ipynb",
        "title": "🌾 Data Analysis & Exploration",
        "category": "Agrology",
        "description": "Comprehensive toolkit for agricultural data exploration and analysis",
        "features": [
            "Automated outlier detection",
            "Statistical summaries",
            "Correlation analysis",
            "Time-series visualization",
            "Data quality checks"
        ],
        "use_cases": [
            "Crop yield analysis",
            "Soil data exploration",
            "Environmental sensor analysis",
            "Field trial results",
            "Research data QC"
        ]
    },
    
    # Greenhouse
    "Greenhouse-ML-Yield-Prediction": {
        "file": "notebooks/greenhouse/ml_yield_prediction.ipynb",
        "title": "🤖 ML Yield Prediction",
        "category": "Greenhouse",
        "description": "Machine learning models for crop yield prediction and optimization",
        "features": [
            "Random Forest models",
            "Gradient Boosting",
            "Feature importance analysis",
            "Cross-validation",
            "Prediction confidence intervals"
        ],
        "use_cases": [
            "Yield forecasting",
            "Disease risk assessment",
            "Optimal condition recommendations",
            "Resource planning",
            "Harvest scheduling"
        ]
    },
    
    # Add more notebooks here...
}

def generate_wiki_page(notebook_id: str, metadata: Dict) -> str:
    """Generate wiki page content for a notebook"""
    
    content = f"""# {metadata['title']}

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/{metadata['file']})

> **{metadata['description']}**

---

## 📋 Overview

{metadata['description']}

This notebook is part of the **{metadata['category']}** category and provides specialized tools for botanical research and analysis.

---

## 🎯 Use Cases

"""
    
    for use_case in metadata['use_cases']:
        content += f"- ✅ **{use_case}**\n"
    
    content += f"""
---

## ⭐ Key Features

"""
    
    for feature in metadata['features']:
        content += f"- ✅ {feature}\n"
    
    content += f"""
---

## 🚀 Getting Started

### Quick Start

1. **Open in Colab** — Click the badge above
2. **Run installation cell** — Install required libraries
3. **Configure settings** — Use interactive widgets
4. **Execute analysis** — Run cells sequentially
5. **Review results** — Examine output and visualizations

### Prerequisites

**Required:**
- Google account (for Colab)
- Internet connection

**Optional:**
- API keys (for full features)
- Sample data (or use built-in examples)

---

## 📦 What's Included

### Notebook Structure

*(Customize based on actual notebook)*

1. **Introduction** — Overview and setup
2. **Installation** — Library dependencies
3. **Configuration** — Interactive UI
4. **Functions** — Helper functions
5. **Analysis** — Main workflow
6. **Visualization** — Results display
7. **Export** — Output options
8. **Citations** — Data sources

---

## 💡 Usage Examples

### Basic Usage

```python
# Configure your analysis
species_name = "Your species"
data_source = "GBIF"

# Run analysis
results = analyze_data(species_name)

# Display results
display(results)
```

---

## 🔧 Advanced Features

*(Document advanced features specific to this notebook)*

---

## 📊 Expected Output

*(Describe what users should expect to see)*

---

## 🐛 Troubleshooting

### Common Issues

**Issue 1:**
- ✅ Solution 1
- ✅ Solution 2

**Issue 2:**
- ✅ Solution 1
- ✅ Solution 2

---

## 📚 Related Resources

### Documentation
- [Main Repository](https://github.com/outobecca/botanical-colabs)
- [API Setup Guide](https://github.com/outobecca/botanical-colabs/blob/main/API_SETUP.md)
- [Contributing Guidelines](https://github.com/outobecca/botanical-colabs/blob/main/CONTRIBUTING.md)

### Related Notebooks
- [Other related notebook 1](#)
- [Other related notebook 2](#)

---

## 📄 License

MIT License — Free to use, modify, and distribute

**Citation:**
```bibtex
@software{{botanical_notebook_2025,
  author = {{Sihvonen, Pekka}},
  title = {{{metadata['title']} - Botanical Colabs}},
  year = {{2025}},
  publisher = {{GitHub}},
  url = {{https://github.com/outobecca/botanical-colabs}}
}}
```

---

## 🤝 Contributing

Found an issue or have a suggestion?

- 🐛 [Report Issue](https://github.com/outobecca/botanical-colabs/issues/new)
- 💬 [Start Discussion](https://github.com/outobecca/botanical-colabs/discussions)
- 🔀 [Submit Pull Request](https://github.com/outobecca/botanical-colabs/pulls)

---

**Created:** 2025-11-04  
**Version:** 2.0  
**Status:** ✅ Production Ready

[← Back to {metadata['category']}](Home#{metadata['category'].lower()}-notebooks) | [View on GitHub](https://github.com/outobecca/botanical-colabs/blob/main/{metadata['file']})
"""
    
    return content


def main():
    """Generate all wiki pages"""
    
    # Create wiki directory if it doesn't exist
    wiki_dir = Path("wiki")
    wiki_dir.mkdir(exist_ok=True)
    
    print("🚀 Generating GitHub Wiki pages...")
    print(f"📁 Output directory: {wiki_dir}")
    print()
    
    # Generate pages
    for notebook_id, metadata in NOTEBOOKS.items():
        print(f"📝 Generating: {notebook_id}.md")
        
        # Generate content
        content = generate_wiki_page(notebook_id, metadata)
        
        # Write to file
        output_file = wiki_dir / f"{notebook_id}.md"
        output_file.write_text(content, encoding='utf-8')
        
        print(f"   ✅ Created: {output_file}")
    
    print()
    print(f"✅ Generated {len(NOTEBOOKS)} wiki pages!")
    print()
    print("📖 Next steps:")
    print("1. Review generated pages in wiki/ directory")
    print("2. Customize content for each notebook")
    print("3. Add screenshots and examples")
    print("4. Push to GitHub wiki repository")
    print()
    print("🔗 GitHub Wiki setup:")
    print("   git clone https://github.com/outobecca/botanical-colabs.wiki.git")
    print("   cp wiki/*.md botanical-colabs.wiki/")
    print("   cd botanical-colabs.wiki")
    print("   git add .")
    print("   git commit -m 'Add comprehensive notebook documentation'")
    print("   git push")


if __name__ == "__main__":
    main()
