# 🌿 Botanical Notebook Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_botanical_notebook.ipynb)

> **The original and most comprehensive template for botanical data collection and analysis**

---

## 📋 Overview

The **Botanical Notebook Template** is the foundation template for all botanical projects. It provides a complete, ready-to-use framework for fetching multi-source plant data, generating AI-powered descriptions, and creating beautiful visualizations.

### What Makes It Special
- 🌍 **Multi-source integration** — GBIF, Trefle, Wikipedia, Wikimedia, and more
- 🤖 **AI-powered summaries** — Google Gemini integration
- 🎨 **Interactive UI** — Full widget-based configuration
- 📊 **Built-in visualizations** — Charts and maps
- 🌐 **9 languages supported** — EN, FI, SV, DE, FR, ES, IT, JP, CN
- 🔧 **Highly customizable** — Easy to adapt for specific needs

---

## 🎯 Use Cases

### Research & Academia
- ✅ **Taxonomy research** — Fetch complete taxonomic data
- ✅ **Botanical surveys** — Document field observations
- ✅ **Species comparisons** — Compare multiple species
- ✅ **Literature reviews** — Gather background information
- ✅ **Herbarium digitization** — Add context to specimens

### Education
- ✅ **Teaching materials** — Create educational content
- ✅ **Student projects** — Provide structured framework
- ✅ **Interactive lessons** — Demonstrate botanical concepts
- ✅ **Field trip preparation** — Research local flora
- ✅ **Quiz generation** — Create botanical quizzes

### Professional Use
- ✅ **Nursery catalogs** — Generate product descriptions
- ✅ **Garden planning** — Research plant requirements
- ✅ **Conservation work** — Document endangered species
- ✅ **Landscape design** — Research suitable plants
- ✅ **Consulting reports** — Professional documentation

### Personal Projects
- ✅ **Plant identification** — Learn about found plants
- ✅ **Garden journal** — Track your plants
- ✅ **Nature photography** — Add botanical context
- ✅ **Citizen science** — Contribute observations
- ✅ **Educational hobby** — Learn botany interactively

---

## ⭐ Key Features

### Multi-Source Data Integration

**GBIF (Global Biodiversity Information Facility):**
```python
def fetch_gbif_data(species_name: str) -> Dict[str, Any]:
    """
    Fetch comprehensive taxonomic data from GBIF.
    
    Returns:
        - Scientific name
        - Taxonomic classification (kingdom → species)
        - Common names (multiple languages)
        - Occurrence counts
        - Conservation status
    """
```

**Trefle API:**
```python
def fetch_trefle_data(species_name: str, api_key: str) -> Dict[str, Any]:
    """
    Fetch growth characteristics from Trefle.
    
    Returns:
        - Growth habits
        - Mature size
        - Flower colors
        - Foliage characteristics
        - Light requirements
        - Water needs
        - Hardiness zones
    """
```

**Wikipedia:**
```python
def fetch_wikipedia_summary(species_name: str, language: str = 'en') -> str:
    """
    Fetch encyclopedic content from Wikipedia.
    
    Supports 9 languages: EN, FI, SV, DE, FR, ES, IT, JP, CN
    """
```

**Wikimedia Commons:**
```python
def fetch_wikimedia_images(species_name: str, limit: int = 5) -> List[Dict]:
    """
    Fetch botanical illustrations and photographs.
    
    Returns:
        - High-resolution images
        - Usage rights
        - Photographer credits
        - Quality scores
    """
```

### AI-Powered Features

**Google Gemini Integration:**
```python
def generate_ai_summary(
    species_name: str,
    data: Dict[str, Any],
    language: str = 'en'
) -> str:
    """
    Generate natural language summaries.
    
    Features:
        - Context-aware descriptions
        - Multi-language support
        - Fact-checking against sources
        - Natural, readable text
    """
```

**Smart summarization:**
- Combines data from multiple sources
- Creates coherent narratives
- Highlights key characteristics
- Adapts tone to use case

