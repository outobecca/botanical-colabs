# Botanical Sciences Colab Notebooks

A collection of reproducible Jupyter/Colab notebooks for practical botanical, horticultural, and agricultural research — combining open data sources, simple data pipelines, and AI-assisted workflows.

This repository provides a comprehensive suite of tools and templates for plant science, designed to empower researchers, educators, students, and hobbyists to conduct data-driven botanical research without requiring extensive programming knowledge or local computing infrastructure. All notebooks are optimized to run in Google Colab, making advanced botanical analysis accessible to everyone.

## 🎯 What This Repository Offers

- **Production-ready notebooks** for real-world botanical research tasks
- **Comprehensive templates** to jumpstart your own botanical data projects
- **Educational materials** for learning data science in the context of plant science
- **Regional analysis tools** leveraging local open data sources
- **Multi-language support** for global accessibility
- **Zero local setup** required - runs entirely in Google Colab
- ⭐ **NEW: MyST & Marp** — Scientific documentation and presentation features

## ✨ New in Version 2.0

🚀 **Enhanced with Professional Features:**
- **MyST Markdown** — Advanced scientific documentation with cross-references, citations, and admonitions
- **Marp Presentations** — Convert notebooks to beautiful slide decks (HTML, PDF, PowerPoint)
- **Auto-Reload Magic** — Efficient development with instant code updates
- **Code Modularization** — %%writefile for organized, reusable code
- **Jupyter Book Support** — Build publication-quality documentation
- **VS Code Optimized** — Full IDE features with notebook integration

📖 See [MyST & Marp Integration Guide](MYST_MARP_GUIDE.md) for details

## Quick links
- 🌐 Repository: https://github.com/outobecca/botanical-colabs
- 🌍 GitHub Pages: https://outobecca.github.io/botanical-colabs/
- 📓 Notebooks: `notebooks/`
- 🔑 [API Setup Guide](API_SETUP.md)
- 🤝 [Contributing Guidelines](CONTRIBUTING.md)
- 📋 [Changelog](CHANGELOG.md)
- ⚖️ [License](LICENSE)
- 📄 [GitHub Pages Setup](GITHUB_PAGES.md)
- ⭐ **[MyST & Marp Guide](MYST_MARP_GUIDE.md)** ← NEW!

## 🏆 Badges

Here's a list of badges used in this repository to indicate the status of each notebook:

*   ![Under Review](https://img.shields.io/badge/status-under%20review-yellow) - This notebook is currently under peer review.
*   ![Needs API Keys](https://img.shields.io/badge/status-needs%20api%20keys-red) - This notebook requires API keys to function.
*   ![In Production](https://img.shields.io/badge/status-in%20production-green) - This notebook is considered stable and ready for general use.
*   ![Experimental](https://img.shields.io/badge/status-experimental-orange) - This notebook is still under development and may not be stable.

## 📚 Notebook Organization

Notebooks are organized into six specialized categories, each designed for specific use cases in botanical and agricultural science:

- 📐 **[templates/](notebooks/templates/)** - Starting point templates for different scientific workflows and analysis types
- 🌾 **[agrology/](notebooks/agrology/)** - Field crop and soil science analysis with statistical tools and data exploration  
- 🏗️ **[greenhouse/](notebooks/greenhouse/)** - Protected cultivation management, ML predictions, and visualization tools
- 🗺️ **[regional/](notebooks/regional/)** - Region-specific analysis using local open data sources (starting with Finland)
- 🎓 **[education/](notebooks/education/)** - Interactive learning materials for beginners in botanical data science
- 📋 **[examples/](notebooks/examples/)** - Real-world implementations demonstrating best practices

---

## 📐 Templates (notebooks/templates/)

Professionally designed starting points for creating new botanical research notebooks. Each template includes pre-configured sections, best practices for documentation, error handling, and data source citations. **Now enhanced with MyST markdown, auto-reload, and Marp presentation features!**

### ⭐ `TEMPLATE_myst_scientific.ipynb` — MyST Scientific Template NEW!
Advanced scientific notebook template with MyST markdown features for publication-quality documentation. Includes cross-references, citations, admonitions, auto-reload setup, %%writefile for code modularization, and Jupyter Book compatibility. Perfect for research papers, scientific reports, and technical documentation.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_myst_scientific.ipynb)

### ⭐ `TEMPLATE_marp_presentation.ipynb` — Marp Presentation Template NEW!
Convert your botanical research into beautiful presentations! Includes Marp markdown for slides, live demo code cells, professional visualizations, and export options (HTML, PDF, PowerPoint). Ideal for conferences, teaching, and stakeholder presentations.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_marp_presentation.ipynb)

### `TEMPLATE_botanical_notebook.ipynb` — General Template
Comprehensive general-purpose template for botanical science notebooks. Includes sections for literature review, data collection, analysis, visualization, and conclusions. Features built-in support for GBIF, Trefle, and other major botanical databases.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_botanical_notebook.ipynb)

### `TEMPLATE_data_analysis.ipynb` — Data Analysis Template  
Specialized template pre-configured for analyzing environmental sensors, soil tests, and plant measurements. Includes statistical tests, outlier detection, correlation analysis, and automated report generation. Ideal for greenhouse operators and field researchers.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_data_analysis.ipynb)

