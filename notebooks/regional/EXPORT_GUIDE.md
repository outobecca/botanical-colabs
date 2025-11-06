# 📤 Export Guide - Finnish Weather Analysis

This guide explains how to export the notebook with **results only** (no code cells) in various formats.

## 🎯 Quick Start

### Option 1: Use Export Buttons (Easiest)
1. Run all cells in the notebook up to Step 8
2. Click the export buttons at Step 8
3. Choose your format: HTML, PDF, Slides, or CSV

### Option 2: Use PowerShell Script (Recommended for Windows)
```powershell
# Export to HTML (results only)
.\export_notebook.ps1 html

# Export to PDF (results only, requires MiKTeX)
.\export_notebook.ps1 pdf

# Export to Slides (results only)
.\export_notebook.ps1 slides

# Export all formats
.\export_notebook.ps1 all
```

### Option 3: Manual Command (Terminal/Command Prompt)
```bash
# Export to HTML (results only - NO CODE CELLS)
jupyter nbconvert --to html --no-input finnish_weather_analysis.ipynb

# Export to PDF (results only - NO CODE CELLS)
jupyter nbconvert --to pdf --no-input finnish_weather_analysis.ipynb

# Export to Slides (results only - NO CODE CELLS)
jupyter nbconvert --to slides --no-input finnish_weather_analysis.ipynb
```

## 🔧 LaTeX/MiKTeX Setup for PDF Export

### Problem: "LaTeX not found" or "pdflatex not found"

### Solution 1: Add MiKTeX to Windows PATH
1. Press `Win + X` → Select "System"
2. Click "Advanced system settings" → "Environment Variables"
3. Under "System variables", find and select "Path"
4. Click "Edit" → "New"
5. Add: `C:\Program Files\MiKTeX\miktex\bin\x64`
6. Click OK on all dialogs
7. **Restart PowerShell/Terminal and Jupyter**

### Solution 2: Verify MiKTeX Installation
Check if pdflatex.exe exists:
```powershell
# Check if file exists
Test-Path "C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex.exe"

# Or check version
& "C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex.exe" --version
```

### Solution 3: Use HTML Export Instead
HTML export works perfectly without LaTeX and looks great:
```bash
jupyter nbconvert --to html --no-input finnish_weather_analysis.ipynb
```

## 📋 What Gets Exported?

### With `--no-input` flag (Results Only):
✅ **INCLUDED:**
- Markdown text and headers
- Charts and visualizations
- Tables and data displays
- Output from print statements
- Analysis results

❌ **EXCLUDED:**
- Python code cells
- Import statements
- Function definitions

### Without `--no-input` flag (Everything):
✅ **INCLUDED:**
- Everything above PLUS
- All Python code cells
- Comments in code

## 📁 Export Formats Explained

### 🌐 HTML Export
- **Best for**: Sharing via email, web hosting, viewing in browser
- **Pros**: Works everywhere, no dependencies, includes all visualizations
- **File size**: ~500KB - 2MB
- **Command**: `jupyter nbconvert --to html --no-input finnish_weather_analysis.ipynb`

### 📄 PDF Export
- **Best for**: Printing, professional reports, archiving
- **Pros**: Fixed layout, looks professional, works offline
- **Cons**: Requires MiKTeX/LaTeX installation
- **File size**: ~300KB - 1MB
- **Command**: `jupyter nbconvert --to pdf --no-input finnish_weather_analysis.ipynb`

### 🎬 Slides Export (reveal.js)
- **Best for**: Presentations, demos, teaching
- **Pros**: Interactive slides, beautiful animations, works in browser
- **File size**: ~500KB - 2MB
- **Command**: `jupyter nbconvert --to slides --no-input finnish_weather_analysis.ipynb`
- **View**: Open `.slides.html` file in any web browser

### 💾 CSV Export
- **Best for**: Data analysis in Excel, R, Python, etc.
- **Pros**: Raw data only, works with any tool
- **File size**: ~50KB - 500KB
- **Command**: Use the CSV export button in Step 8

## 🛠️ Advanced Options

### Include Code Cells in Export
Remove `--no-input` flag:
```bash
jupyter nbconvert --to html finnish_weather_analysis.ipynb
```

### Custom Output Filename
```bash
jupyter nbconvert --to html --no-input --output my_report.html finnish_weather_analysis.ipynb
```

### Execute Before Export
```bash
jupyter nbconvert --to html --no-input --execute finnish_weather_analysis.ipynb
```

### Custom reveal.js Theme (Slides)
```bash
jupyter nbconvert --to slides --no-input --SlidesExporter.reveal_theme=moon finnish_weather_analysis.ipynb
```

Themes: `beige`, `blood`, `moon`, `night`, `serif`, `simple`, `sky`, `solarized`

## ❓ Troubleshooting

### HTML export works but looks broken
- Check browser console for errors
- Try opening in different browser
- Ensure all cells were executed before export

### PDF export fails with "LaTeX not found"
1. Verify MiKTeX is installed: `pdflatex --version`
2. Add MiKTeX to PATH (see instructions above)
3. Restart terminal/Jupyter
4. Try HTML export as alternative

### Charts not showing in export
- Make sure all cells executed successfully
- Check for `plt.show()` in visualization cells
- Try re-running the notebook before export

### Export buttons not working
- Check that nbconvert is installed: `pip install nbconvert`
- For PDF: Check MiKTeX installation
- Look at error messages in output area

### Slides look wrong
- Open the `.slides.html` file in a web browser
- Press `F` for fullscreen mode
- Use arrow keys to navigate
- Press `Esc` for overview

## 📚 Additional Resources

- [Jupyter nbconvert Documentation](https://nbconvert.readthedocs.io/)
- [MiKTeX Installation Guide](https://miktex.org/howto/install-miktex)
- [reveal.js Documentation](https://revealjs.com/)

## 💡 Tips

1. **Always run all cells before exporting** to ensure latest results
2. **HTML export is the most reliable** - use it when PDF fails
3. **Use PowerShell script** for easiest export on Windows
4. **Slides are great for presentations** - open in browser and use arrow keys
5. **CSV export for data only** - use for further analysis in other tools

## 🆘 Still Having Issues?

Check the notebook's Step 8 cell for detailed troubleshooting information and interactive export buttons.
