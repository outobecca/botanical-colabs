# Jupyter nbconvert configuration for Finnish Weather Analysis
# This file configures how notebooks are exported to HTML, PDF, and Slides
# Place this file in the same directory as your notebook

c = get_config()

# ============================================================================
# HIDE CODE CELLS - Export only results (output, markdown, visualizations)
# ============================================================================

# Exclude input cells (code) from all exports
c.TemplateExporter.exclude_input = True

# Alternative: Use a preprocessor to remove code cells
c.HTMLExporter.exclude_input = True
c.PDFExporter.exclude_input = True
c.SlidesExporter.exclude_input = True

# ============================================================================
# PDF EXPORT SETTINGS (LaTeX/MiKTeX configuration)
# ============================================================================

# Set LaTeX engine - use pdflatex from MiKTeX
c.PDFExporter.latex_command = ['pdflatex', '{filename}']

# Add common MiKTeX paths (Windows)
import os
miktex_paths = [
    r"C:\Program Files\MiKTeX\miktex\bin\x64",
    r"C:\Users\pekka\AppData\Local\Programs\MiKTeX\miktex\bin\x64",
    os.path.expanduser(r"~\AppData\Local\Programs\MiKTeX\miktex\bin\x64")
]

# Add MiKTeX to PATH if found
for miktex_path in miktex_paths:
    if os.path.exists(miktex_path):
        current_path = os.environ.get('PATH', '')
        if miktex_path not in current_path:
            os.environ['PATH'] = miktex_path + os.pathsep + current_path
        break

# ============================================================================
# HTML EXPORT SETTINGS
# ============================================================================

# Embed images in HTML (no external files needed)
c.HTMLExporter.embed_images = True

# Use full HTML template
c.HTMLExporter.template_name = 'classic'

# ============================================================================
# SLIDES EXPORT SETTINGS (reveal.js)
# ============================================================================

# Use reveal.js template
c.SlidesExporter.reveal_theme = 'serif'  # Options: beige, blood, moon, night, serif, simple, sky, solarized
c.SlidesExporter.reveal_transition = 'slide'  # Options: none, fade, slide, convex, concave, zoom
c.SlidesExporter.reveal_scroll = True  # Enable scrolling in slides

# ============================================================================
# GENERAL SETTINGS
# ============================================================================

# Execute notebook before exporting (optional - set to False if already executed)
c.ExecutePreprocessor.enabled = False

# Timeout for cell execution (if executing)
c.ExecutePreprocessor.timeout = 600

# ============================================================================
# USAGE EXAMPLES
# ============================================================================
"""
With this configuration file in the same directory as your notebook:

# Export to HTML (results only - no code)
jupyter nbconvert --to html finnish_weather_analysis.ipynb

# Export to PDF (results only - no code, requires MiKTeX)
jupyter nbconvert --to pdf finnish_weather_analysis.ipynb

# Export to Slides (results only - no code)
jupyter nbconvert --to slides finnish_weather_analysis.ipynb

# Override config to INCLUDE code cells:
jupyter nbconvert --to html --no-input=False finnish_weather_analysis.ipynb

# Or use the buttons in Step 8 of the notebook!
"""
