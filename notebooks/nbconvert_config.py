# Jupyter nbconvert configuration for Botanical Colab Notebooks
# This file configures how notebooks are exported to HTML, PDF, and Slides.
# It is designed to be generic for all notebooks in this project.

c = get_config()

# ============================================================================
# HIDE CODE CELLS - Export only results (output, markdown, visualizations)
# ============================================================================
# By default, code cells are excluded from the output.
# To override this, use the --no-input=False flag on the command line.
# Example: jupyter nbconvert --to html --no-input=False "path/to/your/notebook.ipynb"

c.TemplateExporter.exclude_input = True
c.HTMLExporter.exclude_input = True
c.PDFExporter.exclude_input = True
c.SlidesExporter.exclude_input = True

# ============================================================================
# PDF EXPORT SETTINGS (LaTeX/MiKTeX configuration)
# ============================================================================

# Set LaTeX engine
c.PDFExporter.latex_command = ['pdflatex', '{filename}']

# Add common MiKTeX paths (Windows) to the environment
import os
if os.name == 'nt':
    miktex_paths = [
        r"C:\Program Files\MiKTeX\miktex\bin\x64",
        os.path.expanduser(r"~\AppData\Local\Programs\MiKTeX\miktex\bin\x64")
    ]
    
    path_env = os.environ.get('PATH', '')
    for miktex_path in miktex_paths:
        if os.path.exists(miktex_path) and miktex_path not in path_env:
            os.environ['PATH'] = miktex_path + os.pathsep + path_env
            print(f"Added MiKTeX to PATH: {miktex_path}")
            break

# ============================================================================
# HTML EXPORT SETTINGS
# ============================================================================

# Embed images directly in the HTML file for portability
c.HTMLExporter.embed_images = True
c.HTMLExporter.template_name = 'classic'

# ============================================================================
# SLIDES EXPORT SETTINGS (reveal.js)
# ============================================================================

c.SlidesExporter.reveal_theme = 'serif'
c.SlidesExporter.reveal_transition = 'slide'
c.SlidesExporter.reveal_scroll = True

# ============================================================================
# GENERAL SETTINGS
# ============================================================================

# Do not execute the notebook before exporting.
# Assumes the user has already run the notebook.
c.ExecutePreprocessor.enabled = False
c.ExecutePreprocessor.timeout = 600

