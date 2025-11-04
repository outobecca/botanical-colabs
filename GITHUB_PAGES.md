# GitHub Pages Setup

This repository includes a static GitHub Pages site that displays the README.md content as a landing page and provides easy access to all notebooks in the repository.

## Features

- **Automatic README rendering**: The landing page automatically renders the README.md file using Marked.js
- **Notebook aggregation**: All notebooks from the `notebooks/` folder are accessible
- **Responsive design**: Mobile-friendly layout with clean, modern styling
- **Colab integration**: Direct links to open notebooks in Google Colab

## Setup Instructions

### Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings**
3. Navigate to **Pages** in the left sidebar
4. Under "Build and deployment":
   - Source: Select **GitHub Actions**
5. Save the settings

The GitHub Actions workflow (`.github/workflows/pages.yml`) will automatically deploy the site when you push to the `main` branch.

### Accessing the Site

Once deployed, your site will be available at:
```
https://<username>.github.io/<repository-name>/
```

For this repository:
```
https://outobecca.github.io/botanical-colabs/
```

## How It Works

### Files

- **index.html**: Main HTML structure
- **style.css**: Styling and responsive design
- **script.js**: JavaScript for loading and rendering README.md
- **_config.yml**: Jekyll configuration (optional)
- **.github/workflows/pages.yml**: GitHub Actions workflow for deployment

### Dynamic Content Loading

The site uses JavaScript to:
1. Fetch the README.md file
2. Convert Markdown to HTML using Marked.js library
3. Render the content dynamically
4. Enhance notebook links with Colab badges

### Notebooks

All notebooks in the `notebooks/` folder are automatically detected and linked in the rendered README. The links are enhanced to:
- Open directly in Google Colab
- Include visual indicators (🚀 emoji)
- Open in a new tab

## Customization

### Changing Colors

Edit `style.css` to customize the color scheme. The main theme color is defined in:
```css
/* Green theme */
header {
    background: linear-gradient(135deg, #2e7d32 0%, #66bb6a 100%);
}
```

### Updating Repository Information

Edit `script.js` to update repository details:
```javascript
const GITHUB_REPO = 'outobecca/botanical-colabs';
const GITHUB_BRANCH = 'main';
```

### Adding Custom Sections

You can enhance the README.md with custom HTML that will be rendered on the GitHub Pages site. The Marked.js library supports:
- Standard Markdown syntax
- Inline HTML
- Code blocks with syntax highlighting
- Tables
- Task lists

## Local Testing

To test the site locally before deploying:

```bash
# Start a simple HTTP server
python3 -m http.server 8000

# Open in your browser
# http://localhost:8000/
```

Or use any static file server of your choice.

## Troubleshooting

### Site Not Updating

1. Check the Actions tab in your repository for deployment status
2. Verify that GitHub Pages is enabled in Settings
3. Clear your browser cache
4. Wait a few minutes for GitHub's CDN to update

### README Not Rendering

1. Verify README.md exists in the repository root
2. Check browser console for JavaScript errors
3. Ensure the Marked.js CDN is accessible

### Notebook Links Not Working

1. Verify notebook files are in the `notebooks/` folder
2. Check that file names match the links in README.md
3. Ensure files have `.ipynb` extension

## Maintenance

### Adding New Notebooks

1. Add your notebook to the `notebooks/` folder
2. Update README.md with notebook description and link
3. Commit and push to `main` branch
4. GitHub Actions will automatically deploy the updated site

### Updating Styles

1. Edit `style.css`
2. Test locally
3. Commit and push to `main` branch
4. GitHub Actions will deploy the changes

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Marked.js Documentation](https://marked.js.org/)
- [Google Colab](https://colab.research.google.com/)
