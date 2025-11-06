# Google Gemini Agent Instructions

This document provides comprehensive instructions for Google Gemini when assisting with the **Botanical Sciences Colab Notebooks** repository.

## 🎯 Repository Overview

**Repository:** Botanical Sciences Colab Notebooks  
**Purpose:** Collection of reproducible Jupyter/Colab notebooks for botanical, horticultural, and agricultural research  
**Tech Stack:** Python, Jupyter, Google Colab, MyST Markdown, Marp presentations  
**License:** MIT  

### Primary Goals
- Provide production-ready notebooks for botanical research
- Create accessible educational materials for plant science data analysis
- Integrate multiple open data sources (GBIF, Trefle, FMI, Wikipedia, iNaturalist)
- Enable zero-setup research via Google Colab
- Support AI-assisted workflows with Google Gemini API

## 📂 Repository Structure

```
botanical-colab-notebooks/
├── notebooks/
│   ├── templates/          # Starter templates for different workflows
│   ├── agrology/          # Field crop and soil science analysis
│   ├── greenhouse/        # Protected cultivation management
│   ├── regional/          # Region-specific analysis (Finland, etc.)
│   ├── education/         # Interactive learning materials
│   └── examples/          # Real-world implementations
├── wiki/                  # Auto-generated documentation
├── blog/                  # Jekyll blog posts
├── _posts/                # Additional blog content
├── API_SETUP.md           # API key configuration guide
├── CONTRIBUTING.md        # Contribution guidelines
├── TEMPLATE_GUIDE.md      # Detailed template usage instructions
├── MYST_MARP_GUIDE.md     # MyST & Marp integration guide
└── PEER_REVIEW.md         # Peer review process documentation
```

## 🤖 When to Use Gemini API

The repository uses Google Gemini API for:
1. **Content Summarization** — Condensing botanical information from multiple sources
2. **Multi-language Generation** — Creating plant descriptions in 9 languages
3. **Data Interpretation** — Extracting insights from complex datasets
4. **AI-Powered Analysis** — Natural language processing of botanical texts

**Example Notebooks Using Gemini:**
- `notebooks/examples/generator-plant-card.ipynb` — Multi-source plant card generator with AI summarization

## 📝 Code Standards

### Python Style Guidelines

#### Type Hints (Required)
```python
from typing import Optional, Dict, List, Any

def fetch_species_data(
    scientific_name: str,
    include_images: bool = True
) -> Optional[Dict[str, Any]]:
    """
    Fetch species data from GBIF API.
    
    Args:
        scientific_name: Binomial nomenclature (e.g., "Quercus robur")
        include_images: Whether to fetch associated images
    
    Returns:
        Dictionary with species data or None if not found
        
    Source:
        GBIF.org - Global Biodiversity Information Facility
        https://www.gbif.org
        DOI: 10.15468/dl.xxxxx
    """
    pass
```

#### Error Handling (Required)
```python
def safe_api_call(
    url: str,
    timeout: int = 10
) -> Optional[Dict[str, Any]]:
    """Safe API call with comprehensive error handling."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"⏱️ Timeout: {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ API Error: {e}")
        return None
    except json.JSONDecodeError:
        print("❌ Invalid JSON response")
        return None
```

#### Documentation (Required)
- **All functions** must have docstrings with Args, Returns, and Source
- **Complex logic** must have inline comments
- **Data sources** must include citations with access dates and DOIs
- **Assumptions and limitations** must be documented

### Notebook Structure

**Use the Template:** All new notebooks should start from `notebooks/templates/TEMPLATE_botanical_notebook.ipynb`

**6-Step Structure:**
1. **Installation & Configuration** — Packages, imports, UI widgets, API keys
2. **Helper Functions** — Reusable utilities (API calls, validation, formatting)
3. **Data Fetching Functions** — API integrations organized by source
4. **Execute Data Collection** — Main workflow orchestration
5. **Data Analysis & Visualization** — Tables, plots, statistical summaries
6. **Citations & Documentation** — Data provenance and source citations