### `TEMPLATE_machine_learning.ipynb` — ML Template
Production-ready machine learning template specialized for agricultural applications like crop yield prediction and disease risk models. Includes feature engineering, model selection, hyperparameter tuning, and model evaluation with agricultural metrics.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_machine_learning.ipynb)

### `TEMPLATE_environmental_monitoring.ipynb` — Environmental Template
Focused template for monitoring and analyzing soil health, water usage, climate data, and sustainability metrics. Perfect for environmental assessments, resource optimization, and sustainability reporting.
[📖 Details](notebooks/templates/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_environmental_monitoring.ipynb)

---

## 🌾 Agrology (notebooks/agrology/)

Advanced field crop and soil science analysis notebooks designed for researchers and farmers working with agricultural data. These notebooks provide powerful statistical tools and data exploration capabilities for making data-driven decisions in crop management.

### `data_analysis_exploration.ipynb` — Data Analysis & Exploration
Comprehensive interactive analysis toolkit for environmental sensors, soil tests, and plant measurements. Features automated outlier detection, statistical summaries, correlation analysis, and data quality assessment. Includes visualization tools for time-series data, spatial patterns, and multi-variate relationships. Perfect for initial data exploration and quality control.
[📖 Details](notebooks/agrology/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/agrology/data_analysis_exploration.ipynb)

### `environmental_management.ipynb` — Environmental & Resource Management
In-depth analysis of soil health indicators, water usage patterns, climate resilience metrics, and resource consumption for sustainable agriculture. Includes carbon footprint calculations, water efficiency metrics, and sustainability reporting tools. Ideal for precision agriculture and environmental impact assessments.
[📖 Details](notebooks/agrology/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/agrology/environmental_management.ipynb)

### `fertilizer_calculations.ipynb` — Fertilizer Calculations
Calculate precise fertilizer requirements based on crop-specific nutrient needs, soil test results, and field characteristics. Supports multiple crops (vegetables, grains, legumes, root crops) with NPK optimization for nitrogen, phosphorus, and potassium. Features nutrient budget calculations, fertilizer product recommendations, application rate determination, and cost estimates. Accounts for existing soil nutrients and fertilizer efficiency to minimize waste and environmental impact. Ideal for precision agriculture, nutrient management planning, and sustainable farming practices.
[📖 Details](notebooks/agrology/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/agrology/fertilizer_calculations.ipynb)

---

## 🏗️ Greenhouse (notebooks/greenhouse/)

Specialized notebooks for protected cultivation and greenhouse management, featuring advanced machine learning models and interactive visualizations for optimizing growing conditions and predicting outcomes.

