// GitHub repository information
const GITHUB_REPO = 'outobecca/botanical-colabs';
const GITHUB_BRANCH = 'main';

// Load and render README content
async function loadReadme() {
    try {
        const response = await fetch('README.md');
        const markdown = await response.text();
        
        // Convert markdown to HTML using marked.js
        const html = marked.parse(markdown);
        
        // Render the content
        document.getElementById('content').innerHTML = html;
        
        // Enhance notebook links
        enhanceNotebookLinks();
    } catch (error) {
        console.error('Error loading README:', error);
        document.getElementById('content').innerHTML = '<p class="error">Failed to load content. Please try again later.</p>';
    }
}

// Enhance notebook links to include Colab badges and links
function enhanceNotebookLinks() {
    const content = document.getElementById('content');
    
    // Find all links to .ipynb files in the notebooks folder
    const links = content.querySelectorAll('a[href*="notebooks/"][href$=".ipynb"]');
    
    links.forEach(link => {
        const notebookPath = link.getAttribute('href');
        const notebookName = notebookPath.split('/').pop();
        
        // Create Colab link
        const colabUrl = `https://colab.research.google.com/github/${GITHUB_REPO}/blob/${GITHUB_BRANCH}/${notebookPath}`;
        
        // If the link text is "Direct link", update it to open in Colab
        if (link.textContent.includes('Direct link')) {
            link.href = colabUrl;
            link.target = '_blank';
            link.rel = 'noopener noreferrer';
        }
    });
    
    // Also enhance any existing Colab links
    const colabLinks = content.querySelectorAll('a[href*="colab.research.google.com"]');
    colabLinks.forEach(link => {
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
        
        // Add Colab badge icon if it's a "Direct link" or "Open in Colab"
        if (link.textContent.includes('Direct link') || link.textContent.includes('Open in Colab')) {
            link.innerHTML = '🚀 ' + link.textContent;
        }
    });
}

// Fetch and display notebooks dynamically
async function loadNotebooks() {
    try {
        // GitHub API endpoint to list repository contents
        const apiUrl = `https://api.github.com/repos/${GITHUB_REPO}/contents/notebooks`;
        
        const response = await fetch(apiUrl);
        const files = await response.json();
        
        // Filter for .ipynb files
        const notebooks = files.filter(file => file.name.endsWith('.ipynb'));
        
        // Create notebook cards (this could be used to add a separate notebooks section)
        console.log('Found notebooks:', notebooks.map(n => n.name));
        
    } catch (error) {
        console.error('Error loading notebooks:', error);
    }
}

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
    loadReadme();
    loadNotebooks();
});
