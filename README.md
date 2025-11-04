# Botanical Sciences Colab Notebooks

A collection of reproducible Jupyter/Colab notebooks for practical botanical, horticultural, and agricultural research — combining open data sources, simple data pipelines, and AI-assisted workflows.

This repository is focused on small, shareable notebooks that demonstrate useful analyses and tools for plant science, including plant identification, species factsheets, distribution summaries, and plant care card generation.

## Quick links
- 🌐 Repository: https://github.com/outobecca/botanical-colabs
- 🌍 GitHub Pages: https://outobecca.github.io/botanical-colabs/
- 📓 Notebooks: `notebooks/`
- 🔑 [API Setup Guide](API_SETUP.md)
- 🤝 [Contributing Guidelines](CONTRIBUTING.md)
- 📋 [Changelog](CHANGELOG.md)
- ⚖️ [License](LICENSE)
- 📄 [GitHub Pages Setup](GITHUB_PAGES.md)

## 📚 Notebook Organization

Notebooks are organized into categories for easy navigation:

- 📐 **[templates/](notebooks/templates/)** - Notebook templates for different scientific workflows
- 🌾 **[agrology/](notebooks/agrology/)** - Field crop and soil science notebooks  
- 🏗️ **[greenhouse/](notebooks/greenhouse/)** - Protected cultivation and greenhouse management
- 🗺️ **[regional/](notebooks/regional/)** - Region-specific horticultural analysis
- 🎓 **[education/](notebooks/education/)** - Learning and training materials
- 📋 **[examples/](notebooks/examples/)** - Example implementations and demonstrations

---

## 📐 Templates (notebooks/templates/)

Starting points for creating new notebooks in specific domains.

### `TEMPLATE_botanical_notebook.ipynb` — General Template
General-purpose template for botanical science notebooks.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_botanical_notebook.ipynb)

### `TEMPLATE_data_analysis.ipynb` — Data Analysis Template  
Pre-configured for environmental sensors, soil tests, and plant measurements.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_data_analysis.ipynb)

### `TEMPLATE_machine_learning.ipynb` — ML Template
Specialized for crop yield prediction and disease risk models.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_machine_learning.ipynb)

### `TEMPLATE_environmental_monitoring.ipynb` — Environmental Template
For soil health, water usage, and sustainability analysis.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_environmental_monitoring.ipynb)

---

## 🌾 Agrology (notebooks/agrology/)

Field crop and soil science analysis notebooks.

### `data_analysis_exploration.ipynb` — Data Analysis & Exploration
Interactive analysis of environmental sensors, soil tests, and plant measurements. Includes outlier detection, statistical summaries, and data cleaning.
[📖 Details](notebooks/agrology/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/agrology/data_analysis_exploration.ipynb)

### `environmental_management.ipynb` — Environmental & Resource Management
Analyze soil health, water usage, climate resilience, and resource consumption for sustainable agriculture.
[📖 Details](notebooks/agrology/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/agrology/environmental_management.ipynb)

---

## 🏗️ Greenhouse (notebooks/greenhouse/)

Protected cultivation and greenhouse management notebooks.

### `ml_yield_prediction.ipynb` — Crop Yield Prediction & ML
Machine learning models for predicting yield, disease risk, and optimal growing conditions. Includes Random Forest models and feature importance analysis.
[📖 Details](notebooks/greenhouse/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/greenhouse/ml_yield_prediction.ipynb)

### `data_visualization.ipynb` — Data Visualization
Create interactive visualizations for plant growth, environmental conditions, and greenhouse metrics using Matplotlib, Seaborn, and Plotly.
[📖 Details](notebooks/greenhouse/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/greenhouse/data_visualization.ipynb)

---

## 🗺️ Regional (notebooks/regional/)

Region-specific horticultural analysis with local data sources.

### `finnish_weather_analysis.ipynb` 🇫🇮 — Finnish Weather Analysis
Analyze Finnish weather data for horticulture using FMI (Ilmatieteen laitos) open data. Includes growing season analysis, frost risk, and GDD calculations. **Bilingual: Finnish/English**
[📖 Details](notebooks/regional/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/regional/finnish_weather_analysis.ipynb)

---

## 🎓 Education (notebooks/education/)

Learning and training materials for horticultural data science.

