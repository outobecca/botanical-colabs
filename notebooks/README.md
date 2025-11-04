# 📓 Botanical Sciences Notebooks

This directory contains a collection of reproducible Jupyter/Colab notebooks for botanical, horticultural, and agricultural research. Each notebook is designed to be self-contained, well-documented, and scientifically rigorous.

## 🎯 Our Vision

We aim to create a comprehensive library of **ready-to-use, scientifically validated notebooks** that demonstrate:

- 🔬 **Reproducible research methods** using open botanical data sources
- 📊 **Data-driven insights** for plant science, ecology, and agriculture
- 🤖 **AI-assisted workflows** that augment (not replace) scientific expertise
- 🌍 **Multilingual accessibility** to serve the global botanical community
- 🎓 **Educational resources** for students, researchers, and hobbyists

### Why Notebooks?

Jupyter notebooks combine code, documentation, and visualizations in a single reproducible document. This makes them ideal for:

- **Teaching** — Show methodology alongside results
- **Research** — Document complete analytical pipelines
- **Collaboration** — Share reproducible analyses
- **Prototyping** — Rapidly test ideas with real data
- **Communication** — Create publication-ready figures and tables

## 📋 Template System

To maintain consistency and quality, all notebooks follow **standardized templates**. Each template provides a proven structure for a specific type of analysis.

### Current Templates

#### 🌿 **TEMPLATE_botanical_notebook.ipynb** — General Botanical Research
The foundational template for most botanical analyses.

**Use this template for:**
- Species data aggregation and analysis
- Biodiversity assessments
- Distribution mapping and visualization
- Taxonomic queries and validation
- Plant trait analysis
- General-purpose botanical research

**Structure:**
1. **Installation & Configuration** — Libraries, imports, UI widgets, API keys
2. **Helper Functions** — Utilities, validation, formatting, citations
3. **Data Fetching Functions** — API calls organized by source
4. **Execute Data Collection** — Main workflow orchestrating data retrieval
5. **Data Analysis & Visualization** — Tables, plots, statistical summaries
6. **Citations & Documentation** — Source tracking and provenance

**Features:**
- ✅ Type-hinted functions with comprehensive docstrings
- ✅ Error handling patterns for robust execution
- ✅ Colab Secrets integration for secure API key storage
- ✅ Interactive UI widgets for parameter configuration
- ✅ Automated citation and provenance tracking
- ✅ Data validation and quality checks
- ✅ Publication-ready visualizations

**Get started:** See [TEMPLATE_GUIDE.md](../TEMPLATE_GUIDE.md) for detailed instructions.

### 🚀 Future Templates (Coming Soon)

We're developing specialized templates for common botanical research workflows:

#### 🗺️ **TEMPLATE_distribution_mapping.ipynb** — Species Distribution Analysis
**Purpose:** Create occurrence maps, analyze distribution patterns, assess range shifts

**Will include:**
- GBIF occurrence data retrieval and cleaning
- Spatial analysis tools (range size, hotspots, endemism)
- Interactive maps with Folium/Plotly
- Climate zone overlay analysis
- Conservation status assessment
- Export to GIS formats (GeoJSON, Shapefile)

**Use cases:**
- Species range mapping
- Biodiversity hotspot identification
- Climate change impact assessment
- Conservation planning
- Invasive species tracking

---

#### 📊 **TEMPLATE_trait_analysis.ipynb** — Plant Trait Data Analysis
**Purpose:** Analyze morphological, physiological, and ecological traits

**Will include:**
- Trait database integration (TRY, BIEN, GIFT)
- Statistical comparisons across groups
- Phylogenetic signal analysis
- Trait-environment correlations
- PCA and clustering visualizations
- Publication-ready trait tables

**Use cases:**
- Functional ecology studies
- Comparative morphology
- Ecophysiology research
- Trait-based ecology
- Plant strategy analysis

---

#### 🌡️ **TEMPLATE_phenology_analysis.ipynb** — Phenological Event Tracking
**Purpose:** Analyze plant life cycle events and seasonal patterns

**Will include:**
- Phenology database integration (USA-NPN, PEP725)
- Time series visualization
- Climate correlation analysis
- Trend detection (flowering time shifts)
- Growing degree day calculations
- Seasonal pattern modeling

**Use cases:**
- Climate change phenology research
- Agricultural timing optimization
- Ecosystem monitoring
- Citizen science data analysis
- Pollinator synchrony studies

---

#### 🧬 **TEMPLATE_phylogenetic_analysis.ipynb** — Phylogenetic Tree Analysis
**Purpose:** Construct and analyze evolutionary relationships

**Will include:**
- GenBank sequence retrieval
- Multiple sequence alignment
- Phylogenetic tree construction
- Tree visualization (ETE, Toytree)
- Ancestral state reconstruction
- Diversification rate analysis

**Use cases:**
- Evolutionary biology research
- Taxonomic revisions
- Biogeography studies
- Trait evolution analysis
- Molecular systematics

---

