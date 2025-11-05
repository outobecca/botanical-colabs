# 🌿 Plant Card Generator

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/examples/generator-plant-card.ipynb)

> **Create comprehensive, professionally formatted plant care cards by aggregating data from multiple botanical databases**

---

## 📋 Overview

The Plant Card Generator is an advanced multi-source data aggregation tool that creates comprehensive plant information cards by fetching and combining data from 9+ different botanical APIs and databases. Perfect for creating educational materials, nursery labels, botanical garden signage, or personal plant reference cards.

### Key Capabilities
- 🌍 **Multi-source data** — GBIF, Trefle, Wikipedia, iNaturalist, and more
- 🤖 **AI-powered summaries** — Google Gemini integration
- 🌐 **9 languages supported** — English, Finnish, Swedish, German, French, Spanish, Italian, Portuguese, Dutch
- 📸 **Automated images** — Quality-scored selection from Wikimedia
- ✅ **Data validation** — Cross-reference verification
- 📄 **Multiple formats** — HTML, JSON, printable cards

---

## 🎯 Use Cases

### Education & Research
- ✅ **Botanical education materials** — Create teaching resources
- ✅ **Species documentation** — Research database entries
- ✅ **Field guides** — Printable identification cards
- ✅ **Lab notebooks** — Quick species reference
- ✅ **Student projects** — Data collection practice

### Commercial
- ✅ **Nursery labels** — Professional plant tags
- ✅ **Botanical garden signage** — Visitor information
- ✅ **Garden center displays** — Customer education
- ✅ **Landscape planning** — Plant selection guides
- ✅ **E-commerce** — Product descriptions

### Personal
- ✅ **Garden planning** — Plant database for your garden
- ✅ **Plant collection** — Personal herbarium
- ✅ **Learning tool** — Botanical knowledge building
- ✅ **Gift cards** — Beautiful plant information cards

---

## ⭐ Key Features

### Multi-Source Data Integration

#### GBIF (Global Biodiversity Information Facility)
- **Taxonomy** — Scientific classification
- **Distribution** — Geographic occurrence data
- **Conservation status** — IUCN Red List integration
- **Synonyms** — Alternative scientific names
- **2 billion+ records**

#### Trefle API
- **Growth characteristics** — Height, spread, growth rate
- **Care requirements** — Light, water, temperature, pH
- **Growth form** — Tree, shrub, herb, etc.
- **Toxicity** — Safety information
- **400,000+ species**

#### Wikipedia
- **Encyclopedic content** — General descriptions
- **9 languages** — Multi-language support
- **Common names** — Vernacular names
- **Cultural information** — History and uses

#### Wikimedia Commons
- **Botanical illustrations** — High-quality images
- **Historical drawings** — Heritage collections
- **Quality scoring** — Automated selection
- **Proper attribution** — License tracking

#### iNaturalist
- **Community observations** — Real-world sightings
- **Common names** — Multiple languages
- **Observation counts** — Popularity metrics
- **Geographic data** — Where it's been seen

#### Encyclopedia of Life (EOL)
- **Ecological data** — Habitat information
- **Reproduction** — Life cycle details
- **Behavior** — Growth patterns

#### Biodiversity Heritage Library (BHL)
- **Historical illustrations** — Vintage botanical art
- **Scientific literature** — Research papers
- **Rare species** — Historical documentation

### AI-Powered Features

#### Google Gemini Integration
- **Smart summarization** — Condense multiple sources
- **Natural language** — Readable descriptions
- **Multi-language** — Generate in any supported language
- **Context-aware** — Botanical knowledge
- **Fact checking** — Cross-reference validation

#### Automated Quality Control
- **Data validation** — Consistency checks
- **Source verification** — Multiple confirmations
- **Error detection** — Flag inconsistencies
- **Completeness scoring** — Data coverage metrics

### Language Support

**Supported languages:**
- 🇬🇧 **English** — Default, most complete
- 🇫🇮 **Finnish (Suomi)** — Wikipedia + AI
- 🇸🇪 **Swedish (Svenska)** — Wikipedia + AI
- 🇩🇪 **German (Deutsch)** — Wikipedia + AI
- 🇫🇷 **French (Français)** — Wikipedia + AI
- 🇪🇸 **Spanish (Español)** — Wikipedia + AI
- 🇮🇹 **Italian (Italiano)** — Wikipedia + AI
- 🇯🇵 **Japanese (日本語)** — Wikipedia + AI
- 🇨🇳 **Chinese (中文)** — Wikipedia + AI

**Note:** Language selection affects Wikipedia content and AI-generated summaries. Taxonomic data remains in scientific nomenclature.

---

## 📦 What's Included

### Notebook Structure

