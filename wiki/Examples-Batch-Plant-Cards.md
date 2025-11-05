# 📦 Batch Plant Cards

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/examples/batch-plant-cards.ipynb)

> **Process multiple species simultaneously with progress tracking and automated exports**

---

## 📋 Overview

The Batch Plant Cards notebook extends the [Plant Card Generator](Examples-Plant-Card-Generator) to handle **bulk processing** of multiple species. Perfect for creating comprehensive plant databases, field guides, or nursery catalogs with hundreds or thousands of species.

### Key Capabilities
- 📊 **CSV file upload** — Process species lists from spreadsheets
- 📈 **Progress tracking** — Real-time progress bars with tqdm
- 🔄 **Error handling** — Continue processing even if individual species fail
- 💾 **Multiple exports** — CSV, JSON, and HTML formats
- 📉 **Results analysis** — Statistical summaries and family distribution
- ⏸️ **Rate limiting** — Configurable delays to respect API limits

---

## 🎯 Use Cases

### Large-Scale Projects
- ✅ **Field guide creation** — Process 100+ species for regional guides
- ✅ **Nursery catalogs** — Generate descriptions for entire inventory
- ✅ **Research databases** — Build comprehensive species databases
- ✅ **Conservation projects** — Document endangered species lists
- ✅ **Educational materials** — Create classroom resources

### Data Management
- ✅ **Database migration** — Convert species lists to structured data
- ✅ **Quality assurance** — Batch validate species information
- ✅ **Data enrichment** — Add details to existing species lists
- ✅ **Format conversion** — CSV to JSON/HTML conversion
- ✅ **Automated updates** — Refresh species data periodically

---

## ⭐ Key Features

### CSV File Upload

**Interactive file upload:**
```python
# Upload your CSV file
csv_upload = widgets.FileUpload(
    accept='.csv',
    description='Upload CSV'
)
```

**Required CSV format:**
```csv
species_name
Rosa canina
Quercus robur
Betula pendula
Pinus sylvestris
```

**Optional columns:**
- `common_name` — Display name
- `priority` — Processing order
- `notes` — Internal comments

### Progress Tracking

**Real-time progress bar:**
```python
from tqdm.notebook import tqdm

for species in tqdm(species_list):
    # Process each species
    # Update progress automatically
```

**Features:**
- Estimated time remaining
- Processing speed (species/second)
- Current species name
- Success/failure counts

### Error Handling

**Robust failure management:**
```python
failed_species = []

for species in species_list:
    try:
        result = process_species(species)
        successful.append(result)
    except Exception as e:
        failed_species.append({
            'species': species,
            'error': str(e)
        })
        # Continue with next species
```

**Failed species log:**
- Species name
- Error message
- Timestamp
- Retry capability

### Multiple Export Formats

#### CSV Export
```python
# Export to CSV
df.to_csv('plant_cards_export.csv', index=False)
```

**Includes:**
- All fetched data fields
- Timestamps
- Source attribution
- Data quality indicators

#### JSON Export
```python
# Export to JSON
json_data = df.to_json(orient='records', indent=2)
```

**Structure:**
```json
[
  {
    "scientificName": "Rosa canina",
    "family": "Rosaceae",
    "commonNames": ["Dog Rose"],
    "characteristics": {...},
    "sources": [...]
  }
]
```

#### HTML Export
```python
# Export to styled HTML
html = df.to_html(
    classes='plant-table',
    escape=False
)
```

**Features:**
- Professional styling
- Sortable columns
- Responsive design
- Print-friendly

### Results Analysis

**Statistical summary:**
```python
# Summary statistics
total_species = len(results)
success_rate = len(successful) / total_species
avg_processing_time = total_time / total_species

# Family distribution
family_counts = df['family'].value_counts()
```

**Visualizations:**
- Family distribution bar chart
- Success/failure pie chart
- Processing time histogram
- Data completeness heatmap

---

## 📦 What's Included

### Notebook Structure

1. **Introduction** — Batch processing overview
2. **Installation** — Required libraries (requests, pandas, tqdm, openpyxl)
3. **Configuration UI** — Interactive widgets for settings
4. **Data Input** — CSV upload and manual entry
5. **Helper Functions** — API wrappers and utilities
6. **Batch Processing Engine** — Main processing loop
7. **Progress Monitoring** — Real-time status updates
8. **Error Logging** — Failed species tracking
9. **Results Analysis** — Statistical summaries
10. **Data Visualization** — Charts and graphs
11. **Export Functions** — Multiple format exports
12. **Retry Mechanism** — Re-process failed species

### Processing Functions

