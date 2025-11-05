# Contributing to Botanical Sciences Colab Notebooks

Thank you for your interest in contributing! This project aims to provide reproducible, scientifically rigorous notebooks for botanical research.

## � Academic Verification Required

**This repository requires academic verification for all contributors** to ensure scientific rigor and credibility.

### Who Can Contribute?

We welcome contributions from:
- ✅ Faculty at accredited universities
- ✅ Researchers at recognized institutions
- ✅ Postdoctoral researchers
- ✅ Graduate students (Masters/PhD)
- ✅ Scientists at botanical gardens, museums, or conservation organizations

### Verification Process

1. **Submit your PR** - Create your pull request normally
2. **Get notified** - Automated workflow will post verification instructions
3. **Provide credentials** - Email or comment with your institutional affiliation
4. **Wait 1-3 days** - We verify your academic status
5. **Contribute freely** - Once verified, all future PRs are pre-approved

**Full details:** [Academic Verification Guide](.github/ACADEMIC_VERIFICATION.md)

**Why?** Our notebooks are used for research, education, and conservation. We need to ensure all contributions meet academic standards.

---

## �🌿 How to Contribute

### Types of Contributions

1. **New Notebooks**
   - Plant identification tools
   - Species analysis pipelines
   - Data visualization examples
   - Educational tutorials

2. **Improvements to Existing Notebooks**
   - Bug fixes
   - Better documentation
   - Performance optimizations
   - Additional data sources

3. **Documentation**
   - README improvements
   - Tutorial content
   - API documentation
   - Example use cases

4. **Data Sources**
   - Integration of new APIs
   - Alternative data providers
   - Data validation methods

## 📝 Contribution Guidelines

### 📋 Using the Notebook Template

**All new notebooks should start from the template:** `notebooks/TEMPLATE_botanical_notebook.ipynb`

The template provides:
- ✅ Standardized 6-step structure (Setup → Helpers → Data → Execute → Display → Citations)
- ✅ Pre-configured helper functions with error handling
- ✅ Interactive UI widgets and Colab Secrets integration
- ✅ Type hints and comprehensive docstrings
- ✅ Citation and provenance tracking templates
- ✅ Data visualization templates

**Quick start:**
```bash
# Copy template
cp notebooks/TEMPLATE_botanical_notebook.ipynb notebooks/your-new-notebook.ipynb

# Or in Colab: File → Save a copy
```

**See [TEMPLATE_GUIDE.md](TEMPLATE_GUIDE.md) for detailed instructions.**

### Notebook Standards

All notebooks should follow these principles:

#### 1. **Scientific Rigor**
- ✅ Cite all data sources with dates and URLs
- ✅ Include data provenance and quality indicators
- ✅ Document assumptions and limitations
- ✅ Add disclaimers for AI-generated content
- ✅ Use peer-reviewed sources when possible

#### 2. **Code Quality**
```python
# Use type hints
def fetch_species_data(scientific_name: str) -> Optional[Dict[str, Any]]:
    """
    Fetch species data from API.
    
    Args:
        scientific_name: Binomial nomenclature (e.g., "Quercus robur")
    
    Returns:
        Dictionary with species data or None if not found
        
    Source:
        GBIF.org - Global Biodiversity Information Facility
        https://www.gbif.org
    """
    pass
```

- ✅ Add docstrings to all functions
- ✅ Use type hints for function signatures
- ✅ Handle errors gracefully
- ✅ Provide clear error messages
- ✅ Follow PEP 8 style guidelines

#### 3. **Documentation**
Each notebook should include:

- **Header cell** with:
  - Title and version
  - Author and date
  - License (MIT)
  - Brief description
  - Language indicator

- **Introduction section** with:
  - Use cases
  - Data sources (with citations)
  - Requirements (API keys, packages)
  - Expected outputs

- **Clear section headers** using markdown:
  - `# Main Title`
  - `## Section`
  - `### Subsection`

- **Comments in code**:
  - Explain complex logic
  - Document assumptions
  - Note potential edge cases