### Scientific Rigor Requirements

#### Data Source Citations (Required)
```markdown
### Data Sources

1. **GBIF** (Accessed: 2025-11-06)
   - Global Biodiversity Information Facility
   - https://www.gbif.org
   - DOI: 10.15468/dl.xxxxx
   - License: CC0 / CC-BY (varies by dataset)

2. **Trefle API** (Accessed: 2025-11-06)
   - Botanical data for 400,000+ species
   - https://trefle.io
   - License: API Terms of Service
```

#### AI-Generated Content Disclaimers (Required)
```markdown
### ⚠️ AI-Generated Content Notice

This notebook uses Google Gemini API for content summarization and translation.

**Important:**
- AI-generated content is **not peer-reviewed**
- Always **verify critical information** against authoritative sources
- Use for **educational and exploratory purposes**
- Not suitable for **formal publications** without verification
```

#### Data Quality Indicators (Required)
- Include confidence scores (e.g., GBIF matching confidence)
- Note data completeness and gaps
- Document validation steps
- Provide data quality warnings

## 🛠️ Working with Templates

### Template Selection Guide

1. **TEMPLATE_myst_scientific.ipynb** — For scientific papers and technical documentation
   - MyST markdown features (cross-references, citations, admonitions)
   - Auto-reload for efficient development
   - %%writefile for code modularization
   - Jupyter Book compatibility

2. **TEMPLATE_marp_presentation.ipynb** — For presentations and slide decks
   - Marp markdown for slides
   - Export to HTML, PDF, PowerPoint
   - Live demo code cells
   - Professional visualizations

3. **TEMPLATE_botanical_notebook.ipynb** — General-purpose botanical research
   - GBIF, Trefle, Wikipedia integration
   - Interactive UI widgets
   - Comprehensive error handling

4. **TEMPLATE_data_analysis.ipynb** — For sensor data and measurements
   - Statistical tests and outlier detection
   - Correlation analysis
   - Automated reporting

5. **TEMPLATE_machine_learning.ipynb** — For ML applications
   - Feature engineering
   - Model selection and tuning
   - Agricultural metrics evaluation

6. **TEMPLATE_environmental_monitoring.ipynb** — For sustainability analysis
   - Soil health monitoring
   - Water usage tracking
   - Climate data analysis

### Template Customization Steps

1. **Copy template** to appropriate directory (`agrology/`, `greenhouse/`, etc.)
2. **Update header** with title, author, date, description
3. **Modify imports** based on required packages
4. **Customize helper functions** for specific data sources
5. **Implement data fetching** for your APIs
6. **Add analysis logic** and visualizations
7. **Update citations** with accurate sources and access dates
8. **Test thoroughly** in Google Colab

**Detailed guide:** See [TEMPLATE_GUIDE.md](TEMPLATE_GUIDE.md)

## 🔑 API Integration

### Supported APIs and Data Sources

1. **GBIF** (Global Biodiversity Information Facility)
   - Species occurrence data (2+ billion records)
   - Taxonomic backbone
   - Free, no API key required
   - Rate limit: Reasonable use policy

2. **Trefle** (Plant Database)
   - 400,000+ plant species
   - Requires free API key
   - Rate limit: 120 requests/minute

3. **Google Gemini** (AI Analysis)
   - Content summarization and translation
   - Requires API key from Google AI Studio
   - Rate limit: Varies by tier

4. **FMI Open Data** (Finnish Meteorological Institute)
   - Weather data and climate analysis
   - Free for non-commercial use
   - No API key required

5. **Wikipedia/Wikimedia**
   - Encyclopedic content and images
   - Free, no API key required
   - Respect usage guidelines

6. **iNaturalist**
   - Community science observations
   - Free API access
   - Rate limit: 100 requests/minute

### API Key Management (Colab Secrets)