### Interactive Configuration UI

**Widget-based setup:**
```python
# Species input
species_input = widgets.Text(
    value='Rosa canina',
    description='Species:',
    placeholder='Enter scientific name'
)

# Language selector
language_selector = widgets.Dropdown(
    options=['en', 'fi', 'sv', 'de', 'fr', 'es', 'it', 'jp', 'cn'],
    value='en',
    description='Language:'
)

# Data source toggles
use_gbif = widgets.Checkbox(value=True, description='GBIF')
use_trefle = widgets.Checkbox(value=True, description='Trefle')
use_wikipedia = widgets.Checkbox(value=True, description='Wikipedia')
use_wikimedia = widgets.Checkbox(value=True, description='Wikimedia')
use_ai = widgets.Checkbox(value=True, description='AI Summary')
```

**Real-time validation:**
- Check species name format
- Validate API keys
- Preview selected options
- Progress indicators

### Built-in Visualizations

**Distribution map:**
```python
def plot_distribution_map(occurrences: List[Dict]) -> None:
    """
    Plot species occurrences on world map.
    
    Features:
        - Interactive markers
        - Heatmap overlay
        - Country statistics
        - Zoom controls
    """
```

**Growth characteristics:**
```python
def plot_growth_chart(characteristics: Dict) -> None:
    """
    Visualize growth requirements.
    
    Charts:
        - Light requirements (sun/shade scale)
        - Water needs (drought/wet scale)
        - Temperature ranges (hardiness zones)
        - Growth habit comparison
    """
```

**Taxonomic tree:**
```python
def plot_taxonomy_tree(classification: Dict) -> None:
    """
    Display taxonomic hierarchy.
    
    Shows:
        - Kingdom → Phylum → Class → Order → Family → Genus → Species
        - Common ancestor relationships
        - Related species
    """
```

---

## 📦 What's Included

### Notebook Structure (14 Cells)

1. **Introduction & Overview**
   - Template description
   - Feature highlights
   - Quick start guide

2. **Library Installation**
   ```python
   !pip install -q requests pandas matplotlib seaborn ipywidgets folium
   ```

3. **Import Statements**
   - Core libraries
   - Data processing
   - Visualization tools

4. **Configuration UI**
   - Interactive widgets
   - API key inputs
   - Data source selection

5. **API Helper Functions**
   - safe_api_call()
   - validate_species_name()
   - format_scientific_name()

6. **GBIF Integration**
   - fetch_gbif_data()
   - parse_gbif_response()

7. **Trefle Integration**
   - fetch_trefle_data()
   - parse_growth_data()

8. **Wikipedia Integration**
   - fetch_wikipedia_summary()
   - extract_key_facts()

9. **Wikimedia Integration**
   - fetch_wikimedia_images()
   - select_best_image()

10. **AI Summary Generation**
    - generate_ai_summary()
    - validate_ai_output()

11. **Data Visualization**
    - plot_distribution_map()
    - plot_growth_chart()
    - plot_taxonomy_tree()

12. **Main Processing Pipeline**
    - Orchestrate all functions
    - Handle errors gracefully
    - Display results

13. **Export Functions**
    - export_to_html()
    - export_to_json()
    - export_to_markdown()

14. **Examples & Testing**
    - Sample queries
    - Edge cases
    - Performance tests

---

## 🚀 Getting Started

### Quick Start (5 minutes)

1. **Open in Colab** — Click badge above

2. **Run Setup Cells** — Execute cells 1-3:
   - Install libraries
   - Import modules
   - Load configuration

3. **Configure Species:**
   - Enter scientific name: `Rosa canina`
   - Select language: `en`
   - Check data sources to use

