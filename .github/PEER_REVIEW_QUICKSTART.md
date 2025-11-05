# Quick Reference: Peer Review System

## 🚀 Quick Start for Reviewers

### Step 1: Find a Notebook to Review
- Browse [Pull Requests with label `peer-review-request`](https://github.com/outobecca/botanical-colabs/pulls?q=label%3Apeer-review-request)
- Or check `.github/peer-review.json` for notebooks needing reviews

### Step 2: Test the Notebook
```bash
# Open in Google Colab
# Click: File → Open notebook → GitHub
# Paste PR URL or notebook path
# Run all cells
```

### Step 3: Fill Out Review
Use template: `.github/PULL_REQUEST_TEMPLATE/peer_review.md`

### Step 4: Add to Database
Edit `.github/peer-review.json`:
```json
{
  "reviewer": "your-github-username",
  "date": "2025-11-05",
  "vote": "approve",
  "category": "accuracy",
  "comment": "Data sources verified, results reproducible"
}
```

### Step 5: Commit and Push
```bash
git add .github/peer-review.json
git commit -m "review: approve notebook for accuracy"
git push
```

---

## 📋 Review Checklist

### Before Approving
- [ ] Notebook runs without errors in Colab
- [ ] Data sources are authoritative
- [ ] Results are reproducible
- [ ] Code follows best practices
- [ ] Documentation is clear
- [ ] Citations are present
- [ ] No conflicts of interest

---

## 🏆 Badge Meanings

| Badge | What It Means |
|-------|---------------|
| ![Peer Reviewed](https://img.shields.io/badge/Peer_Reviewed-✓-success) | **Verified** — 2+ reviewers approved |
| ![In Review](https://img.shields.io/badge/In_Review-1/2-yellow) | **Being Reviewed** — Needs more reviews |
| ![AI Generated](https://img.shields.io/badge/AI_Generated-GitHub_Copilot-blue) | **AI-Assisted** — Created with AI help |
| ![accuracy ✓](https://img.shields.io/badge/accuracy-✓-green) | **Accurate** — Scientific accuracy verified |

---

## 📊 Review Categories

| Category | What to Check |
|----------|---------------|
| **🎯 Accuracy** | Data sources, taxonomy, results correctness |
| **🔧 Methodology** | Code quality, algorithms, error handling |
| **📝 Documentation** | Clarity, citations, instructions |
| **👥 Usability** | Ease of use, interface, error messages |
| **🔁 Reproducibility** | Consistency, dependencies, repeatability |

---

## 🔄 Review States

```
pending → in_review → approved
                   ↓
                declined → needs revision → in_review
```

---

## 💡 Tips

### Good Review Comments
✅ "Data sources verified against GBIF API, taxonomy correct"  
✅ "Tested with 50+ species, all results reproducible"  
✅ "Code follows PEP 8, proper error handling implemented"

### Poor Review Comments
❌ "Looks good"  
❌ "LGTM"  
❌ "Approved"

---

## 🔗 Quick Links

- **[Full Guidelines](PEER_REVIEW.md)** — Comprehensive documentation
- **[Review Database](.github/peer-review.json)** — Current review status
- **[Review Template](.github/PULL_REQUEST_TEMPLATE/peer_review.md)** — Submission form
- **[Contributing Guide](CONTRIBUTING.md)** — How to contribute
- **[Open Reviews](https://github.com/outobecca/botanical-colabs/pulls?q=label%3Apeer-review-request)** — Notebooks needing review

---

## ⚡ Common Tasks

### Mark Notebook as AI-Generated
```json
"metadata": {
  "ai_generated": true,
  "ai_assistant": "GitHub Copilot"
}
```

### Update Review Status to Approved
```json
"metadata": {
  "peer_reviewed": true,
  "review_status": "approved",
  "approval_date": "2025-11-05",
  "current_reviews": 2
}
```

### Decline a Review
```json
{
  "vote": "decline",
  "comment": "Needs improvement: data source not authoritative, consider using GBIF instead"
}
```

---

## 📞 Get Help

- **Questions:** [GitHub Discussions](https://github.com/outobecca/botanical-colabs/discussions)
- **Issues:** [Report Problems](https://github.com/outobecca/botanical-colabs/issues)
- **Email:** Contact maintainers

---

**Last Updated:** November 5, 2025