#### 4. **Reproducibility**
- ✅ Pin package versions in requirements
- ✅ Test in Google Colab
- ✅ Test locally (if applicable)
- ✅ Include sample outputs
- ✅ Document expected runtime

#### 5. **User Experience**
- ✅ Use clear variable names
- ✅ Add progress indicators
- ✅ Provide helpful error messages
- ✅ Include usage examples
- ✅ Add data visualization where appropriate

### Notebook Structure Template

**Use the provided template:** `notebooks/TEMPLATE_botanical_notebook.ipynb`

The template includes a complete 6-step structure:

1. **Installation & Configuration** — Package installation, imports, UI widgets, API key retrieval
2. **Helper Functions** — Reusable utilities (safe_api_call, validation, formatting, citations)
3. **Data Fetching Functions** — API calls organized by source
4. **Execute Data Collection** — Main workflow orchestrating all data fetching
5. **Data Analysis & Visualization** — Tables, plots, statistical summaries
6. **Citations & Documentation** — Data source citations, provenance tracking

**Detailed guide:** See [TEMPLATE_GUIDE.md](TEMPLATE_GUIDE.md) for:
- Step-by-step customization instructions
- Code style guidelines
- Examples from existing notebooks
- Contribution checklist

**Minimal structure** for custom notebooks:
```markdown
# 🌿 [Notebook Title]
**Version:** 1.0 | **Date:** YYYY-MM-DD | **Author:** Your Name

## Description
Brief description of what the notebook does.

## Use Cases
- Use case 1
- Use case 2

## Data Sources
- Source 1: URL and citation
- Source 2: URL and citation

## Requirements
- Python 3.8+
- API keys: [list required keys]
- Packages: [list from requirements.txt]

## Setup
[Installation and configuration instructions]
```

## 🔄 Contribution Workflow

### 1. Fork the Repository
```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/botanical-colabs.git
cd botanical-colabs
```

### 2. Create a Branch
```bash
# Use descriptive branch names
git checkout -b feature/new-species-classifier
git checkout -b fix/api-error-handling
git checkout -b docs/improve-readme
```

### 3. Make Your Changes

For new notebooks:
- Place in `notebooks/` directory
- Use descriptive filename: `feature-description_language.ipynb`
- Test thoroughly in Colab
- Include sample outputs

For code changes:
- Follow existing code style
- Add/update docstrings
- Test error handling

### 4. Test Your Changes

**In Google Colab:**
```python
# Test with valid data
test_species = "Quercus robur"

# Test with edge cases
test_invalid = "InvalidName123"
test_empty = ""

# Test error handling
# (simulate API failures, missing keys, etc.)
```

**Locally:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run notebook (if using nbconvert)
jupyter nbconvert --to notebook --execute your_notebook.ipynb
```

### 5. Commit Your Changes
```bash
# Use conventional commit messages
git add .
git commit -m "feat: add species distribution mapper notebook"
git commit -m "fix: handle timeout errors in API calls"
git commit -m "docs: improve setup instructions"
```

**Commit message format:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Maintenance tasks

### 6. Push and Create Pull Request
```bash
git push origin your-branch-name
```

Then create a Pull Request on GitHub with:
- **Clear title** describing the change
- **Description** of what and why
- **Screenshots/outputs** for notebooks
- **Testing notes** (what you tested)
- **Related issues** (if applicable)

### 7. Automatic Documentation Generation 🤖

When you create or update notebooks in a PR, our **Auto-Documentation Workflow** automatically:

- ✅ **Generates Wiki Pages** — Comprehensive documentation with setup instructions, features, and usage examples
- ✅ **Creates HTML Previews** — Rendered outputs without code cells for easy viewing
- ✅ **Generates Thumbnails** — Preview images for gallery display
- ✅ **Posts PR Comment** — Summary with links to all generated documentation

**What you need to do:** Nothing! Just add good metadata to your notebook (see below).

**Improve auto-generated docs** by adding metadata in your notebook's first markdown cell:
```markdown
# My Analysis Title

Clear description of what this notebook does and why it's useful.

