# Botanical Sciences Colab Notebooks

A collection of reproducible Jupyter/Colab notebooks for practical botanical, horticultural, and agricultural research — combining open data sources, simple data pipelines, and AI-assisted workflows.

This repository is focused on small, shareable notebooks that demonstrate useful analyses and tools for plant science, including plant identification, species factsheets, distribution summaries, and plant care card generation.

## Quick links
- 🌐 Repository: https://github.com/outobecca/botanical-colabs
- 📓 Notebooks: `notebooks/`
- 🔑 [API Setup Guide](API_SETUP.md)
- 🤝 [Contributing Guidelines](CONTRIBUTING.md)
- 📋 [Changelog](CHANGELOG.md)
- ⚖️ [License](LICENSE)

## Included notebooks

### 📋 `TEMPLATE_botanical_notebook.ipynb` — Notebook Template
A standardized template for creating new botanical science notebooks. Follow this structure when contributing new analyses to the repository.

**Includes:**
- 🏗️ Standard 6-step structure (Setup → Helpers → Data → Execute → Display → Citations)
- 🔧 Pre-configured helper functions with error handling
- 📊 Data visualization templates
- 📚 Citation and provenance tracking
- 🎨 Interactive widgets and UI components
- 🔑 Colab Secrets integration
- ✅ Type hints and comprehensive docstrings

**Use this template when:**
- Creating new botanical analysis notebooks
- Contributing to the repository
- Standardizing existing notebooks
- Learning the repository structure

**Interface:** English  
**Status:** Template (starting point for new notebooks)  
**Open in Colab:** [Direct link](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/TEMPLATE_botanical_notebook.ipynb)

---

### 🌿 `generator-plant-card_en.ipynb` *(v1.2)* — Multilingual Plant Card Generator
Plant card generator that aggregates data from multiple biodiversity databases and creates comprehensive species factsheets. **Now with multilingual support!**

**Core Features:**
- 🌍 GBIF taxonomy and occurrence data
- 🌱 Trefle plant characteristics
- 🎨 Wikimedia Commons botanical illustrations
- 📚 Encyclopedia of Life ecological data
- 🐦 iNaturalist community observations
- 📖 Wikipedia summaries (in your language!)
- 🇫🇮 Laji.fi Finnish species names (optional)
- 📜 BHL historical illustrations
- 🤖 AI-generated summaries (Google Gemini, in your language!)

**Supported Languages:**
- 🇬🇧 English
- 🇫🇮 Finnish (Suomi)
- 🇸🇪 Swedish (Svenska)
- 🇩🇪 German (Deutsch)
- 🇫🇷 French (Français)
- 🇪🇸 Spanish (Español)
- 🇮🇹 Italian (Italiano)
- 🇯🇵 Japanese (日本語)
- �� Chinese (中文)

**What's multilingual?**
- Wikipedia summaries fetched in your selected language
- AI-generated descriptions written in your selected language
- UI remains in English for consistency

**Interface:** English  
**Status:** Production ready  
**Open in Colab:** [Direct link](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/generator-plant-card_en.ipynb)

---

### 📝 Legacy Notebooks

**`Kasvikortti.ipynb`** — Original Finnish version (archived, use generator-plant-card_en.ipynb instead)

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

### In progress 🚧
- 🚧 Batch processing for multiple species
- 🚧 Export to PDF/HTML

### Planned 📋
- 📋 Crop yield prediction models
- 📋 Pest and disease identification
- 📋 Soil health analysis tools
- 📋 Interactive distribution maps
- 📋 Phylogenetic tree visualization
- 📋 GitHub Actions for automated testing
- 📋 Unit tests with pytest

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Contact

- **Issues:** [GitHub Issues](https://github.com/outobecca/botanical-colabs/issues)
- **Discussions:** [GitHub Discussions](https://github.com/outobecca/botanical-colabs/discussions)
- **Email:** Open an issue for contact information

---

**Maintained by:** Pekka Sihvonen  
**License:** MIT  
**Last updated:** 2025-11-04