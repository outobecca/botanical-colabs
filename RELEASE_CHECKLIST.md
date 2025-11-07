# Release Checklist

This checklist outlines the steps to be taken before a new release of the Botanical Sciences Colab Notebooks.

## Pre-release Steps

- [ ] **Review all open issues and pull requests:** Ensure all critical bugs are fixed and important features are merged.
- [ ] **Update dependencies:** Run `pip install -r requirements.txt` and ensure all dependencies are up-to-date and compatible.
- [ ] **Run all tests:** Execute all notebook tests and ensure they pass.
- [ ] **Verify documentation:** Check that all new features are documented and existing documentation is up-to-date.
- [ ] **Update `CHANGELOG.md`:** Add an entry for the new release, summarizing changes, new features, and bug fixes.
- [ ] **Update version number:** Increment the version number in relevant files (e.g., `pyproject.toml` if applicable).
- [ ] **Generate previews:** Ensure all notebook previews are generated and up-to-date.
- [ ] **Check for AI-generated content disclaimers:** Verify that all AI-generated content has appropriate disclaimers.
- [ ] **Review data source citations:** Ensure all data sources are properly cited with access dates and DOIs.

## Release Steps

- [ ] **Create a new Git tag:** Tag the release commit with the new version number (e.g., `v1.0.0`).
- [ ] **Create a GitHub Release:** Draft a new release on GitHub, including release notes and linking to the `CHANGELOG.md` entry.
- [ ] **Announce the release:** Share the news on relevant channels (e.g., project website, social media).

## Post-release Steps

- [ ] **Monitor for issues:** Keep an eye on bug reports and user feedback after the release.
- [ ] **Plan for the next release:** Start planning for future features and improvements.
