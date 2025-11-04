# 📋 Notebook Template Usage Guide

This guide explains how to use `TEMPLATE_botanical_notebook.ipynb` to create new botanical science notebooks that follow repository standards.

## 🎯 Template Purpose

The template provides a standardized structure for creating reproducible, well-documented, and maintainable Jupyter/Colab notebooks for botanical research. It enforces:

- **Consistent organization** — 6-step structure used across all notebooks
- **Best practices** — Error handling, type hints, docstrings, citations
- **Reproducibility** — Colab Secrets, dependency installation, clear documentation
- **Scientific rigor** — Data provenance, citation tracking, methodology documentation

## 🏗️ Template Structure

### Overview

The template follows a **6-step structure**:

```
1. Installation & Configuration
   ↓
2. Helper Functions
   ↓
3. Data Fetching Functions
   ↓
4. Execute Data Collection
   ↓
5. Data Analysis & Visualization
   ↓
6. Citations & Documentation
```

### Detailed Breakdown

#### **Step 1: Installation & Configuration**
- **Purpose:** Install dependencies, import libraries, configure user settings
- **Components:**
  - Library installation (`!pip install`)
  - Standard imports (requests, pandas, numpy, matplotlib, etc.)
  - Colab environment detection
  - Interactive widgets (text input, dropdowns, checkboxes)
  - API key retrieval from Colab Secrets
  - Settings save button

**Customize:**
- Add your required packages to `!pip install`
- Create UI widgets for your analysis parameters
- Add API key retrieval for your data sources
- Update `update_settings()` function with your variables

#### **Step 2: Helper Functions**
- **Purpose:** Reusable utility functions for data handling
- **Included Functions:**
  - `safe_api_call()` — Safe HTTP requests with error handling
  - `validate_input()` — Input validation
  - `format_data_for_display()` — DataFrame formatting
  - `create_citation()` — Citation generation

**Customize:**
- Add domain-specific validation functions
- Create data transformation utilities
- Add statistical or mathematical helpers
- Include format converters (units, coordinates, etc.)

#### **Step 3: Data Fetching Functions**
- **Purpose:** API calls and data retrieval
- **Pattern:**
  ```python
  def fetch_source_data(query: str, api_key: str = None) -> Optional[Dict[str, Any]]:
      """Fetches data from [Source Name]."""
      # API call logic
      # Error handling
      # Data parsing
      return result
  ```

**Customize:**
- Replace `fetch_example_data()` with your actual API functions
- Add one function per data source
- Include comprehensive docstrings with source info, license, URL
- Use `safe_api_call()` for all HTTP requests

#### **Step 4: Execute Data Collection**
- **Purpose:** Orchestrate data fetching from all sources
- **Pattern:**
  - Validate input
  - Fetch from each enabled source
  - Compile results
  - Create summary DataFrame

**Customize:**
- Add calls to your data fetching functions
- Implement conditional fetching based on settings
- Add progress indicators for long operations
- Create result aggregation logic

#### **Step 5: Data Analysis & Visualization**
- **Purpose:** Analyze and display results
- **Included:**
  - Formatted data tables
  - Example matplotlib/seaborn plots
  - Statistical summaries
  - Key findings section

**Customize:**
- Replace example plots with your visualizations
- Add statistical tests or calculations
- Create interactive plots (plotly, bokeh)
- Add export functionality (CSV, JSON, images)

#### **Step 6: Citations & Documentation**
- **Purpose:** Document data sources and create citations
- **Components:**
  - Data source citations
  - Query timestamp
  - Notebook citation template

**Customize:**
- Update `create_citation()` with your data sources
- Add specific license information
- Include methodology references

## 🚀 Quick Start: Using the Template

### 1. Copy the Template

```powershell
# In your repository
cp notebooks/TEMPLATE_botanical_notebook.ipynb notebooks/my-new-analysis.ipynb
```