1. **Introduction** — Overview and language selection
2. **Data Source Descriptions** — Detailed API documentation
3. **Library Installation** — All dependencies
4. **Configuration UI** — Interactive species input
5. **Helper Functions** — API wrappers and utilities
6. **Data Fetching Functions** — Source-specific retrievers
7. **Main Execution** — Data collection workflow
8. **Results Display** — Formatted plant card
9. **AI Summary Generation** — Gemini integration
10. **Image Selection** — Wikimedia image retrieval
11. **Export Options** — HTML/JSON output
12. **Citations** — Data source attribution

### Generated Data Fields

**Taxonomy:**
- Scientific name
- Kingdom, Family, Genus, Species
- Common names (multiple languages)
- Synonyms
- Taxonomic status

**Physical Characteristics:**
- Growth form (tree, shrub, herb)
- Average height and spread
- Growth rate
- Foliage type (deciduous/evergreen)

**Care Requirements:**
- Light needs (full sun to shade)
- Water requirements
- Temperature range
- Soil pH preference
- Hardiness zones

**Additional Information:**
- Distribution and native range
- Conservation status
- Toxicity warnings
- Cultural significance
- Historical uses

---

## 🚀 Getting Started

### Quick Start

1. **Open in Colab** — Click badge above
2. **Run installation cell** — Install dependencies
3. **Enter species name** — Use interactive widget
4. **Select language** — Choose preferred language
5. **Add API keys** — (Optional) Gemini, Trefle, BHL
6. **Save configuration** — Click save button
7. **Execute data collection** — Run the main cell
8. **View results** — Beautiful formatted output

### API Key Setup

