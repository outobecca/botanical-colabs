# API Keys Setup Guide

This guide helps you obtain and configure API keys for the botanical notebooks.

## 🔑 Required API Keys

### Free APIs (No Key Required)
- ✅ **GBIF** - Global Biodiversity Information Facility
- ✅ **Wikipedia** - Encyclopedia summaries
- ✅ **Wikimedia Commons** - Botanical illustrations
- ✅ **iNaturalist** - Community observations
- ✅ **Encyclopedia of Life** - Ecological data

### APIs Requiring Keys

#### 1. Google Gemini API (for AI summaries)

**Cost:** Free tier available (60 requests/minute)

**Setup:**
1. Go to https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (starts with `AIza...`)
5. In Colab: Click 🔑 Secrets → Add Secret
   - Name: `GOOGLE_API_KEY`
   - Value: [paste your key]

**Documentation:** https://ai.google.dev/tutorials/setup

---

#### 2. Trefle API (plant database)

**Cost:** Free tier (120 requests/day)

**Setup:**
1. Go to https://trefle.io
2. Create account
3. Go to https://trefle.io/profile
4. Generate API token
5. Copy the token
6. In Colab: Click 🔑 Secrets → Add Secret
   - Name: `TREFLE_API_KEY`
   - Value: [paste your token]

**Documentation:** https://docs.trefle.io

**Note:** Trefle is transitioning to a new platform. Check current status.

---

#### 3. Laji.fi API (Finnish biodiversity)

**Cost:** Free

**Setup:**
1. Go to https://laji.fi/en/about/13
2. Request API access (email: helpdesk@laji.fi)
3. Provide:
   - Name and organization
   - Intended use
   - Email address
4. Receive token via email
5. In Colab: Click 🔑 Secrets → Add Secret
   - Name: `LAJI_TOKEN`
   - Value: [paste your token]

**Documentation:** https://api.laji.fi/explorer/

---

#### 4. Biodiversity Heritage Library (BHL)

**Cost:** Free

**Setup:**
1. Go to https://www.biodiversitylibrary.org/docs/api3.html
2. Request API key via form
3. Receive key via email
4. In Colab: Click 🔑 Secrets → Add Secret
   - Name: `BHL_API_KEY`
   - Value: [paste your key]

**Documentation:** https://www.biodiversitylibrary.org/api2/docs/

**Note:** BHL is optional for historical botanical illustrations.

---

## 📱 Using Secrets in Google Colab

### Step-by-step:

1. **Open your notebook in Colab**
   - https://colab.research.google.com

2. **Access Secrets panel**
   - Click the 🔑 key icon on the left sidebar
   - Or go to: Tools → Secrets

3. **Add each secret**
   - Click "+ Add new secret"
   - Enter name exactly as shown above
   - Paste the API key/token
   - Toggle "Notebook access" ON

4. **Verify in code**
   ```python
   from google.colab import userdata
   
   # Test if key is accessible
   try:
       key = userdata.get('GOOGLE_API_KEY')
       print("✅ Key found")
   except:
       print("❌ Key not found")
   ```

---

## 🏠 Using Environment Variables Locally

If running notebooks locally (not in Colab):

### Option 1: .env file (recommended)

1. Create `.env` file in project root:
   ```bash
   GOOGLE_API_KEY=your_key_here
   TREFLE_API_KEY=your_key_here
   LAJI_TOKEN=your_token_here
   BHL_API_KEY=your_key_here
   ```

2. Install python-dotenv:
   ```bash
   pip install python-dotenv
   ```

3. Load in notebook:
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
   ```

**⚠️ Important:** Add `.env` to `.gitignore` (already done)

### Option 2: System environment variables

**Windows PowerShell:**
```powershell
$env:GOOGLE_API_KEY = "your_key_here"
$env:TREFLE_API_KEY = "your_key_here"
```

**Linux/Mac:**
```bash
export GOOGLE_API_KEY="your_key_here"
export TREFLE_API_KEY="your_key_here"
```

---

## 🔒 Security Best Practices

### ✅ DO:
- Store keys in Colab Secrets or .env files
- Add `.env` to `.gitignore`
- Regenerate keys if accidentally exposed
- Use separate keys for development/production
- Review API usage regularly

### ❌ DON'T:
- Hardcode keys in notebooks
- Commit keys to Git
- Share keys in screenshots
- Use same key across multiple projects
- Ignore rate limits

---

## 🚨 If You Accidentally Expose a Key

1. **Immediately revoke** the key:
   - Gemini: https://aistudio.google.com/app/apikey
   - Trefle: https://trefle.io/profile
   - Others: Contact provider

2. **Generate new key**

3. **Update in your secrets**

4. **If committed to Git:**
   ```bash
   # Remove from history (use with caution)
   git filter-branch --force --index-filter \
   "git rm --cached --ignore-unmatch path/to/file" \
   --prune-empty --tag-name-filter cat -- --all
   ```

---

## 📊 API Rate Limits

| API | Free Tier Limit | Notes |
|-----|----------------|-------|
| Gemini | 60 req/min | 1,500 req/day |
| Trefle | 120 req/day | May change |
| Laji.fi | Varies | Contact for details |
| BHL | No strict limit | Be respectful |
| GBIF | No limit | May throttle heavy use |

**Tip:** Cache results to avoid repeated API calls for the same species.

---

## ❓ Troubleshooting

### "Secret not found" error
- Check spelling (exact match required)
- Ensure "Notebook access" toggle is ON
- Restart runtime and try again

### "Invalid API key" error
- Verify key is correct (no extra spaces)
- Check if key is active (not revoked)
- Ensure key has proper permissions

### "Rate limit exceeded"
- Wait before retrying
- Implement exponential backoff
- Cache previous results
- Consider upgrading to paid tier

### API returns no data
- Verify species name spelling
- Check if species exists in that database
- Try alternative name (synonym)
- Check API status page

---

## 🆘 Support

- **Gemini API**: https://ai.google.dev/docs
- **Trefle**: helpdesk via website
- **Laji.fi**: helpdesk@laji.fi
- **BHL**: https://www.biodiversitylibrary.org/contact
- **General**: Open an issue in this repository

---

Last updated: 2025-11-04

---

## 5. GitHub API Token & Gemini API Key for AI Chatbox

**Cost:** Free

**Purpose:** The AI Chatbox functionality relies on two secrets to be set in your repository settings:

1.  **`GITHUB_TOKEN`:** This is a pre-configured secret in your repository that allows the GitHub Action to commit the generated notebook to the repository.
2.  **`GEMINI_API_KEY`:** This is the API key for the Google Gemini API, which is used to generate the notebook content.

**Setup:**

1.  **`GITHUB_TOKEN`:** This secret is automatically created by GitHub and is available to all workflows. You do not need to do anything to set it up.

2.  **`GEMINI_API_KEY`:**
    1.  Go to https://aistudio.google.com/app/apikey
    2.  Sign in with your Google account.
    3.  Click "Create API Key".
    4.  Copy the key (starts with `AIza...`).
    5.  In your GitHub repository, go to `Settings` > `Secrets and variables` > `Actions`.
    6.  Click `New repository secret`.
    7.  Set the name to `GEMINI_API_KEY` and paste the key as the value.

**How it works:**

1.  When a user submits a prompt in the chatbox on the GitHub Pages site, a new GitHub Issue is created with the label `ai-request`.
2.  This triggers the `ai-notebook-generator.yml` GitHub Action.
3.  The action uses the `GEMINI_API_KEY` to generate the notebook content based on the issue body.
4.  The action then uses the `GITHUB_TOKEN` to commit the new notebook to the `notebooks/examples/` directory.
