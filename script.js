// GitHub repository information
const GITHUB_REPO = 'outobecca/botanical-colabs';
const GITHUB_BRANCH = 'main';

// Load and render README content
async function loadReadme() {
    try {
        // Try to fetch README.md from current directory first, then from root
        let response;
        try {
            response = await fetch('./README.md');
            if (!response.ok) throw new Error('Not found in current dir');
        } catch {
            response = await fetch('/README.md');
        }
        
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

// Load blog posts for the home page
async function loadBlogPosts() {
    const blogContainer = document.getElementById('blog-posts');
    if (!blogContainer) return;
    
    // Static blog posts for now
    // In a full Jekyll setup, this would be generated server-side
    const posts = [
        {
            title: 'Welcome to Botanical Colabs Blog',
            date: 'November 5, 2025',
            excerpt: 'We\'re launching a botanical science blog to showcase how these notebooks are used in real research. Stay tuned for case studies, tutorials, and research highlights!',
            link: 'blog/'
        }
    ];
    
    blogContainer.innerHTML = posts.map(post => `
        <div class="blog-card">
            <div class="blog-date">${post.date}</div>
            <h3><a href="${post.link}" style="color: inherit; text-decoration: none;">${post.title}</a></h3>
            <p>${post.excerpt}</p>
            <a href="${post.link}" class="category-link">Read More →</a>
        </div>
    `).join('');
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
            link.textContent = '🚀 ' + link.textContent;
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

// Smooth scrolling for anchor links
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Sticky navbar on scroll
function setupStickyNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.style.boxShadow = '0 8px 20px rgba(0, 0, 0, 0.6)';
            navbar.classList.add('scrolled');
        } else {
            navbar.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.4)';
            navbar.classList.remove('scrolled');
        }
    });
}

// Add mouse tracking for category cards
function setupCardMouseTracking() {
    const cards = document.querySelectorAll('.category-card');
    
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = ((e.clientX - rect.left) / rect.width) * 100;
            const y = ((e.clientY - rect.top) / rect.height) * 100;
            
            card.style.setProperty('--mouse-x', `${x}%`);
            card.style.setProperty('--mouse-y', `${y}%`);
        });
    });
}

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
    loadReadme();
    loadNotebooks();
    loadBlogPosts();
    setupSmoothScrolling();
    setupStickyNavbar();
    setupCardMouseTracking();
});
