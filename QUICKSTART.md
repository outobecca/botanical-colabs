# Quick Start Guide

Get started with Botanical Sciences Colab Notebooks in 5 minutes!

## 🚀 For First-Time Users

### Option 1: Try in Google Colab (Recommended)

**No installation needed!**

1. **Open the notebook:**
   - Click: [Plant Card Generator](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/generator-plant-card_fi.ipynb)
   - Or go to [Google Colab](https://colab.research.google.com) and upload the notebook

2. **Set up API keys** (optional but recommended):
   - Click 🔑 Secrets in the left sidebar
   - Add these secrets:
     - `GOOGLE_API_KEY` — [Get from Google AI Studio](https://aistudio.google.com/app/apikey)
     - `TREFLE_API_KEY` — [Get from Trefle.io](https://trefle.io)
     - `LAJI_TOKEN` — [Request from Laji.fi](https://laji.fi/en/about/13)
   - See [API_SETUP.md](API_SETUP.md) for detailed instructions

3. **Run the notebook:**
   - Click ▶️ on the first cell to install packages
   - Fill in the plant name (e.g., "Quercus robur")
   - Select data sources
   - Click "Tallenna asetukset" (Save settings)
   - Run remaining cells in order

4. **View your plant card!** 🌿

---

### Option 2: Run Locally

**Requirements:** Python 3.8+

```powershell
# Clone the repository
git clone https://github.com/outobecca/botanical-colabs.git
cd botanical-colabs

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

Then open `notebooks/generator-plant-card_fi.ipynb`

---

## 📝 Example: Create Your First Plant Card

### Step 1: Configure

```python
# In the configuration cell, enter:
kasvin_nimi = "Quercus robur"  # English Oak

# Select data sources (checkboxes):
✅ GBIF taksonomia
✅ Wikimedia kasvikuvitus
✅ Wikipedia tiivistelmä
□ Gemini AI-kuvaus (requires API key)
```

### Step 2: Run

Execute cells in order (Shift + Enter):
1. ✅ Setup and installation
2. ✅ Helper functions
3. ✅ Data fetching
4. ✅ Visualization

### Step 3: Results

You'll get:
- 📊 Taxonomy table (Kingdom, Family, Genus, etc.)
- 🌱 Growth characteristics (if Trefle available)
- 🗺️ Distribution data
- 🎨 Botanical illustrations
- 📖 Citations and sources

---

## 🎯 Common Use Cases

### For Researchers
```python
# Study species distribution
kasvin_nimi = "Pinus sylvestris"
# Enable: GBIF occurrence + distribution
```

### For Educators
```python
# Create teaching materials
kasvin_nimi = "Malus domestica"
# Enable: All sources for comprehensive overview
```

### For Gardeners
```python
# Plan your garden
kasvin_nimi = "Lavandula angustifolia"
# Enable: Trefle (pH, growth form)
```

---

## ⚡ Tips for Success

### ✅ DO:
- Use **scientific names** (Latin binomial: *Genus species*)
- Check spelling carefully
- Start with common species to test
- Enable multiple data sources for complete info
- Save results before closing browser

### ❌ DON'T:
- Use common names only
- Expect instant results (APIs take time)
- Run all cells at once (run sequentially)
- Commit API keys to Git
- Ignore error messages

---

## 🔧 Troubleshooting

### "Secret not found"
- Check spelling of secret names
- Ensure toggle is ON in Colab Secrets
- Restart runtime: Runtime → Restart runtime

### "No data found"
- Verify scientific name spelling
- Try alternative name (synonym)
- Check if species exists in GBIF
- Some rare species may have limited data

### "API timeout"
- Wait a moment and retry
- Check internet connection
- Some APIs may be temporarily down

### "Rate limit exceeded"
- You've made too many requests
- Wait before retrying
- Consider caching results

---

## 📚 Learn More

- **Full documentation:** [README.md](README.md)
- **API setup:** [API_SETUP.md](API_SETUP.md)
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Version history:** [CHANGELOG.md](CHANGELOG.md)

---

## 🆘 Get Help

1. **Check documentation** — Most questions answered in guides above
2. **Search existing issues** — [GitHub Issues](https://github.com/outobecca/botanical-colabs/issues)
3. **Open new issue** — Provide details (error message, steps to reproduce)
4. **Join discussions** — [GitHub Discussions](https://github.com/outobecca/botanical-colabs/discussions)

---

## 🎓 Next Steps

After your first plant card:

1. **Try different species:**
   - Common: *Quercus robur*, *Betula pendula*
   - Rare: *Primula scotica*, *Welwitschia mirabilis*
   - Exotic: *Dionaea muscipula*, *Rafflesia arnoldii*

2. **Enable AI summaries:**
   - Get Google Gemini API key
   - See instant AI-generated descriptions

3. **Export your results:**
   - Right-click plant card → Save as PDF
   - Or copy data to your own documents

4. **Contribute back:**
   - Found a bug? Report it!
   - Have ideas? Share them!
   - Want to improve? Submit a PR!

---

**Ready to explore? [Open the notebook in Colab →](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/generator-plant-card_fi.ipynb)**

Happy botanizing! 🌿
