# Finnish Weather Analysis - Export Helper Script
# Run this script to export the notebook with proper settings
# 
# Usage (PowerShell):
#   .\export_notebook.ps1 html    # Export to HTML (results only)
#   .\export_notebook.ps1 pdf     # Export to PDF (results only, requires MiKTeX)
#   .\export_notebook.ps1 slides  # Export to slides (results only)
#   .\export_notebook.ps1 all     # Export all formats

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet('html', 'pdf', 'slides', 'all')]
    [string]$Format = 'html'
)

$NotebookName = "finnish_weather_analysis.ipynb"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host "  Finnish Weather Analysis - Export Tool" -ForegroundColor Cyan
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host ""

# Check if notebook exists
if (-not (Test-Path $NotebookName)) {
    Write-Host "❌ ERROR: $NotebookName not found in current directory" -ForegroundColor Red
    Write-Host "   Current directory: $PWD" -ForegroundColor Yellow
    exit 1
}

# Check if nbconvert is installed
try {
    $null = jupyter nbconvert --version
    Write-Host "✅ Jupyter nbconvert is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: Jupyter nbconvert not found" -ForegroundColor Red
    Write-Host "   Install with: pip install nbconvert" -ForegroundColor Yellow
    exit 1
}

# Add MiKTeX to PATH if needed (for PDF export)
$MiKTeXPaths = @(
    "C:\Program Files\MiKTeX\miktex\bin\x64",
    "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64",
    "$env:USERPROFILE\AppData\Local\Programs\MiKTeX\miktex\bin\x64"
)

foreach ($path in $MiKTeXPaths) {
    if (Test-Path $path) {
        if ($env:PATH -notlike "*$path*") {
            $env:PATH = "$path;$env:PATH"
            Write-Host "✅ Added MiKTeX to PATH: $path" -ForegroundColor Green
        }
        break
    }
}

# Function to export to specific format
function Export-Notebook {
    param(
        [string]$ExportFormat
    )
    
    Write-Host ""
    Write-Host "📤 Exporting to $ExportFormat..." -ForegroundColor Yellow
    Write-Host "   Format: $ExportFormat (results only - NO CODE CELLS)" -ForegroundColor Cyan
    
    $OutputFile = ""
    
    switch ($ExportFormat) {
        "html" {
            $OutputFile = "finnish_weather_analysis.html"
            jupyter nbconvert --to html --no-input $NotebookName
        }
        "pdf" {
            $OutputFile = "finnish_weather_analysis.pdf"
            Write-Host "   ⚠️  Requires MiKTeX/LaTeX installation" -ForegroundColor Yellow
            jupyter nbconvert --to pdf --no-input $NotebookName
        }
        "slides" {
            $OutputFile = "finnish_weather_analysis.slides.html"
            jupyter nbconvert --to slides --no-input $NotebookName
        }
    }
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✅ Export successful!" -ForegroundColor Green
        Write-Host "   📁 File: $OutputFile" -ForegroundColor Green
        
        # Show file size
        if (Test-Path $OutputFile) {
            $fileSize = (Get-Item $OutputFile).Length / 1KB
            Write-Host "   📊 Size: $([math]::Round($fileSize, 2)) KB" -ForegroundColor Green
        }
    } else {
        Write-Host "   ❌ Export failed!" -ForegroundColor Red
        
        if ($ExportFormat -eq "pdf") {
            Write-Host ""
            Write-Host "   🔧 LaTeX troubleshooting:" -ForegroundColor Yellow
            Write-Host "      1. Verify MiKTeX is installed" -ForegroundColor White
            Write-Host "      2. Add MiKTeX to Windows PATH:" -ForegroundColor White
            Write-Host "         C:\Program Files\MiKTeX\miktex\bin\x64" -ForegroundColor Cyan
            Write-Host "      3. Restart PowerShell after changing PATH" -ForegroundColor White
            Write-Host "      4. Try HTML export instead!" -ForegroundColor White
        }
    }
}

# Export based on format parameter
Write-Host "🎯 Export Settings:" -ForegroundColor Cyan
Write-Host "   • Code cells: HIDDEN (--no-input)" -ForegroundColor White
Write-Host "   • Output cells: VISIBLE" -ForegroundColor White
Write-Host "   • Markdown cells: VISIBLE" -ForegroundColor White
Write-Host "   • Charts/Visualizations: VISIBLE" -ForegroundColor White
Write-Host ""

if ($Format -eq "all") {
    Export-Notebook -ExportFormat "html"
    Export-Notebook -ExportFormat "slides"
    Export-Notebook -ExportFormat "pdf"
} else {
    Export-Notebook -ExportFormat $Format
}

Write-Host ""
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host "  ✅ Export process complete!" -ForegroundColor Green
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "💡 Tips:" -ForegroundColor Yellow
Write-Host "   • HTML export works on any system (no dependencies)" -ForegroundColor White
Write-Host "   • PDF export requires MiKTeX/LaTeX installation" -ForegroundColor White
Write-Host "   • Slides export creates reveal.js presentations" -ForegroundColor White
Write-Host "   • To include code cells, edit this script and remove --no-input" -ForegroundColor White
Write-Host ""