4. **Add API Keys (Optional):**
   - **Gemini API** (recommended): [Get free key](https://makersuite.google.com/app/apikey)
   - **Trefle API** (optional): [Get free key](https://trefle.io)

5. **Run Processing:**
   - Execute main pipeline cell
   - Wait for data fetching
   - View generated output

6. **Explore Results:**
   - Read AI summary
   - View images
   - Check visualizations
   - Export if needed

### Detailed Setup

#### API Keys Setup

**Google Gemini (Free - Recommended):**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with Google account
3. Click "Create API Key"
4. Copy key to notebook configuration

**Trefle (Free - Optional):**
1. Visit [Trefle.io](https://trefle.io)
2. Sign up for free account
3. Generate API token
4. Copy to notebook

**No API key needed:**
- GBIF — Free, no key required
- Wikipedia — Free, no key required
- Wikimedia — Free, no key required

#### Customization

**Modify data sources:**
```python
# Add custom API
def fetch_custom_data(species_name: str) -> Dict:
    url = f"https://api.example.com/species/{species_name}"
    response = requests.get(url)
    return response.json()

# Integrate in main pipeline
custom_data = fetch_custom_data(species_name)
```

**Change output format:**
```python
# Customize HTML template
html_template = """
<div class="plant-card custom-style">
    <h1>{scientific_name}</h1>
    <p>{description}</p>
    <!-- Add your custom HTML -->
</div>
"""
```

**Add new visualizations:**
```python
def plot_custom_chart(data: Dict) -> None:
    """Add your custom visualization."""
    plt.figure(figsize=(10, 6))
    # Your plotting code
    plt.show()
```

---

## 💡 Usage Examples

### Example 1: Basic Species Query

```python
# Simple query with defaults
species_name = "Rosa canina"
language = "en"

# Fetch data from all sources
data = {
    'gbif': fetch_gbif_data(species_name),
    'trefle': fetch_trefle_data(species_name, trefle_key),
    'wikipedia': fetch_wikipedia_summary(species_name, language),
    'images': fetch_wikimedia_images(species_name)
}

# Generate AI summary
summary = generate_ai_summary(species_name, data, language)

print(summary)
```

### Example 2: Multi-language Research

```python
# Fetch in multiple languages
languages = ['en', 'fi', 'sv']
species_name = "Betula pendula"

for lang in languages:
    print(f"\n=== {lang.upper()} ===")
    summary = fetch_wikipedia_summary(species_name, lang)
    print(summary)
```

### Example 3: Comparative Analysis

```python
# Compare multiple species
species_list = [
    "Quercus robur",
    "Quercus petraea",
    "Quercus cerris"
]

comparison_data = []
for species in species_list:
    data = fetch_gbif_data(species)
    comparison_data.append(data)

# Visualize comparison
plot_species_comparison(comparison_data)
```

### Example 4: Custom Export

```python
# Export with custom formatting
species_name = "Pinus sylvestris"

# Fetch all data
complete_data = process_species(species_name)

# Export to multiple formats
export_to_html(complete_data, 'pine.html')
export_to_json(complete_data, 'pine.json')
export_to_markdown(complete_data, 'pine.md')
```

---

## 📊 Data Sources Overview

| Source | Data Type | API Key | Languages | Rate Limit |
|--------|-----------|---------|-----------|------------|
| **GBIF** | Taxonomy, occurrences | ❌ Not needed | All | Unlimited |
| **Trefle** | Growth characteristics | ✅ Required | English | 120/hour |
| **Wikipedia** | Encyclopedic content | ❌ Not needed | 9 languages | Unlimited |
| **Wikimedia** | Images, illustrations | ❌ Not needed | All | Unlimited |
| **iNaturalist** | Observations | ❌ Not needed | All | Unlimited |
| **Google Gemini** | AI summaries | ✅ Required | 100+ | 60/min |

---

## 🔧 Advanced Features

### Caching API Responses

```python
import json
from pathlib import Path

def cache_api_response(key: str, data: Dict) -> None:
    """Cache API responses to reduce requests."""
    cache_dir = Path('.cache')
    cache_dir.mkdir(exist_ok=True)
    
    with open(cache_dir / f"{key}.json", 'w') as f:
        json.dump(data, f)

def get_cached_response(key: str) -> Optional[Dict]:
    """Retrieve cached response if available."""
    cache_file = Path('.cache') / f"{key}.json"
    if cache_file.exists():
        with open(cache_file) as f:
            return json.load(f)
    return None
```

### Batch Processing

```python
def process_species_list(species_list: List[str]) -> List[Dict]:
    """Process multiple species efficiently."""
    results = []
    
    for species in species_list:
        # Check cache first
        cached = get_cached_response(species)
        if cached:
            results.append(cached)
            continue
        
        # Fetch and cache
        data = process_species(species)
        cache_api_response(species, data)
        results.append(data)
    
    return results
```

### Error Recovery

```python
def process_with_retry(
    species_name: str,
    max_retries: int = 3
) -> Dict:
    """Retry failed requests with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return process_species(species_name)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt
            print(f"Retry {attempt + 1} after {wait_time}s...")
            time.sleep(wait_time)
```

---

## 🐛 Troubleshooting

### Common Issues

**Species not found:**
```
✅ Check scientific name spelling
✅ Try genus name only
✅ Search GBIF first to verify name
✅ Check for synonyms
```

**API key errors:**
```
✅ Verify key is copied correctly (no extra spaces)
✅ Check key hasn't expired
✅ Ensure key has required permissions
✅ Try regenerating key
```

**No Wikipedia content:**
```
✅ Try different language
✅ Search by common name
✅ Check species has Wikipedia article
✅ Try genus-level article
```

**Images not loading:**
```
✅ Check internet connection
✅ Try different search terms
✅ Verify Wikimedia is accessible
✅ Check image exists for species
```

**Slow processing:**
```
✅ Disable optional data sources
✅ Skip AI summary for faster results
✅ Use cached responses
✅ Process one species at a time
```

---

## 📚 Related Resources

### Templates
- [MyST Scientific Template](TEMPLATE-MyST-Scientific) — Advanced documentation
- [Data Analysis Template](TEMPLATE-Data-Analysis) — Analyze collected data
- [Machine Learning Template](TEMPLATE-Machine-Learning) — Build models

### Examples
- [Plant Card Generator](Examples-Plant-Card-Generator) — Based on this template
- [Batch Plant Cards](Examples-Batch-Plant-Cards) — Process multiple species

### Documentation
- [API Setup Guide](https://github.com/outobecca/botanical-colabs/blob/main/API_SETUP.md)
- [MyST & Marp Guide](https://github.com/outobecca/botanical-colabs/blob/main/MYST_MARP_GUIDE.md)
- [Contributing Guide](https://github.com/outobecca/botanical-colabs/blob/main/CONTRIBUTING.md)

### External Resources
- [GBIF Data Portal](https://www.gbif.org)
- [Trefle API Documentation](https://docs.trefle.io)
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)
- [Google Gemini](https://ai.google.dev)

---

## 📄 License

MIT License — Free to use, modify, and distribute

**Attribution:**
```
Botanical Notebook Template
Created by Pekka Sihvonen
https://github.com/outobecca/botanical-colabs
```

**Citation:**
```bibtex
@software{botanical_notebook_template_2025,
  author = {Sihvonen, Pekka},
  title = {Botanical Notebook Template - Botanical Colabs},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/outobecca/botanical-colabs}
}
```

---

## 🤝 Contributing

Help improve this template!

**Ideas for contributions:**
- 🌍 Add new data sources
- 🎨 Improve visualizations
- 🌐 Add more languages
- 📚 Better documentation
- 🐛 Fix bugs
- ⚡ Performance improvements

[Submit Issues](https://github.com/outobecca/botanical-colabs/issues) | [Pull Requests](https://github.com/outobecca/botanical-colabs/pulls)

---

**Created:** 2024-01-15  
**Updated:** 2025-11-05  
**Version:** 1.5  
**Status:** ✅ Production Ready

[← Back to Templates](Home#-templates) | [View on GitHub](https://github.com/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_botanical_notebook.ipynb)