```python
from google.colab import userdata

# Retrieve API keys from Colab Secrets
try:
    GEMINI_API_KEY = userdata.get('GEMINI_API_KEY')
    TREFLE_API_KEY = userdata.get('TREFLE_API_KEY')
except Exception as e:
    print("⚠️ API keys not found in Colab Secrets")
    print("See API_SETUP.md for configuration instructions")
```

**Important:**
- Never hardcode API keys in notebooks
- Use Colab Secrets or environment variables
- Add `.env` to `.gitignore`
- Document required keys in notebook header

**Setup guide:** See [API_SETUP.md](API_SETUP.md)

## 🧪 Testing Requirements

### Before Submitting Code

1. **Test in Google Colab** (Primary environment)
   - Upload notebook to Colab
   - Run all cells sequentially
   - Verify all outputs
   - Test with edge cases

2. **Test Error Handling**
   - Invalid API keys
   - Network timeouts
   - Malformed data
   - Empty responses
   - Rate limit exceeded

3. **Test Edge Cases**
   - Empty strings
   - Special characters
   - Non-existent species
   - Multiple languages
   - Large datasets

4. **Verify Outputs**
   - Data visualizations render correctly
   - Tables display properly
   - Downloads work as expected
   - Citations are complete

### Local Testing (Optional)

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook
```

## 📊 Data Visualization Standards

### Library Preferences

1. **Matplotlib** — Publication-quality static plots
2. **Seaborn** — Statistical graphics and heatmaps
3. **Plotly** — Interactive dashboards and 3D visualizations
4. **Pandas** — Data tables and summaries

### Visualization Best Practices

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set consistent style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

# Create informative plots
def plot_species_distribution(data: pd.DataFrame) -> None:
    """
    Plot species geographic distribution.
    
    Args:
        data: DataFrame with latitude, longitude columns
    """
    fig, ax = plt.subplots()
    ax.scatter(data['longitude'], data['latitude'], 
               alpha=0.6, s=50, c='green')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Species Distribution Map')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
```

**Requirements:**
- Axis labels and titles (always)
- Color-blind friendly palettes
- Appropriate plot types for data
- Legends when needed
- High DPI for publications (300 dpi)

## 🌍 Multi-language Support

### Supported Languages

The repository supports 9 languages for Wikipedia content and AI-generated summaries:
- English (en)
- Finnish (fi)
- Swedish (sv)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Dutch (nl)

### Language Configuration

```python
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'fi': 'Finnish',
    'sv': 'Swedish',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'nl': 'Dutch'
}

def get_wikipedia_content(
    species: str,
    language: str = 'en'
) -> Optional[str]:
    """Fetch Wikipedia content in specified language."""
    if language not in SUPPORTED_LANGUAGES:
        print(f"⚠️ Unsupported language: {language}")
        language = 'en'
    # Implementation...
```

## 🔄 Contribution Workflow

### For Gemini-Assisted Development

1. **Understand requirements** from user request
2. **Select appropriate template** based on use case
3. **Generate code** following style guidelines
4. **Include comprehensive docstrings** with type hints
5. **Add error handling** for all external calls
6. **Provide citations** for all data sources
7. **Test thoroughly** before suggesting submission
8. **Document assumptions** and limitations

### Academic Verification

**Important:** This repository requires academic verification for contributors.

- All contributors must be affiliated with accredited institutions
- Verification process documented in `.github/ACADEMIC_VERIFICATION.md`
- Ensures scientific rigor and credibility

**When assisting users:**
- Remind them about verification requirements
- Direct them to CONTRIBUTING.md for details
- Encourage proper scientific documentation

### Peer Review Process

**Review Requirements:**
- Templates: 2 peer reviews
- Examples: 2 peer reviews
- Educational: 1 peer review
- Regional: 1 peer review

**Review Categories:**
- Scientific Accuracy
- Methodology
- Documentation
- Usability
- Reproducibility