### `ml_yield_prediction.ipynb` — Crop Yield Prediction & ML
State-of-the-art machine learning models for predicting crop yield, disease risk assessment, and optimal growing condition recommendations. Implements Random Forest, Gradient Boosting, and neural network models with comprehensive feature importance analysis. Includes model validation, cross-validation strategies, and prediction confidence intervals. Essential for data-driven greenhouse management and yield optimization.
[📖 Details](notebooks/greenhouse/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/greenhouse/ml_yield_prediction.ipynb)

### `data_visualization.ipynb` — Data Visualization
Professional-quality interactive visualizations for plant growth monitoring, environmental conditions tracking, and greenhouse performance metrics. Utilizes Matplotlib for publication-ready static plots, Seaborn for statistical graphics, and Plotly for interactive dashboards. Create time-series plots, heatmaps, 3D visualizations, and custom dashboards for presenting research findings or operational reports.
[📖 Details](notebooks/greenhouse/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/greenhouse/data_visualization.ipynb)

### `lighting_setup_analyzer.ipynb` — Lighting Setup Analyzer
Comprehensive analysis of greenhouse lighting setups using CSV measurement data. Evaluates PPFD (Photosynthetic Photon Flux Density), light intensity distribution across zones, uniformity ratios to identify hot/cold spots, Daily Light Integral (DLI) for photoperiod control, and energy efficiency metrics. Provides actionable recommendations for optimizing plant growth conditions while minimizing energy costs. Essential for greenhouse operators managing supplemental lighting, ensuring uniform crop development, and meeting the 200-400 μmol/m²/s PPFD requirements for optimal photosynthesis.
[📖 Details](notebooks/greenhouse/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/greenhouse/lighting_setup_analyzer.ipynb)

---

## 🗺️ Regional (notebooks/regional/)

Region-specific horticultural analysis leveraging local open data sources and meteorological services. These notebooks demonstrate how to integrate national databases and services for localized botanical research.

### `finnish_weather_analysis.ipynb` 🇫🇮 — Finnish Weather Analysis
Comprehensive analysis of Finnish weather data for horticultural applications using FMI (Ilmatieteen laitos) open data API. Calculate growing season metrics, frost risk assessments, and Growing Degree Days (GDD) for different crop types. Includes historical climate analysis, seasonal patterns, and future climate projections. Features bilingual documentation (Finnish/English) for accessibility. Ideal for Finnish farmers, researchers, and gardeners planning crop selection and timing. **Note:** Can be adapted for other national weather services.
[📖 Details](notebooks/regional/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/regional/finnish_weather_analysis.ipynb)

---

## 🎓 Education (notebooks/education/)

Interactive learning materials designed for complete beginners in botanical data science. These notebooks require no prior programming experience and provide step-by-step guidance with real botanical examples.

### `education_tutorial.ipynb` — Data Science Tutorial
Comprehensive interactive learning environment for beginners in botanical data science. Covers Python programming basics, Pandas for data manipulation, data visualization techniques, statistical analysis fundamentals, and introductory machine learning—all with horticultural and botanical examples. Features hands-on exercises, quizzes, and real-world case studies. Perfect for students, educators, and professionals transitioning into data-driven plant science. **No prior programming required!** Start your journey into botanical data science here.
[📖 Details](notebooks/education/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/education/education_tutorial.ipynb)

---

## 📋 Examples (notebooks/examples/)

Real-world implementations and demonstrations showcasing best practices for botanical data integration and multi-source data aggregation.

