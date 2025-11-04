# 📚 Botanical Sciences Notebooks

This directory contains Jupyter/Colab notebooks for botanical and horticultural research, organized by category.

## 📁 Directory Structure

```
notebooks/
├── templates/          # Notebook templates for different workflows
├── agrology/           # Field crop and soil science
├── greenhouse/         # Protected cultivation management  
├── regional/           # Region-specific analysis
├── education/          # Learning and training materials
└── examples/           # Example implementations
```

## 📐 Categories

### [templates/](templates/)
**Purpose:** Starting point templates for different scientific workflows

Specialized templates pre-configured with:
- Common imports and dependencies
- Helper functions for specific domains
- Sample data generators
- Standard analysis structures

**When to use:** Copy a template when starting a new analysis in that domain.

---

### [agrology/](agrology/)
**Purpose:** Field crop and soil science analysis

Focus areas:
- Soil health monitoring (pH, nutrients, organic matter)
- Environmental sensor data analysis
- Resource management
- Sustainability metrics

**Applications:** Open-field agriculture, soil conservation, precision farming

---

### [greenhouse/](greenhouse/)
**Purpose:** Protected cultivation and greenhouse management

Focus areas:
- Yield prediction models
- Climate control optimization
- Growth monitoring
- Data visualization

**Applications:** Greenhouse operations, controlled environment agriculture, hydro ponics

---

### [regional/](regional/)
**Purpose:** Region-specific horticultural analysis

Focus areas:
- Local weather data integration
- Regional growing seasons
- Climate-specific challenges
- Local data source APIs

**Applications:** Location-specific planning, regional adaptation strategies

**Current regions:** Finland (FMI weather data)

---

### [education/](education/)
**Purpose:** Learning and training materials

Focus areas:
- Python programming basics
- Data science fundamentals
- Statistical analysis
- Machine learning introduction

**Target audience:** Students, professionals new to data science, self-learners

---

### [examples/](examples/)
**Purpose:** Complete working examples and demonstrations

Focus areas:
- Multi-source data aggregation
- API integration examples
- Production-ready workflows

**Use cases:** Reference implementations, learning by example

---

## 🚀 Getting Started

### For Beginners
1. Start with [education/education_tutorial.ipynb](education/education_tutorial.ipynb)
2. Try example notebooks in [examples/](examples/)
3. Experiment with your own data using templates

### For Researchers
1. Choose a template from [templates/](templates/) matching your workflow
2. Copy and customize for your specific research
3. Or browse category-specific notebooks for your field

### For Different Applications

**Field Agriculture?** → Start with [agrology/](agrology/)
- Soil analysis
- Environmental monitoring
- Sustainability tracking

**Greenhouse Operations?** → Start with [greenhouse/](greenhouse/)
- Yield prediction
- Climate optimization
- Growth visualization

**Local/Regional Focus?** → Check [regional/](regional/)
- Weather data integration
- Local climate analysis
- Region-specific recommendations

## 📖 Using the Notebooks

### In Google Colab (Recommended)
1. Click any "Open in Colab" badge in the category READMEs
2. No installation needed - runs in your browser
3. Save a copy to your Google Drive to keep changes

### Locally
```bash
# Clone the repository
git clone https://github.com/outobecca/botanical-colabs.git
cd botanical-colabs

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook notebooks/
```

## 🤝 Contributing

### Adding a New Notebook
1. Choose the appropriate category (or propose a new one)
2. Use the relevant template from [templates/](templates/)
3. Follow the [CONTRIBUTING.md](../CONTRIBUTING.md) guidelines
4. Update the category's README.md
5. Submit a pull request

### Proposing a New Category
1. Open an issue explaining the need
2. Provide examples of notebooks that would fit
3. Suggest organization structure
4. Wait for community feedback

## 📝 Naming Conventions

- Templates: `TEMPLATE_<purpose>.ipynb`
- Analysis notebooks: `<descriptive_name>.ipynb`
- Use underscores for spaces: `data_analysis.ipynb`
- Use lowercase for file names
- Include version in README if multiple versions exist

## 🔍 Finding Notebooks

**By Task:**
- Data cleaning/exploration → `agrology/data_analysis_exploration.ipynb`
- Visualization → `greenhouse/data_visualization.ipynb`
- ML/Prediction → `greenhouse/ml_yield_prediction.ipynb`
- Learning Python → `education/education_tutorial.ipynb`

**By Data Source:**
- FMI weather data → `regional/finnish_weather_analysis.ipynb`
- Biodiversity databases → `examples/generator-plant-card.ipynb`

**By Field:**
- Soil science → `agrology/`
- Greenhouse management → `greenhouse/`
- Education → `education/`

## 📚 Additional Resources

- [Repository README](../README.md) - Main documentation
- [Template Guide](../TEMPLATE_GUIDE.md) - How to use templates
- [API Setup](../API_SETUP.md) - Configure API keys
- [Contributing](../CONTRIBUTING.md) - Contribution guidelines

---

**Questions?** Open an issue or check [Discussions](https://github.com/outobecca/botanical-colabs/discussions)

**Happy researching! 🌱📊**