```python
def process_species(
    species_name: str,
    language: str = 'en',
    api_keys: Dict[str, str] = None
) -> Dict[str, Any]:
    """
    Process a single species.
    
    Returns:
        Dictionary with all collected data
    """
    
def run_batch_processing(
    species_list: List[str],
    delay: float = 1.0,
    language: str = 'en'
) -> Tuple[List[Dict], List[Dict]]:
    """
    Process multiple species with progress tracking.
    
    Returns:
        Tuple of (successful_results, failed_species)
    """
```

---

## 🚀 Getting Started

### Method 1: CSV Upload (Recommended)

1. **Prepare CSV file:**
   ```csv
   species_name
   Rosa canina
   Quercus robur
   Betula pendula
   ```

2. **Open in Colab** — Click badge above

3. **Upload CSV:**
   - Click "Choose Files" button
   - Select your CSV file
   - Wait for upload confirmation

4. **Configure settings:**
   - Select language
   - Set delay between requests
   - Choose export formats

5. **Start processing:**
   - Click "Start Batch Processing"
   - Monitor progress bar
   - Wait for completion

6. **Download results:**
   - CSV export button
   - JSON export button
   - HTML export button

### Method 2: Manual Entry

1. **Enter species list:**
   ```python
   species_list = [
       "Rosa canina",
       "Quercus robur",
       "Betula pendula",
       # ... add more
   ]
   ```

2. **Configure and run:**
   ```python
   results = run_batch_processing(
       species_list,
       delay=1.0,
       language='en'
   )
   ```

3. **Export results:**
   ```python
   save_to_csv(results, 'output.csv')
   save_to_json(results, 'output.json')
   ```

---

## 💡 Usage Examples

### Example 1: Small Batch (10-50 species)

```python
# Quick processing for small lists
species_list = [
    "Rosa canina",
    "Quercus robur",
    "Betula pendula",
    # ... 10 species total
]

# Fast processing (0.5s delay)
results, failed = run_batch_processing(
    species_list,
    delay=0.5,
    language='en'
)

# Quick export
export_to_csv(results)
```

**Estimated time:** 1-2 minutes

### Example 2: Medium Batch (50-200 species)

```python
# Upload CSV with 100 species
# Set delay to 1.0 seconds
# Process with progress tracking

# Estimated time: 5-10 minutes
```

**Features to use:**
- CSV upload
- Progress monitoring
- Error logging
- Batch export

### Example 3: Large Batch (200+ species)

```python
# Upload CSV with 500 species
# Set delay to 2.0 seconds (respect API limits)
# Enable retry for failed species

# Estimated time: 20-30 minutes
```

**Recommendations:**
- Run during off-peak hours
- Save intermediate results
- Monitor failed species
- Retry failures separately

### Example 4: Multi-language Database

```python
# Process in multiple languages
languages = ['en', 'fi', 'sv', 'de']

for lang in languages:
    results = run_batch_processing(
        species_list,
        language=lang,
        delay=1.5
    )
    export_to_csv(results, f'plants_{lang}.csv')
```

**Creates:**
- plants_en.csv
- plants_fi.csv
- plants_sv.csv
- plants_de.csv

---

## 📊 Performance

### Processing Speed

| Batch Size | Delay | Est. Time | Memory |
|------------|-------|-----------|--------|
| 10 species | 0.5s | 1 min | <50MB |
| 50 species | 1.0s | 3-5 min | <100MB |
| 100 species | 1.0s | 5-10 min | <200MB |
| 500 species | 2.0s | 20-30 min | <500MB |
| 1000 species | 2.0s | 40-60 min | <1GB |

### Optimization Tips

**Speed up processing:**
- ✅ Use lower delays for free APIs (0.5-1.0s)
- ✅ Process in parallel (advanced)
- ✅ Skip optional data sources
- ✅ Cache API responses

**Reduce failures:**
- ✅ Validate species names first
- ✅ Use higher delays for stability
- ✅ Implement retry logic
- ✅ Handle timeouts gracefully

**Save resources:**
- ✅ Export periodically (every 100 species)
- ✅ Clear outputs between batches
- ✅ Use Colab Pro for longer runtime
- ✅ Split into smaller batches

---

## 🔧 Advanced Features

### Automatic Retry

```python
# Retry failed species with longer delay
if failed_species:
    print(f"Retrying {len(failed_species)} failed species...")
    
    retry_results, still_failed = run_batch_processing(
        [s['species'] for s in failed_species],
        delay=3.0,  # Longer delay
        language=language
    )
    
    # Combine with successful results
    all_results.extend(retry_results)
```

### Progress Checkpoint