### `education_tutorial.ipynb` — Data Science Tutorial
Interactive learning environment for beginners. Covers Python basics, Pandas, visualization, statistics, and machine learning with horticultural examples. **No prior programming required!**
[📖 Details](notebooks/education/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/education/education_tutorial.ipynb)

---

## 📋 Examples (notebooks/examples/)

Example implementations and demonstrations.

### `generator-plant-card.ipynb` — Plant Card Generator
Multi-source plant information aggregator. Fetches data from GBIF, Trefle, Wikipedia, and more. **Supports 9 languages!**
[📖 Details](notebooks/examples/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/examples/generator-plant-card.ipynb)

---

## Features & goals
- Demonstrate reproducible data queries against biodiversity APIs.
- Create concise, printable plant care cards from aggregated data.
- Provide Colab-ready notebooks so researchers and hobbyists can run examples without local setup.

## Run the notebooks

Recommended: open notebooks in Google Colab (no local install needed):

1. Open the notebook file in the `notebooks/` folder.
2. Click "Open in Colab" or upload the notebook to Colab.
3. If a cell installs packages (e.g., `pip install requests pandas google-generativeai`), run it.

Local (optional): to run locally you'll need Python 3.8+ and some packages. Create a virtual env and install dependencies:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

If `requirements.txt` is not present, install minimal packages used by the starter notebook:

```powershell
pip install requests pandas ipywidgets pillow google-generativeai
```

## API keys & secrets

Some data sources require API keys or tokens. **See [API_SETUP.md](API_SETUP.md) for detailed instructions.**

**Quick start:**
1. Get free API keys from:
   - [Google Gemini](https://aistudio.google.com/app/apikey) — AI summaries
   - [Trefle](https://trefle.io) — Plant database
   - [Laji.fi](https://laji.fi/en/about/13) — Finnish names
2. In Colab: Click 🔑 Secrets → Add your keys
3. Run the notebook configuration cell

**Security:** Never commit API keys to Git. Use Colab Secrets or `.env` files (already in `.gitignore`).

## Privacy & license

- **License:** MIT License — see [LICENSE](LICENSE)
- **Data sources** have their own licenses (GBIF uses CC0/CC-BY, Wikimedia varies by image, etc.)
- **Always respect source licenses** when reusing data or images
- **AI-generated content** is not peer-reviewed and should be verified
- **No warranties:** Data is provided as-is from external sources

See [LICENSE](LICENSE) for detailed information about data source licenses.

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

**Ways to contribute:**
- 🆕 Add new notebooks (analysis, visualization, tutorials)
- 🐛 Fix bugs or improve existing notebooks
- 📖 Improve documentation
- 🔗 Integrate new data sources
- ✅ Add tests or validation

**Quick workflow:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following [contribution guidelines](CONTRIBUTING.md)
4. Test thoroughly (especially in Google Colab)
5. Submit a pull request with clear description

**Standards:**
- Use type hints and docstrings
- Cite all data sources
- Add error handling
- Test in Colab before submitting
- Follow existing code style

## Project roadmap

### Completed ✅
- ✅ Plant card generator with multi-source data aggregation
- ✅ Comprehensive documentation and type hints
- ✅ Error handling and validation
- ✅ Colab Secrets integration
- ✅ Scientific citations and provenance tracking
- ✅ Multilingual support (9 languages for Wikipedia and AI content)
- ✅ **Horticultural data analysis and exploration notebook**
- ✅ **Data visualization notebook (Matplotlib, Seaborn, Plotly)**
- ✅ **Machine learning crop yield prediction notebook**
- ✅ **Environmental and resource management notebook**
- ✅ **Education and training tutorial notebook**

### In progress 🚧
- 🚧 Batch processing for multiple species
- 🚧 Export to PDF/HTML

### Planned 📋
- 📋 Pest and disease identification
- 📋 Interactive distribution maps
- 📋 Phylogenetic tree visualization
- 📋 GitHub Actions for automated testing
- 📋 Unit tests with pytest
- 📋 Workflow automation and reproducible pipelines

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Contact

- **Issues:** [GitHub Issues](https://github.com/outobecca/botanical-colabs/issues)
- **Discussions:** [GitHub Discussions](https://github.com/outobecca/botanical-colabs/discussions)
- **Email:** Open an issue for contact information

---

**Maintained by:** Pekka Sihvonen  
**License:** MIT  
**Last updated:** 2025-11-04