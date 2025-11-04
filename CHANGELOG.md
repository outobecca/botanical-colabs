# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Pest and disease identification tools
- Interactive distribution maps
- Batch processing capabilities
- GitHub Actions for automated testing

## [1.2.0] - 2025-11-04

### Added
- **Five new horticultural science notebooks** implementing comprehensive use cases:
  1. `data_analysis_exploration.ipynb` - Data analysis and exploration with forms for sensor/environmental data
  2. `data_visualization.ipynb` - Interactive visualizations (Matplotlib, Seaborn, Plotly)
  3. `ml_yield_prediction.ipynb` - Machine learning models for crop yield and disease prediction
  4. `environmental_management.ipynb` - Soil health, water usage, and climate resilience analysis
  5. `education_tutorial.ipynb` - Interactive learning environment for data science in horticulture
- **Interactive form-based input** in all new notebooks for easy data configuration
- **Sample data generators** for environmental sensors, soil analysis, and plant growth
- **Complete implementations** covering:
  - Data loading, cleaning, and transformation
  - Statistical analysis and outlier detection
  - Time series visualization and correlation analysis
  - Random Forest models for regression and classification
  - Feature importance analysis
  - Environmental sustainability metrics
  - Step-by-step educational tutorials
- **Export functionality** for cleaned data and analysis results
- **Comprehensive documentation** in README.md for all new notebooks
- Updated roadmap reflecting completed implementations

### Changed
- Updated README.md with detailed descriptions of all new notebooks
- Updated project roadmap to mark horticultural notebooks as completed
- Enhanced documentation for various use cases in horticultural sciences

## [1.1.0] - 2025-11-04

### Added
- Comprehensive documentation in all notebook cells
- Type hints and docstrings for all functions
- Scientific citations and data provenance tracking
- Error handling with informative messages
- `safe_api_call()` helper function for robust API calls
- `validate_scientific_name()` for input validation
- Data quality indicators (confidence scores, etc.)
- Structured data presentation with source attribution
- Professional styling for outputs
- Support for multiple data sources:
  - GBIF (taxonomy, occurrences, distribution)
  - Trefle (plant characteristics)
  - Laji.fi (Finnish names)
  - Wikimedia Commons (botanical illustrations)
  - Encyclopedia of Life (ecology)
  - Wikipedia (summaries)
  - iNaturalist (observations)
  - Biodiversity Heritage Library (historical illustrations)
- Google Gemini AI integration for summaries
- Colab vs local environment detection
- API key status indicators
- Progress tracking and status messages
- Comprehensive disclaimer and license information

### Changed
- Renamed notebook from `Kasvikortti.ipynb` to `generator-plant-card_fi.ipynb`
- Restructured notebook into clear phases (Setup → Helpers → Data Fetching → Visualization)
- Improved widget layout and styling
- Enhanced error messages with suggested fixes
- Better handling of missing or invalid data
- More scientific presentation of results
- Updated README with better project description and usage instructions

### Fixed
- Improved handling of API timeouts
- Better error recovery when data sources are unavailable
- Fixed potential issues with missing API keys
- Improved validation of scientific names
- Better handling of edge cases (empty results, invalid responses)

### Documentation
- Added detailed docstrings to all functions
- Created CONTRIBUTING.md with guidelines for contributors
- Created comprehensive LICENSE file with data source licenses
- Created .gitignore for proper version control
- Added requirements.txt for dependency management
- Improved inline comments and explanations
- Added data source descriptions and citations

### Security
- Removed hardcoded API keys
- Added secure Colab Secrets integration
- Added .gitignore to prevent committing secrets
- Improved API key validation

## [1.0.0] - 2024-06-15

### Added
- Initial release of plant card generator notebook
- Basic GBIF taxonomy fetching
- Trefle API integration for plant characteristics
- Laji.fi Finnish name lookup
- Wikimedia Commons image search
- Simple data presentation
- Interactive widget for configuration

### Known Issues
- Limited error handling
- Basic documentation
- No type hints
- Minimal data validation

---

## Version Guidelines

### Version Number Format: MAJOR.MINOR.PATCH

- **MAJOR**: Incompatible API changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

### Change Categories

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Features that will be removed
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

---

[Unreleased]: https://github.com/outobecca/botanical-colabs/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/outobecca/botanical-colabs/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/outobecca/botanical-colabs/releases/tag/v1.0.0