```python
# Save progress every 50 species
checkpoint_interval = 50

for i, species in enumerate(species_list):
    result = process_species(species)
    results.append(result)
    
    if (i + 1) % checkpoint_interval == 0:
        save_checkpoint(results, f'checkpoint_{i+1}.csv')
```

### Custom Data Sources

```python
# Add custom data source to batch processing
def process_species_with_custom(species_name: str) -> Dict:
    # Standard processing
    data = process_species(species_name)
    
    # Add custom source
    custom_data = fetch_custom_api(species_name)
    data['custom'] = custom_data
    
    return data
```

### Parallel Processing

```python
from concurrent.futures import ThreadPoolExecutor

def parallel_batch_processing(species_list: List[str]) -> List[Dict]:
    """
    Process multiple species in parallel.
    Use with caution - respect API rate limits!
    """
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_species, species_list))
    return results
```

---

## 📈 Results Analysis

### Statistical Summary

```python
# Generate summary
summary = {
    'total_species': len(results),
    'successful': len(successful),
    'failed': len(failed),
    'success_rate': len(successful) / len(results),
    'families': df['family'].nunique(),
    'avg_processing_time': total_time / len(results)
}
```

### Family Distribution

```python
# Analyze family distribution
family_counts = df['family'].value_counts()

# Visualize
plt.figure(figsize=(12, 6))
family_counts.head(10).plot(kind='bar')
plt.title('Top 10 Plant Families')
plt.xlabel('Family')
plt.ylabel('Number of Species')
```

### Data Completeness

```python
# Check data completeness
completeness = {
    'has_description': df['description'].notna().sum(),
    'has_image': df['image_url'].notna().sum(),
    'has_care_info': df['care'].notna().sum(),
    'complete_records': df.notna().all(axis=1).sum()
}

# Completeness percentage
for key, value in completeness.items():
    pct = (value / len(df)) * 100
    print(f"{key}: {pct:.1f}%")
```

---

## 🐛 Troubleshooting

### Common Issues

**CSV upload fails:**
- ✅ Check file format (UTF-8 encoding)
- ✅ Verify column name is "species_name"
- ✅ Remove empty rows
- ✅ Check for special characters

**Many species fail:**
- ✅ Verify species names are correct
- ✅ Increase delay between requests
- ✅ Check API keys are valid
- ✅ Retry failed species separately

**Processing too slow:**
- ✅ Reduce delay (if allowed by APIs)
- ✅ Skip optional data sources
- ✅ Process in smaller batches
- ✅ Use Colab Pro for faster runtime

**Memory errors:**
- ✅ Process in smaller batches
- ✅ Clear outputs periodically
- ✅ Export and restart for large datasets
- ✅ Use Colab Pro for more RAM

**Export fails:**
- ✅ Check file permissions
- ✅ Verify data format
- ✅ Try different export format
- ✅ Download in chunks

---

## 📚 Related Resources

### Documentation
- [Plant Card Generator](Examples-Plant-Card-Generator) — Single species processing
- [Data Analysis Template](TEMPLATE-Data-Analysis) — Analyze exported data
- [API Setup Guide](https://github.com/outobecca/botanical-colabs/blob/main/API_SETUP.md)

### Data Sources
- [GBIF Backbone Taxonomy](https://www.gbif.org/dataset/d7dddbf4-2cf0-4f39-9b2a-bb099caae36c)
- [The Plant List](http://www.theplantlist.org) — Verify species names
- [World Flora Online](http://www.worldfloraonline.org) — Taxonomic validation

### Tools
- [OpenRefine](https://openrefine.org) — Clean species lists
- [Python pandas](https://pandas.pydata.org) — Data manipulation
- [tqdm](https://tqdm.github.io) — Progress bars

---

## 📄 License

MIT License — Free to use, modify, and distribute

**Citation:**
```bibtex
@software{batch_plant_cards_2025,
  author = {Sihvonen, Pekka},
  title = {Batch Plant Cards - Botanical Colabs},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/outobecca/botanical-colabs}
}
```

---

## 🤝 Contributing

Improve batch processing!

- 🚀 Add parallel processing
- 💾 Improve caching
- 📊 Better analytics
- 🐛 Report bugs
- 💡 Suggest features

[Submit Issues](https://github.com/outobecca/botanical-colabs/issues) | [Pull Requests](https://github.com/outobecca/botanical-colabs/pulls)

---

**Created:** 2025-11-04  
**Version:** 1.0  
**Status:** ✅ Production Ready

[← Back to Examples](Home#-examples) | [View on GitHub](https://github.com/outobecca/botanical-colabs/blob/main/notebooks/examples/batch-plant-cards.ipynb)
