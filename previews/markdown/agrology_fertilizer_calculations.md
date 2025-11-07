
---
**📸 Preview Mode**  
This is a static snapshot generated with dummy data for demonstration purposes.

---

[//]: # ( Fertilizer Calculations with Crop-Specific Nutrient Needs )

[//]: # ( License: MIT License )

[//]: # ( Repository: https://github.com/pekka/botanical-colab-notebooks )

# 🌾 Fertilizer Calculations with Crop-Specific Nutrient Needs
**Version 1.1** | Updated: 2025-11-06 | Author: Botanical Colabs Team

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pekka/botanical-colab-notebooks/blob/main/notebooks/agrology/fertilizer_calculations.ipynb)

## 📋 Overview

**Purpose:** Calculate precise fertilizer requirements based on crop-specific nutrient needs, soil test results, and field characteristics.

**Research Question:** How can we optimize fertilizer application rates to meet crop nutrient demands while minimizing waste and environmental impact?

### 🎯 Use Cases
- Calculate NPK (Nitrogen, Phosphorus, Potassium) requirements for different crops
- Account for existing soil nutrients from soil tests
- Determine fertilizer product quantities needed
- Compare different fertilizer products and formulations
- Generate application recommendations by crop type
- Estimate costs and optimize fertilizer selection

### 🌱 Supported Crops

| Category | Crops | Nutrient Profile |
|----------|-------|------------------|
| **Vegetables** | Tomato, Lettuce, Pepper, Cucumber | High N, Moderate P-K |
| **Grains** | Corn, Wheat, Barley | Moderate-High N |
| **Legumes** | Soybean, Peas, Beans | Low N, Moderate P-K |
| **Root Crops** | Potato, Carrot, Beet | Moderate N, High K |

### ⚠️ Notes
- Values are general guidelines - adjust for local conditions
- Always perform soil tests for accurate recommendations
- Consider organic matter and previous crop history
- Follow local regulations for fertilizer application



```python

if 'PREVIEW_MODE' in os.environ:
    # Using dummy data for preview
    pass
else:
    
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
    

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[1], line 1
    ----> 1 if 'PREVIEW_MODE' in os.environ:
          2     # Using dummy data for preview
          3     pass
          4 else:
          5 
          6     # AUTO-INJECTED DUMMY DATA FOR PREVIEW GENERATION
    

    NameError: name 'os' is not defined


## 📚 Background & Methodology

### Scientific Context

Proper fertilizer management requires understanding:
- **Crop Nutrient Demands:** Different crops have varying NPK requirements at different growth stages
- **Soil Nutrient Supply:** Existing soil nutrients reduce fertilizer needs
- **Fertilizer Efficiency:** Not all applied nutrients are available to plants
- **Environmental Stewardship:** Precision application prevents nutrient runoff and pollution

### Nutrient Requirements

**Macronutrients (NPK):**
- **Nitrogen (N):** Promotes vegetative growth, leaf development, and protein synthesis
- **Phosphorus (P):** Essential for root development, flowering, and energy transfer
- **Potassium (K):** Improves disease resistance, water regulation, and fruit quality

### Methodology
1. **Crop Selection** - Choose crop and target yield
2. **Soil Testing** - Input existing soil nutrient levels
3. **Nutrient Budget** - Calculate crop needs minus soil supply
4. **Fertilizer Selection** - Choose appropriate product(s)
5. **Rate Calculation** - Determine application quantities
6. **Recommendations** - Generate application schedule

### Expected Outputs
- Nutrient requirement calculations by crop
- Fertilizer product recommendations
- Application rates (kg/ha or lb/acre)
- Cost estimates
- Comparative analysis of fertilizer options


## ⚙️ Step 1: Installation and Configuration

Run the cells below to install libraries and configure your analysis.



```python
# ============================================================================
# Library Installation and Import
# ============================================================================
"""
Installs required Python libraries.
Run this cell first.
"""

# Installation
!pip install -q pandas numpy matplotlib seaborn ipywidgets

# Core imports
import warnings

import ipywidgets as widgets
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import clear_output, display

warnings.filterwarnings("ignore")

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

print("✅ Libraries installed successfully")
```

    ✅ Libraries installed successfully
    


```python
# ============================================================================
# Interactive Configuration
# ============================================================================

crop_dropdown = widgets.Dropdown(
    options=list(CROP_NUTRIENT_DATABASE.keys()) + ["Custom"], description="Crop:"
)
field_area_input = widgets.FloatText(value=1.0, description="Field Area (ha):")
target_yield_input = widgets.FloatText(value=0, description="Target Yield (t/ha):")
soil_n_input = widgets.FloatText(value=40, description="Soil N (kg/ha):")
soil_p_input = widgets.FloatText(value=25, description="Soil P (kg/ha):")
soil_k_input = widgets.FloatText(value=150, description="Soil K (kg/ha):")
unit_dropdown = widgets.Dropdown(
    options=["Metric (kg/ha)", "Imperial (lb/acre)"], description="Units:"
)
run_button = widgets.Button(
    description="Calculate", button_style="success", icon="check"
)
output_area = widgets.Output()


def on_calculate_button_clicked(b):
    with output_area:
        clear_output()
        # ... (calculation logic) ...


run_button.on_click(on_calculate_button_clicked)

display(
    crop_dropdown,
    field_area_input,
    target_yield_input,
    soil_n_input,
    soil_p_input,
    soil_k_input,
    unit_dropdown,
    run_button,
    output_area,
)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[3], line 6
          1 # ============================================================================
          2 # Interactive Configuration
          3 # ============================================================================
          5 crop_dropdown = widgets.Dropdown(
    ----> 6     options=list(CROP_NUTRIENT_DATABASE.keys()) + ["Custom"], description="Crop:"
          7 )
          8 field_area_input = widgets.FloatText(value=1.0, description="Field Area (ha):")
          9 target_yield_input = widgets.FloatText(value=0, description="Target Yield (t/ha):")
    

    NameError: name 'CROP_NUTRIENT_DATABASE' is not defined


## 📓 Exporting the Notebook

You can export this notebook to different formats (HTML, PDF, etc.) using the provided `export.ps1` script.

**Prerequisites:**
- PowerShell (usually pre-installed on Windows)
- Python with `nbconvert` installed (`pip install nbconvert`)
- For PDF export: A LaTeX distribution like MiKTeX.

**Usage (from the `notebooks` directory):**

```powershell
# Export to HTML (default)
.\export.ps1 -NotebookFile .\agrology\fertilizer_calculations.ipynb

# Export to PDF
.\export.ps1 -NotebookFile .\agrology\fertilizer_calculations.ipynb -Format pdf

# Export to Slides
.\export.ps1 -NotebookFile .\agrology\fertilizer_calculations.ipynb -Format slides
```

The exported files will be saved in the same directory as the notebook.
