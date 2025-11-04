# Botanical Sciences Colab Notebooks

A collection of reproducible Jupyter/Colab notebooks for practical botanical, horticultural, and agricultural research — combining open data sources, simple data pipelines, and AI-assisted workflows.

This repository is focused on small, shareable notebooks that demonstrate useful analyses and tools for plant science, including plant identification, species factsheets, distribution summaries, and plant care card generation.

## Quick links
- Repository: https://github.com/outobecca/botanical-colabs
- Notebooks directory: `notebooks/`

## Included notebooks (starter)
- `notebooks/Kasvikortti.ipynb` — Plant card generator that aggregates data from GBIF, Trefle, Laji.fi, Wikimedia Commons, EOL, BHL and (optionally) uses Gemini for short AI summaries. Language: Finnish.

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

Some data sources require API keys or tokens (Trefle, BHL, Laji.fi, Google/Gemini). Best practice:
- Store keys in Colab using environment variables, Colab "secrets" features, or the notebook's variable section rather than hard-coding keys.
- The `Kasvikortti.ipynb` notebook looks for keys in notebook variables (or Colab secrets). Follow the notebook cells to configure keys before running searches.

## Privacy & license
- License: MIT — see `LICENSE` (or include a LICENSE file if not yet present).
- Data sources have their own licenses (GBIF, Wikimedia Commons, Trefle, etc.). Respect the source license when reusing images/data.

## Contributing

Contributions are welcome. Ways to help:
- Add or improve notebooks (small, focused notebooks preferred).
- Add a `requirements.txt` or `environment.yml` for reproducible local execution.
- Provide tests or CI for notebooks (e.g., execute notebooks in CI using nbconvert).

Typical workflow:
1. Fork the repo
2. Add or update a notebook in `notebooks/`
3. Open a pull request with a short description and example outputs/screenshots

## Next steps (suggested)
- Add `requirements.txt` and a `LICENSE` file (if missing).
- Add a short `CONTRIBUTING.md` with notebook style guidelines.
- Add a GitHub Action to run notebooks or basic checks.

## Contact
If you want to collaborate or request a notebook topic, open an issue or contact the repository owner.

---
Generated/updated: 2025-11-04