Or in Colab:
1. Open `TEMPLATE_botanical_notebook.ipynb`
2. File → Save a copy in Drive
3. Rename to your notebook name

### 2. Update Header Section

Edit the first markdown cell:

```markdown
# 🌿 [Your Notebook Title]
**Version 1.0** | Created: 2025-11-04 | Author: Your Name

## 📋 Overview

**Purpose:** [What does this notebook do?]

**Research Question/Goal:** [What problem does it solve?]
```

Update:
- Title
- Date
- Author
- Purpose statement
- Research question
- Use cases
- Data sources table
- Required API keys

### 3. Configure Step 1: Installation

**Update library installation:**
```python
# Add your required packages
!pip install -q requests pandas your-package another-package
```

**Create UI widgets:**
```python
# Example: Scientific name input
scientific_name_widget = widgets.Text(
    value="",
    placeholder="e.g., Quercus robur",
    description="🌱 Species:",
    layout=widgets.Layout(width='500px')
)

# Example: Dropdown menu
analysis_type_widget = widgets.Dropdown(
    options=['Analysis A', 'Analysis B', 'Analysis C'],
    value='Analysis A',
    description='Type:',
)
```

**Add your global variables:**
```python
# Global variables
scientific_name: str = ""
analysis_type: str = ""
YOUR_API_KEY: str = ""
```

**Update `update_settings()` function:**
```python
def update_settings(_=None) -> None:
    global scientific_name, analysis_type, YOUR_API_KEY
    
    scientific_name = scientific_name_widget.value.strip()
    analysis_type = analysis_type_widget.value
    
    # Fetch API keys
    YOUR_API_KEY = get_api_key('YOUR_API_KEY_NAME')
    
    # Status output
    with status_output:
        status_output.clear_output()
        print(f"✅ Settings updated: {scientific_name}")
        print(f"API Key: {'✓ Set' if YOUR_API_KEY else '✗ Missing'}")
```

### 4. Add Helper Functions (Step 2)

Add domain-specific helpers:

```python
def validate_scientific_name(name: str) -> bool:
    """Validates binomial nomenclature format."""
    parts = name.strip().split()
    if len(parts) < 2:
        print("⚠️ Scientific name should have genus and species")
        return False
    return True

def convert_coordinates(lat: float, lon: float) -> Dict[str, str]:
    """Converts decimal coordinates to DMS format."""
    # Your conversion logic
    return {"latitude": lat_dms, "longitude": lon_dms}
```

### 5. Create Data Fetching Functions (Step 3)

Replace `fetch_example_data()` with your actual API functions:

```python
def fetch_gbif_data(scientific_name: str) -> Optional[Dict[str, Any]]:
    """
    Fetches species data from GBIF.
    
    Args:
        scientific_name: Binomial name (e.g., "Quercus robur")
    
    Returns:
        Dictionary with GBIF data or None
        
    Source:
        GBIF Backbone Taxonomy - https://www.gbif.org
        License: CC0 1.0
    """
    url = "https://api.gbif.org/v1/species/match"
    params = {"name": scientific_name}
    
    data = safe_api_call(url, params)
    
    if not data or data.get("matchType") == "NONE":
        print(f"❌ No GBIF match for: {scientific_name}")
        return None
    
    result = {
        "Kingdom": data.get("kingdom", "N/A"),
        "Family": data.get("family", "N/A"),
        "Genus": data.get("genus", "N/A"),
        "Species": data.get("species", "N/A"),
        "GBIF Key": data.get("usageKey", "N/A"),
    }
    
    print(f"✅ GBIF data retrieved")
    return result
```

Add multiple data source functions as needed.

### 6. Update Main Execution (Step 4)

Customize the data collection workflow:

```python
if not scientific_name:
    print("❌ ERROR: Enter species name in Step 1")
else:
    print(f"\\n📊 Analyzing: {scientific_name}")
    print("=" * 60)
    
    all_data = {}
    
    # Fetch from GBIF
    print("\\n📍 Fetching from GBIF...")
    gbif_data = fetch_gbif_data(scientific_name)
    if gbif_data:
        all_data.update(gbif_data)
    
    # Fetch from your other sources
    print("\\n📍 Fetching from Source 2...")
    source2_data = fetch_source2_data(scientific_name)
    if source2_data:
        all_data.update(source2_data)
    
    print("\\n" + "=" * 60)
    print("✅ Data collection complete!")
    
    # Create results DataFrame
    results_df = pd.DataFrame([
        {"Field": k, "Value": v} 
        for k, v in all_data.items() 
        if v and v != "N/A"
    ])
```

### 7. Create Visualizations (Step 5)

Replace example plots with your analysis:

```python
# Distribution map
fig, ax = plt.subplots(figsize=(12, 8))

# Plot occurrence points
ax.scatter(longitudes, latitudes, 
           alpha=0.6, c='forestgreen', 
           s=50, edgecolors='darkgreen')

ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.set_title(f'Distribution: {scientific_name}', 
             fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 8. Update Citations (Step 6)

Add your data source citations to `create_citation()`:

```python
def create_citation(source: str, date: str = None) -> str:
    """Creates a citation for a data source."""
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
    
    citations = {
        "GBIF": f"GBIF.org ({date}). GBIF Backbone Taxonomy. https://doi.org/10.15468/39omei",
        "Trefle": f"Trefle.io ({date}). Plant Species Database. https://trefle.io",
        "YourAPI": f"Your API Name ({date}). https://your-api.com",
    }
    
    return citations.get(source, f"{source} ({date})")
```

### 9. Update Footer Documentation

Edit the final markdown cell:

```markdown
## 📝 Notes and Best Practices

### ✅ Data Quality
- [Your data quality notes]

### 🔬 Scientific Use
- [Domain-specific best practices]

### 🐛 Troubleshooting
- [Common issues and solutions]

### 🔗 Useful Resources
- [Links to documentation]
```

### 10. Test Your Notebook

**In Google Colab:**
1. Runtime → Restart runtime
2. Runtime → Run all
3. Verify all cells execute without errors
4. Check data output and visualizations
5. Test with different input parameters

**Locally (optional):**
```powershell
jupyter nbconvert --to notebook --execute your-notebook.ipynb
```

## ✅ Checklist Before Submitting

Use this checklist before contributing your notebook:

- [ ] **Header updated** with title, date, author, purpose
- [ ] **Data sources documented** in table with licenses
- [ ] **Required API keys listed** with links to obtain them
- [ ] **All cells execute successfully** in Colab
- [ ] **Type hints added** to all function signatures
- [ ] **Docstrings written** for all functions (with Args, Returns, Source)
- [ ] **Error handling implemented** for API calls and data processing
- [ ] **Input validation** added for user parameters
- [ ] **Citations created** for all data sources used
- [ ] **Example output shown** (run with real data before submitting)
- [ ] **Comments added** explaining complex logic
- [ ] **Markdown headers** clearly separate sections
- [ ] **Visualizations labeled** with titles, axis labels, legends
- [ ] **Footer notes updated** with troubleshooting tips
- [ ] **README.md updated** to list your new notebook
- [ ] **CHANGELOG.md updated** with version and changes

## 📚 Code Style Guidelines

### Function Documentation

```python
def fetch_api_data(species: str, api_key: str = None) -> Optional[Dict[str, Any]]:
    """
    Fetches species data from API.
    
    Args:
        species: Scientific name in binomial format
        api_key: Optional API authentication key
    
    Returns:
        Dictionary with species data or None if not found
        
    Source:
        API Name - https://api.example.com
        License: CC-BY 4.0
        
    Example:
        >>> data = fetch_api_data("Quercus robur", api_key="xyz")
        >>> print(data['family'])
        'Fagaceae'
    """
    # Function implementation