**Author:** Your Name
**Tags:** data-analysis, plants, visualization
```

The workflow will:
1. Detect changed notebooks in your PR
2. Extract metadata (title, description, tags, cell counts)
3. Generate wiki page at `wiki/your-notebook.md`
4. Create HTML preview at `previews/html/your_notebook.html`
5. Generate thumbnail at `thumbnails/your_notebook.png`
6. Commit all files to your PR branch
7. Post a comment with links to all generated docs

**Learn more:**
- 📚 [Auto-Documentation Guide](.github/workflows/AUTO_DOCUMENTATION.md)
- ⚡ [Quick Reference](.github/workflows/QUICK_REFERENCE.md)

## 📋 Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code follows project style guidelines
- [ ] All functions have docstrings with type hints
- [ ] Data sources are properly cited
- [ ] Notebook runs without errors in Colab
- [ ] Error handling is implemented
- [ ] Documentation is updated
- [ ] README updated (if adding new notebook)
- [ ] No API keys or secrets in code
- [ ] Commit messages are clear and descriptive

## 🐛 Reporting Issues

### Bug Reports
When reporting bugs, include:
- **Notebook name and cell number**
- **Error message** (full traceback)
- **Expected behavior**
- **Steps to reproduce**
- **Environment** (Colab vs local, Python version)
- **API response** (if applicable, sanitized)

### Feature Requests
When requesting features, include:
- **Use case** (why is this needed?)
- **Expected behavior**
- **Alternative solutions** you've considered
- **Additional context** (data sources, similar tools)

## 🎓 Scientific Standards

### Data Quality
- Always validate API responses
- Check for completeness and accuracy
- Note confidence levels (e.g., GBIF confidence scores)
- Document data limitations

### Citations
Use this format for data sources:
```
Source Name (Access Date). Description. DOI or URL
```

Example:
```
GBIF.org (2025-11-04). GBIF Backbone Taxonomy. https://doi.org/10.15468/39omei
```

### AI-Generated Content
If using AI (Gemini, GPT, etc.):
- ✅ Clearly label AI-generated content
- ✅ Add disclaimers about non-peer-reviewed status
- ✅ Encourage critical evaluation
- ✅ Do not present as authoritative

**Mark AI-generated notebooks** in `.github/peer-review.json`:
```json
"metadata": {
  "ai_generated": true,
  "ai_assistant": "GitHub Copilot"
}
```

## 🔬 Peer Review Process

All notebooks undergo peer review to ensure scientific accuracy and quality.

### Review Requirements

- **Templates:** 2 peer reviews required
- **Examples:** 2 peer reviews required  
- **Educational:** 1 peer review required
- **Regional:** 1 peer review required

### Review Categories

- ✅ **Scientific Accuracy** — Data sources, taxonomy, results
- ✅ **Methodology** — Code quality, algorithms, error handling
- ✅ **Documentation** — Clarity, citations, instructions
- ✅ **Usability** — Ease of use, interface, error messages
- ✅ **Reproducibility** — Consistency, dependencies, instructions

### How to Submit a Review

1. **Test the notebook** thoroughly in Google Colab
2. **Evaluate** against the review categories
3. **Use the template** in `.github/PULL_REQUEST_TEMPLATE/peer_review.md`
4. **Submit** your review by updating `.github/peer-review.json`

**Full guidelines:** See [PEER_REVIEW.md](PEER_REVIEW.md)

### Badges

Approved notebooks earn badges:
- ![Peer Reviewed](https://img.shields.io/badge/Peer_Reviewed-✓-success) — Verified by 2+ reviewers
- ![AI Generated](https://img.shields.io/badge/AI_Generated-GitHub_Copilot-blue) — Created with AI assistance

## 💬 Communication

- **Questions**: Open an issue with the `question` label
- **Discussions**: Use GitHub Discussions
- **Bugs**: Open an issue with the `bug` label
- **Features**: Open an issue with the `enhancement` label

## 📜 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on scientific accuracy
- Give credit where due
- Help newcomers learn

## 🙏 Recognition

Contributors will be acknowledged in:
- Repository README
- Notebook author sections (for significant contributions)
- Release notes

Thank you for contributing to botanical science and open research! 🌱

---

**Questions?** Open an issue or contact the maintainer.