**See:** [PEER_REVIEW.md](PEER_REVIEW.md)

## 🤖 Auto-Documentation

The repository includes automated workflows that generate:

1. **Wiki Pages** — Comprehensive documentation
2. **HTML Previews** — Rendered notebook outputs
3. **Thumbnails** — Preview images for gallery

**When creating notebooks:**
- Add good metadata in first markdown cell
- Include clear title and description
- Use tags for categorization
- Workflows will auto-generate documentation on PR

**Learn more:** `.github/workflows/AUTO_DOCUMENTATION.md`

## ⚠️ Common Pitfalls to Avoid

### Security Issues
- ❌ Never commit API keys to repository
- ❌ Never hardcode credentials in notebooks
- ❌ Never expose sensitive data in outputs

### Code Quality Issues
- ❌ Missing type hints on functions
- ❌ No error handling for API calls
- ❌ Missing docstrings
- ❌ Hardcoded values that should be parameters

### Scientific Issues
- ❌ Missing data source citations
- ❌ No data quality indicators
- ❌ AI content without disclaimers
- ❌ Undocumented assumptions

### Usability Issues
- ❌ Unclear variable names
- ❌ No progress indicators for long operations
- ❌ Poor error messages
- ❌ Missing usage examples

## 📚 Key Documentation Files

**Must Read:**
- [CONTRIBUTING.md](CONTRIBUTING.md) — Contribution guidelines and standards
- [TEMPLATE_GUIDE.md](TEMPLATE_GUIDE.md) — Detailed template usage instructions
- [API_SETUP.md](API_SETUP.md) — API key configuration guide

**Important:**
- [MYST_MARP_GUIDE.md](MYST_MARP_GUIDE.md) — MyST markdown and Marp presentations
- [PEER_REVIEW.md](PEER_REVIEW.md) — Peer review process
- [QUICKSTART.md](QUICKSTART.md) — Quick start guide

**Reference:**
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [LICENSE](LICENSE) — MIT license details

## 🎓 Educational Philosophy

When assisting with educational content:

1. **Start Simple** — Begin with basic concepts
2. **Use Real Examples** — Botanical and horticultural data
3. **Build Progressively** — Increase complexity gradually
4. **Explain Thoroughly** — Don't assume prior knowledge
5. **Provide Context** — Why this technique matters
6. **Encourage Exploration** — Interactive widgets and exercises

**Target Audience:**
- Students (high school to graduate level)
- Researchers transitioning to data science
- Hobbyists and citizen scientists
- Educators and trainers

## 🚀 Version 2.0 Features

### MyST Markdown
- Scientific cross-references
- Citation management
- Admonitions (notes, warnings, tips)
- Jupyter Book compatibility

### Marp Presentations
- Notebook to slide conversion
- HTML, PDF, PowerPoint export
- Professional themes
- Live code demonstrations

### Development Tools
- Auto-reload magic for efficient coding
- %%writefile for code modularization
- VS Code notebook integration

**See:** [MYST_MARP_GUIDE.md](MYST_MARP_GUIDE.md)

## 📞 Getting Help

- **GitHub Issues** — Bug reports and feature requests
- **GitHub Discussions** — Questions and community help
- **Documentation** — Comprehensive guides in repository

## ✅ Final Checklist

When assisting with code generation, ensure:

- [ ] Code follows Python style guidelines (PEP 8)
- [ ] All functions have type hints and docstrings
- [ ] Error handling implemented for all external calls
- [ ] Data sources properly cited with dates and DOIs
- [ ] AI-generated content has disclaimers
- [ ] No API keys or secrets in code
- [ ] Tested in Google Colab environment
- [ ] Clear comments for complex logic
- [ ] Appropriate template selected and followed
- [ ] Documentation updated if needed

---

**Maintained by:** Pekka Sihvonen  
**License:** MIT  
**Last updated:** 2025-11-06  

**For questions or clarification, refer users to repository documentation or GitHub Issues.**
