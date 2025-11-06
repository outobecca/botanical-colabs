# Generic Notebook Export Helper Script
# Exports a given Jupyter notebook to various formats.

param(
    [Parameter(Mandatory=$true)]
    [string]$NotebookFile,

    [Parameter(Mandatory=$false)]
    [ValidateSet('html', 'pdf', 'slides', 'all')]
    [string]$Format = 'html'
)

$NotebookName = Split-Path -Leaf $NotebookFile
$NotebookDir = Split-Path -Path $NotebookFile

Push-Location $NotebookDir

Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host "  Jupyter Notebook Export Tool" -ForegroundColor Cyan
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host ""

# Check if notebook exists
if (-not (Test-Path $NotebookName)) {
    Write-Host "❌ ERROR: $NotebookName not found in $NotebookDir" -ForegroundColor Red
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

# Function to export to specific format
function Export-Notebook {
    param(
        [string]$ExportFormat
    )
    
    Write-Host ""
    Write-Host "📤 Exporting to $ExportFormat..." -ForegroundColor Yellow
    
    $OutputFile = ""
    $BaseName = $NotebookName -replace '.ipynb', ''

    switch ($ExportFormat) {
        "html" {
            $OutputFile = "$($BaseName).html"
            jupyter nbconvert --to html --config nbconvert_config.py $NotebookName
        }
        "pdf" {
            $OutputFile = "$($BaseName).pdf"
            Write-Host "   ⚠️  Requires MiKTeX/LaTeX installation" -ForegroundColor Yellow
            jupyter nbconvert --to pdf --config nbconvert_config.py $NotebookName
        }
        "slides" {
            $OutputFile = "$($BaseName).slides.html"
            jupyter nbconvert --to slides --config nbconvert_config.py $NotebookName
        }
    }
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✅ Export successful!" -ForegroundColor Green
        Write-Host "   📁 File: $OutputFile" -ForegroundColor Green
    } else {
        Write-Host "   ❌ Export failed!" -ForegroundColor Red
    }
}

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

Pop-Location