#### 🌾 **TEMPLATE_crop_analysis.ipynb** — Agricultural Crop Analysis
**Purpose:** Analyze crop data for agricultural applications

**Will include:**
- Crop yield prediction models
- Weather data integration
- Soil parameter analysis
- Pest/disease risk assessment
- Economic analysis tools
- Farm management recommendations

**Use cases:**
- Precision agriculture
- Yield forecasting
- Crop planning
- Resource optimization
- Climate adaptation strategies

---

#### 🏛️ **TEMPLATE_herbarium_digitization.ipynb** — Herbarium Data Processing
**Purpose:** Process and analyze digitized herbarium specimens

**Will include:**
- Image preprocessing and OCR
- Label data extraction
- Georeferencing tools
- Collection gap analysis
- Historical distribution reconstruction
- Databasing and export tools

**Use cases:**
- Museum digitization projects
- Historical biodiversity reconstruction
- Collection management
- Research dataset creation
- Citizen science coordination

---

#### 🔬 **TEMPLATE_ecological_modeling.ipynb** — Ecological Niche Modeling
**Purpose:** Model species distributions and ecological niches

**Will include:**
- MaxEnt and other SDM algorithms
- Environmental layer processing
- Model validation and evaluation
- Future climate projections
- Habitat suitability mapping
- Range shift predictions

**Use cases:**
- Conservation planning
- Invasive species risk assessment
- Climate change vulnerability
- Restoration site selection
- Biodiversity forecasting

---

#### 📖 **TEMPLATE_literature_analysis.ipynb** — Scientific Literature Mining
**Purpose:** Extract insights from botanical literature

**Will include:**
- PubMed/Web of Science API integration
- Text mining and NLP analysis
- Co-citation network visualization
- Topic modeling (LDA)
- Trend analysis over time
- Citation map generation

**Use cases:**
- Literature reviews
- Research trend identification
- Knowledge gap analysis
- Collaboration network mapping
- Systematic reviews

## 📚 Production Notebooks

These notebooks are fully functional and ready to use:

### 🌿 `generator-plant-card.ipynb` (v1.2) — Multilingual Plant Card Generator

Comprehensive species factsheet generator aggregating data from 8+ biodiversity databases.

**Data Sources:**
- 🌍 GBIF — Taxonomy and occurrence data
- 🌱 Trefle — Plant characteristics and care info
- 🎨 Wikimedia Commons — Botanical illustrations
- 📚 Encyclopedia of Life — Ecological data
- 🐦 iNaturalist — Community observations
- 📖 Wikipedia — Species summaries (multilingual)
- 🇫🇮 Laji.fi — Finnish species names (optional)
- 📜 BHL — Historical illustrations
- 🤖 Google Gemini AI — Generated summaries (multilingual)

**Languages Supported:** English, Finnish, Swedish, German, French, Spanish, Italian, Japanese, Chinese

**Perfect for:**
- Species identification and documentation
- Educational plant cards
- Biodiversity assessments
- Garden planning and plant care
- Conservation status checking
- Herbarium label generation

**Open in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/generator-plant-card.ipynb)

---

## 🚀 Getting Started

### Option 1: Use an Existing Notebook (Recommended for Beginners)

1. **Choose a notebook** from the Production Notebooks section above
2. **Open in Google Colab** by clicking the "Open in Colab" badge
3. **Add API keys** to Colab Secrets (see [API_SETUP.md](../API_SETUP.md))
4. **Run the cells** from top to bottom
5. **Customize parameters** in the configuration section
6. **Enjoy your results!**

No local installation required — runs entirely in your browser.

### Option 2: Create a New Notebook from Template

1. **Choose the appropriate template** based on your research needs
2. **Copy the template** to a new file:
   ```bash
   cp TEMPLATE_botanical_notebook.ipynb my_analysis.ipynb
   ```
3. **Follow the template guide** at [TEMPLATE_GUIDE.md](../TEMPLATE_GUIDE.md)
4. **Customize for your needs** (update data sources, analysis, visualizations)
5. **Test thoroughly** in Google Colab
6. **Share your work** (optional: submit a PR to contribute back!)

### Option 3: Run Locally (Advanced)

If you prefer local development:

```bash
# Clone the repository
git clone https://github.com/outobecca/botanical-colabs.git
cd botanical-colabs

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

## 📖 Documentation

- **[Template Guide](../TEMPLATE_GUIDE.md)** — Comprehensive guide to using and customizing templates
- **[API Setup](../API_SETUP.md)** — Instructions for obtaining and configuring API keys
- **[Quick Start](../QUICKSTART.md)** — 5-minute getting started guide
- **[Contributing](../CONTRIBUTING.md)** — Guidelines for contributing new notebooks
- **[Changelog](../CHANGELOG.md)** — Version history and updates

## 🤝 Contributing New Notebooks

We welcome contributions! Here's how to add a new notebook:

### 1. Choose the Right Template

Select the template that best matches your analysis type. If none fit perfectly, use the general `TEMPLATE_botanical_notebook.ipynb` and adapt as needed.

### 2. Follow the Template Structure

All templates use a standardized structure:
- **Step 1:** Installation & Configuration
- **Step 2:** Helper Functions
- **Step 3:** Data Fetching
- **Step 4:** Execute Data Collection
- **Step 5:** Analysis & Visualization
- **Step 6:** Citations & Documentation

This ensures consistency and makes notebooks easier to understand and maintain.

### 3. Document Thoroughly

- Add type hints to all functions
- Write comprehensive docstrings (Args, Returns, Source)
- Include data source citations with licenses
- Add comments explaining complex logic
- Provide usage examples

### 4. Test in Multiple Environments

- ✅ Test in Google Colab (primary target)
- ✅ Test with valid inputs
- ✅ Test with invalid/edge case inputs
- ✅ Verify all visualizations render correctly
- ✅ Check that error messages are helpful

### 5. Submit a Pull Request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines on:
- Code style requirements
- Commit message format
- PR description template
- Review process

## 🎓 Educational Use

These notebooks are designed to be educational as well as practical:

### For Students
- Learn data science applied to real botanical problems
- Understand how to work with scientific APIs
- Practice reproducible research methods
- See professional-quality code examples

### For Educators
- Use notebooks as teaching materials
- Assign notebooks as homework exercises
- Demonstrate real-world data analysis
- Customize for your curriculum

### For Researchers
- Quickly prototype analyses
- Document methods for publications
- Share reproducible results with colleagues
- Build on existing validated workflows

## 🔬 Scientific Standards

All notebooks in this collection follow rigorous scientific standards:

### Data Quality
- ✅ Source data from reputable databases (GBIF, EOL, etc.)
- ✅ Document data collection dates and versions
- ✅ Validate data quality and completeness
- ✅ Note limitations and uncertainties
- ✅ Provide traceable data provenance

### Reproducibility
- ✅ Pin package versions in requirements
- ✅ Document random seeds for stochastic processes
- ✅ Include sample outputs in notebooks
- ✅ Test across different environments
- ✅ Provide clear execution instructions

### Citations
- ✅ Cite all data sources with DOIs where available
- ✅ Include database access dates
- ✅ Note data licenses (CC0, CC-BY, etc.)
- ✅ Provide proper attribution
- ✅ Enable users to cite the notebook itself

### Validation
- ✅ Cross-check results against known references
- ✅ Include data validation steps
- ✅ Handle edge cases gracefully
- ✅ Provide confidence indicators
- ✅ Encourage critical evaluation

## ⚠️ Important Disclaimers

### AI-Generated Content
Some notebooks include AI-generated summaries (e.g., from Google Gemini). These should be treated as:
- ❌ **Not peer-reviewed** — Do not use as authoritative sources
- ✅ **Helpful summaries** — Good starting points for learning
- ✅ **Require validation** — Always verify with primary sources
- ✅ **Experimental** — AI may produce errors or hallucinations

### Data Currency
- Data is fetched in real-time from external APIs
- Availability and content may change over time
- Taxonomic names may be updated or revised
- Always check original sources for critical research

### License Compliance
- Each data source has its own license (see citations)
- Most are CC0 or CC-BY (attribution required)
- Commercial use restrictions may apply
- Images often have separate licenses
- Check individual source terms before reuse

## 🌟 Community

Join our growing community of botanical data scientists:

- **💬 Discussions:** [GitHub Discussions](https://github.com/outobecca/botanical-colabs/discussions)
- **🐛 Issues:** [GitHub Issues](https://github.com/outobecca/botanical-colabs/issues)
- **📧 Contact:** Open an issue for contact information

## 📊 Repository Statistics

- **Templates:** 1 (8+ more planned)
- **Production Notebooks:** 1
- **Data Sources Integrated:** 8+
- **Languages Supported:** 9
- **Lines of Documentation:** 15,000+

---

## 🗺️ Roadmap

### Short Term (Next 3 Months)
- [ ] Add distribution mapping template
- [ ] Add trait analysis template
- [ ] Create video tutorials
- [ ] Add automated testing
- [ ] Improve error messages

### Medium Term (3-6 Months)
- [ ] Add phenology analysis template
- [ ] Add phylogenetic analysis template
- [ ] Create batch processing tools
- [ ] Add PDF/HTML export functionality
- [ ] Build interactive web demos

### Long Term (6-12 Months)
- [ ] Complete all planned templates
- [ ] Add crop analysis workflows
- [ ] Create herbarium digitization tools
- [ ] Add ecological modeling capabilities
- [ ] Build literature mining notebook

## 📄 License

All notebooks and templates in this directory are released under the **MIT License**.

Data sources have their own licenses — see individual notebook citations for details.

---

**🌿 Happy researching!**

*Making botanical data science accessible, reproducible, and rigorous.*

---

**Last Updated:** November 4, 2025  
**Maintained By:** Pekka Sihvonen  
**Repository:** https://github.com/outobecca/botanical-colabs

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