### `generator-plant-card.ipynb` — Plant Card Generator
Advanced multi-source plant information aggregator that creates comprehensive, professionally formatted plant care cards. Fetches and combines data from GBIF (species occurrence), Trefle (plant characteristics), Wikipedia (encyclopedic information), iNaturalist (observations), and more. Features AI-powered content summarization using Google's Gemini API, automated image selection with quality scoring, and intelligent data validation. Supports 9 languages for global accessibility (English, Finnish, Swedish, Spanish, French, German, Italian, Portuguese, Dutch). Perfect for creating educational materials, nursery labels, botanical garden signage, or personal plant reference cards. **Demonstrates advanced API integration patterns and data fusion techniques.**
[📖 Details](notebooks/examples/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/examples/generator-plant-card.ipynb)

---

## Features & goals
- Demonstrate reproducible data queries against biodiversity APIs.
- Create concise, printable plant care cards from aggregated data.
- Provide Colab-ready notebooks so researchers and hobbyists can run examples without local setup.

## 🌟 Key Features

### No Setup Required
All notebooks run directly in Google Colab - no local installation, no environment configuration, no Python setup needed. Just click and start analyzing.

### 📱 Mobile-Friendly
Notebooks are optimized for mobile devices through:
- **Mercury Web Apps**: Convert notebooks to mobile-optimized web applications
- **Responsive Design**: Touch-friendly interfaces that work on phones and tablets
- **Progressive Web Apps**: Installable apps with offline capabilities
- **Simplified Mobile Versions**: Streamlined interfaces for small screens

### Open Data Integration
Seamlessly connects to major botanical and environmental databases:
- **GBIF** (Global Biodiversity Information Facility) - 2+ billion species occurrences
- **Trefle** - Comprehensive plant data API with 400,000+ species
- **FMI Open Data** - Finnish Meteorological Institute weather data
- **Wikipedia/Wikimedia** - Encyclopedic content and high-quality images
- **iNaturalist** - Community science observations

### AI-Powered Analysis
Leverage Google's Gemini API for:
- Automated content summarization
- Natural language insights from data
- Multi-language content generation
- Intelligent data interpretation

### Production-Ready Code
All notebooks include:
- Comprehensive error handling and validation
- Type hints and documentation
- Scientific citations and data provenance
- Best practices for reproducible research
- Modular, reusable code structure

### Educational Focus
Designed for both learning and production use:
- Step-by-step explanations
- Visualization of intermediate results  
- Interactive widgets for exploration
- Real-world examples and use cases

## Run the notebooks

### 🌐 Web/Desktop (Recommended)
Open notebooks in Google Colab (no local install needed):

1. Open the notebook file in the `notebooks/` folder.
2. Click "Open in Colab" or upload the notebook to Colab.
3. If a cell installs packages (e.g., `pip install requests pandas google-generativeai`), run it.

### 📱 Mobile Devices
For the best mobile experience, use our Mercury web apps:

#### Quick Mobile Deployment
```bash
# Setup mobile environment
python deploy_mobile.py --setup

# Run a notebook as mobile web app
python deploy_mobile.py --serve notebooks/examples/mobile_plant_card.ipynb

# Deploy all notebooks to Mercury Cloud
python deploy_mobile.py --all --deploy
```

#### Manual Setup
1. Install Mercury: `pip install mercury`
2. Run: `mercury run notebooks/examples/mobile_plant_card.ipynb`
3. Open in your mobile browser at `http://localhost:8000`
4. Or deploy to cloud for shareable mobile links

**Mobile Examples:**
- 🌱 [Mobile Plant Card Generator](notebooks/examples/mobile_plant_card.ipynb) - Touch-optimized plant care cards
- 📊 [Mobile Fertilizer Calculator](notebooks/agrology/fertilizer_calculations.ipynb) - Simplified mobile interface
- 🌡️ [Mobile Weather Analysis](notebooks/regional/finnish_weather_analysis.ipynb) - Location-based mobile analysis

📖 See [Mobile Deployment Guide](MOBILE_DEPLOYMENT.md) for detailed instructions.

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
- ✅ **Fertilizer calculations with crop-specific nutrient needs**
- ✅ **Greenhouse lighting setup analyzer with PPFD and DLI metrics**
- ✅ **Finnish weather analysis with FMI integration**

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