```

### Error Handling Pattern

```python
def safe_operation(param: str) -> Optional[Any]:
    """Performs operation with comprehensive error handling."""
    try:
        # Main logic
        result = some_operation(param)
        
        if not result:
            print(f"⚠️ No results for: {param}")
            return None
            
        print(f"✅ Operation successful")
        return result
        
    except ValueError as e:
        print(f"❌ Invalid value: {str(e)}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {str(e)[:100]}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)[:100]}")
        return None
```

### Type Hints

```python
from typing import Dict, List, Optional, Any, Tuple

# Use type hints on all functions
def process_data(
    input_data: List[Dict[str, Any]], 
    threshold: float = 0.5
) -> Tuple[pd.DataFrame, int]:
    """Process and filter data."""
    # Implementation
    return dataframe, count

# Use Optional for nullable returns
def fetch_data(query: str) -> Optional[Dict[str, Any]]:
    """Fetches data, returns None if not found."""
    # Implementation
```

### Display Formatting

```python
# Use Markdown for headers and formatting
display(Markdown(f"# 📊 Analysis: **{species_name}**"))
display(Markdown("***"))  # Horizontal line

# Format DataFrames nicely
df_styled = results_df.style.hide(axis='index')
display(df_styled)

# Use HTML for complex formatting
display(HTML(f"""
<div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
    <h3>Summary</h3>
    <p>{summary_text}</p>
</div>
"""))
```

## 🔧 Advanced Customization

### Adding Custom Widgets

```python
# Slider for numeric input
threshold_widget = widgets.FloatSlider(
    value=0.5,
    min=0.0,
    max=1.0,
    step=0.1,
    description='Threshold:',
    readout_format='.1f',
)

# Multi-select
sources_widget = widgets.SelectMultiple(
    options=['Source A', 'Source B', 'Source C'],
    value=['Source A'],
    description='Data Sources:',
)

# Date picker
date_widget = widgets.DatePicker(
    description='Date:',
    value=datetime.now(),
)
```

### Progress Indicators

```python
from tqdm.notebook import tqdm

# For loops
for item in tqdm(items, desc="Processing"):
    process(item)

# Manual progress
progress = widgets.IntProgress(
    value=0,
    min=0,
    max=100,
    description='Loading:',
    bar_style='info'
)
display(progress)

for i in range(100):
    # Update progress
    progress.value = i + 1
```

### Conditional Outputs

```python
# Use ipywidgets Output for dynamic content
debug_output = widgets.Output()

with debug_output:
    if verbose:
        print("🔍 Debug information:")
        print(f"API response: {response}")

if show_debug:
    display(debug_output)
```

## 🌟 Examples from Repository

### Plant Card Generator Structure

See `generator-plant-card_en.ipynb` for a complete implementation:

- **Step 1:** Language selector, scientific name input, API keys, feature toggles
- **Step 2:** `safe_api_call()`, `validate_scientific_name()`, `format_data_for_display()`, `create_citation()`
- **Step 3:** 8 data fetching functions (GBIF, Trefle, Wikipedia, EOL, etc.)
- **Step 4:** Sequential data fetching with progress indicators
- **Step 5:** Formatted data tables, images, and plant card display
- **Step 6:** AI summary generation (optional), citations for all sources

## 🤝 Contributing

When contributing new notebooks:

1. **Use the template** as your starting point
2. **Follow the structure** (don't skip steps)
3. **Test in Colab** before submitting
4. **Document thoroughly** (docstrings, comments, markdown)
5. **Update README.md** to list your notebook
6. **Submit a PR** with clear description

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

## 📖 Additional Resources

- **Repository:** https://github.com/outobecca/botanical-colabs
- **API Setup:** [API_SETUP.md](API_SETUP.md)
- **Quick Start:** [QUICKSTART.md](QUICKSTART.md)
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Changelog:** [CHANGELOG.md](CHANGELOG.md)

---

**Questions?** Open an issue or discussion on GitHub!

**Happy coding!** 🌿🔬📊
