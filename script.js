// GitHub repository information
const GITHUB_REPO = 'outobecca/botanical-colabs';
const GITHUB_BRANCH = 'main';
const GITHUB_API_BASE = 'https://api.github.com';

// Fetch repository statistics from GitHub API
async function fetchRepoStats() {
    try {
        // Fetch basic repo info
        const repoResponse = await fetch(`${GITHUB_API_BASE}/repos/${GITHUB_REPO}`);
        const repoData = await repoResponse.json();
        
        // Fetch contributors
        const contributorsResponse = await fetch(`${GITHUB_API_BASE}/repos/${GITHUB_REPO}/contributors`);
        const contributorsData = await contributorsResponse.json();
        
        // Fetch latest commit
        const commitsResponse = await fetch(`${GITHUB_API_BASE}/repos/${GITHUB_REPO}/commits?per_page=1`);
        const commitsData = await commitsResponse.json();
        
        // Count notebooks by scanning the tree
        const treeResponse = await fetch(`${GITHUB_API_BASE}/repos/${GITHUB_REPO}/git/trees/${GITHUB_BRANCH}?recursive=1`);
        const treeData = await treeResponse.json();
        const notebookCount = treeData.tree.filter(item => item.path.endsWith('.ipynb')).length;
        
        return {
            stars: repoData.stargazers_count || 0,
            forks: repoData.forks_count || 0,
            watchers: repoData.subscribers_count || 0,
            openIssues: repoData.open_issues_count || 0,
            contributors: contributorsData.length || 0,
            notebooks: notebookCount || 15,
            lastUpdate: commitsData[0]?.commit?.author?.date || repoData.updated_at,
            language: repoData.language || 'Jupyter Notebook',
            size: repoData.size || 0
        };
    } catch (error) {
        console.error('Error fetching repo stats:', error);
        return {
            stars: 0,
            forks: 0,
            watchers: 0,
            openIssues: 0,
            contributors: 1,
            notebooks: 15,
            lastUpdate: new Date().toISOString(),
            language: 'Jupyter Notebook',
            size: 0
        };
    }
}

// Update statistics on the page
async function updateRepoStats() {
    const stats = await fetchRepoStats();
    
    // Update hero stats
    const heroStats = document.querySelectorAll('.hero-stats .stat');
    if (heroStats.length >= 3) {
        // Update notebooks count
        heroStats[1].querySelector('.stat-number').textContent = `${stats.notebooks}+`;
    }
    
    // Add repository stats section if it doesn't exist
    let statsSection = document.getElementById('repo-stats');
    if (!statsSection) {
        const container = document.querySelector('.container');
        if (container) {
            const statsHTML = `
                <section id="repo-stats" class="repo-stats-section">
                    <h2 class="section-title">📊 Repository Statistics</h2>
                    <div class="stats-grid">
                        <div class="stat-card">
                            <div class="stat-icon">⭐</div>
                            <div class="stat-value" id="stat-stars">${stats.stars}</div>
                            <div class="stat-label">Stars</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">🍴</div>
                            <div class="stat-value" id="stat-forks">${stats.forks}</div>
                            <div class="stat-label">Forks</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">👀</div>
                            <div class="stat-value" id="stat-watchers">${stats.watchers}</div>
                            <div class="stat-label">Watchers</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">👥</div>
                            <div class="stat-value" id="stat-contributors">${stats.contributors}</div>
                            <div class="stat-label">Contributors</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">📓</div>
                            <div class="stat-value" id="stat-notebooks">${stats.notebooks}</div>
                            <div class="stat-label">Notebooks</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">🐛</div>
                            <div class="stat-value" id="stat-issues">${stats.openIssues}</div>
                            <div class="stat-label">Open Issues</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">🕐</div>
                            <div class="stat-value" id="stat-updated">${formatDate(stats.lastUpdate)}</div>
                            <div class="stat-label">Last Updated</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">💾</div>
                            <div class="stat-value" id="stat-size">${formatSize(stats.size)}</div>
                            <div class="stat-label">Repository Size</div>
                        </div>
                    </div>
                    <div class="stats-footer">
                        <p>Live data from <a href="https://github.com/${GITHUB_REPO}" target="_blank">GitHub Repository</a></p>
                    </div>
                </section>
            `;
            
            // Insert before the quality section
            const qualitySection = document.getElementById('quality');
            if (qualitySection) {
                qualitySection.insertAdjacentHTML('beforebegin', statsHTML);
            } else {
                container.insertAdjacentHTML('beforeend', statsHTML);
            }
        }
    } else {
        // Update existing stats
        document.getElementById('stat-stars').textContent = stats.stars;
        document.getElementById('stat-forks').textContent = stats.forks;
        document.getElementById('stat-watchers').textContent = stats.watchers;
        document.getElementById('stat-contributors').textContent = stats.contributors;
        document.getElementById('stat-notebooks').textContent = stats.notebooks;
        document.getElementById('stat-issues').textContent = stats.openIssues;
        document.getElementById('stat-updated').textContent = formatDate(stats.lastUpdate);
        document.getElementById('stat-size').textContent = formatSize(stats.size);
    }
}

// Format date for display
function formatDate(dateString) {
    const date = new Date(dateString);
    const now = new Date();
    const diffTime = Math.abs(now - date);
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return 'Today';
    if (diffDays === 1) return 'Yesterday';
    if (diffDays < 7) return `${diffDays} days ago`;
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`;
    if (diffDays < 365) return `${Math.floor(diffDays / 30)} months ago`;
    return `${Math.floor(diffDays / 365)} years ago`;
}

// Format file size
function formatSize(kb) {
    if (kb < 1024) return `${kb} KB`;
    if (kb < 1024 * 1024) return `${(kb / 1024).toFixed(1)} MB`;
    return `${(kb / (1024 * 1024)).toFixed(1)} GB`;
}


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
    updateRepoStats();
    setupSmoothScrolling();
    setupStickyNavbar();
    setupCardMouseTracking();
});