#### Required for Full Features
- **Google Gemini** — [Get key](https://aistudio.google.com/app/apikey)
  - AI-powered summaries
  - Multi-language generation
  - Free tier available

- **Trefle** — [Get key](https://trefle.io)
  - Growth characteristics
  - Care requirements
  - Free for non-commercial

#### Optional
- **Laji.fi** — [Get key](https://laji.fi/en/about/13)
  - Finnish species names
  - Free registration

- **BHL** — [Get key](https://www.biodiversitylibrary.org/api2/docs/)
  - Historical illustrations
  - Free registration

#### No Key Required
- GBIF
- Wikipedia
- Wikimedia Commons
- iNaturalist
- EOL

**Storing keys in Colab:**
1. Click 🔑 **Secrets** in sidebar
2. Add key name (e.g., `GEMINI_API_KEY`)
3. Paste key value
4. Toggle "Notebook access" ON

---

## 💡 Usage Examples

### Example 1: Simple Query
```python
# Just enter species name
species_name = "Rosa canina"
# Run data collection
# Get basic information from free sources
```

**Output:**
- Taxonomy from GBIF
- Wikipedia summary
- Wikimedia image
- iNaturalist observations

### Example 2: Full Query with AI
```python
# With Gemini API key
species_name = "Quercus robur"
language = "en"
# Get AI-generated summary
# Professional quality description
```

**Output:**
- All basic data
- AI-powered comprehensive summary
- Growth characteristics (if Trefle key)
- Multiple image options

### Example 3: Multi-language
```python
# Generate in Finnish
species_name = "Betula pendula"
language = "fi"
# Wikipedia summary in Finnish
# AI summary in Finnish
```

**Output:**
- Finnish Wikipedia content
- AI summary in Finnish
- Finnish common names (if Laji.fi key)
- Scientific names (always Latin)

---

## 📊 Data Quality

### Validation Process

1. **Primary verification** — GBIF taxonomy check
2. **Cross-reference** — Compare multiple sources
3. **Consistency** — Flag contradictions
4. **Completeness** — Track data coverage
5. **Attribution** — Source tracking

### Quality Indicators

| Indicator | Description | Score |
|-----------|-------------|-------|
| **Taxonomy verified** | GBIF confirmation | High |
| **Multiple sources** | 3+ sources agree | High |
| **Recent data** | Updated within year | Medium |
| **Single source** | Only one source | Low |
| **No verification** | Unconfirmed | Very Low |

### Known Limitations

⚠️ **Important notes:**
- Wikipedia content is not peer-reviewed
- AI summaries should be verified
- Common names vary by region
- Care requirements are general guidelines
- Always consult expert sources for critical decisions

---

## 🎨 Output Formats

### HTML Card
Beautiful, printable plant card:
- Header with scientific name
- Photo (if available)
- Formatted sections
- Color-coded care icons
- Citations

### JSON Export
Machine-readable data:
```json
{
  "scientificName": "Rosa canina",
  "commonNames": ["Dog Rose", "Wild Rose"],
  "family": "Rosaceae",
  "taxonomy": {...},
  "characteristics": {...},
  "care": {...},
  "sources": [...]
}
```

### Markdown
Documentation format:
```markdown
# Rosa canina (Dog Rose)

## Taxonomy
**Family:** Rosaceae
**Genus:** Rosa

## Description
[AI-generated or Wikipedia summary]

## Care Requirements
- **Light:** Full sun to partial shade
- **Water:** Moderate
```

---

## 🔧 Advanced Features

### Custom Data Sources

Add your own data sources:

```python
def fetch_custom_source(species_name: str) -> Optional[Dict]:
    """Fetch from custom API"""
    url = "https://your-api.com/species"
    params = {"name": species_name}
    return safe_api_call(url, params)

# Integrate into workflow
custom_data = fetch_custom_source(species_name)
```

### Batch Processing

Generate cards for multiple species:

```python
species_list = [
    "Rosa canina",
    "Quercus robur", 
    "Betula pendula"
]

for species in species_list:
    # Generate card
    # Export to file
    # Add delay for rate limits
```

See also: [Batch Plant Cards](Examples-Batch-Plant-Cards) notebook

### Image Selection Algorithm

Automated quality scoring:
```python
score = (
    resolution_points +      # Higher resolution
    title_relevance +        # Filename matches species
    aspect_ratio_points +    # Good proportions
    file_size_reasonable     # Not too large/small
)
```

---

## 📖 Code Examples

### Safe API Call
```python
def safe_api_call(
    url: str,
    params: Optional[Dict[str, Any]] = None,
    timeout: int = 15
) -> Optional[Dict[str, Any]]:
    """
    Makes HTTP request with error handling.
    
    Handles:
    - Timeouts
    - HTTP errors
    - JSON parsing errors
    - Network issues
    """
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
```

### AI Summary Generation
```python
def generate_ai_summary(
    species_data: Dict[str, Any],
    language: str = "en"
) -> Optional[str]:
    """
    Generate AI summary using Gemini.
    
    Combines data from multiple sources
    into coherent description.
    """
    prompt = f"""
    Create a concise botanical summary for {species_data['name']}.
    Include: description, habitat, uses.
    Language: {language}
    Format: 2-3 paragraphs, professional tone.
    """
    
    response = gemini.generate_content(prompt)
    return response.text
```

---

## 🐛 Troubleshooting

### Common Issues

**No data returned:**
- ✅ Check species name spelling
- ✅ Try scientific name instead of common
- ✅ Verify internet connection
- ✅ Check if species exists in GBIF

**API errors:**
- ✅ Verify API keys in Colab Secrets
- ✅ Check key hasn't expired
- ✅ Respect rate limits (add delays)
- ✅ Try again later (temporary outage)

**Images not loading:**
- ✅ Wikimedia may have copyright restrictions
- ✅ Try different species
- ✅ Check image URL validity
- ✅ Some species have limited photography

**AI summary fails:**
- ✅ Ensure Gemini API key is valid
- ✅ Check quota hasn't been exceeded
- ✅ Verify data is complete enough
- ✅ Try simpler prompt

---

## 📚 Related Resources

### Documentation
- [GBIF API Docs](https://www.gbif.org/developer/species)
- [Trefle API Docs](https://docs.trefle.io)
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)
- [Gemini API](https://ai.google.dev/docs)

### Related Notebooks
- [Batch Plant Cards](Examples-Batch-Plant-Cards) — Process multiple species
- [Data Analysis Template](TEMPLATE-Data-Analysis) — Analyze plant data
- [MyST Scientific Template](TEMPLATE-MyST-Scientific) — Document findings

### External Tools
- [GBIF Portal](https://www.gbif.org) — Browse species
- [Plants of the World Online](http://www.plantsoftheworldonline.org) — Kew Gardens database
- [The Plant List](http://www.theplantlist.org) — Species names

---

## 📄 License & Attribution

**Code:** MIT License — Free to use

**Data sources:** Individual licenses apply
- GBIF: CC0 / CC-BY
- Wikipedia: CC-BY-SA
- Wikimedia: Varies by image
- Trefle: Custom (check terms)

**Citation:**
```bibtex
@software{plant_card_generator_2025,
  author = {Sihvonen, Pekka},
  title = {Plant Card Generator - Botanical Colabs},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/outobecca/botanical-colabs}
}
```

---

## 🤝 Contributing

Improve the Plant Card Generator!

- 🔗 Add new data sources
- 🌐 Add more languages
- 🎨 Improve card designs
- 🐛 Report bugs
- 💡 Suggest features

[Submit Issues](https://github.com/outobecca/botanical-colabs/issues) | [Pull Requests](https://github.com/outobecca/botanical-colabs/pulls)

---

**Created:** 2024-06-15  
**Updated:** 2025-11-04  
**Version:** 1.2 (Multilingual)  
**Status:** ✅ Production Ready

[← Back to Examples](Home#-examples) | [View on GitHub](https://github.com/outobecca/botanical-colabs/blob/main/notebooks/examples/generator-plant-card.ipynb)
