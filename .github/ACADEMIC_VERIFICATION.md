# 🎓 Academic Verification Guide

## Overview

This repository requires academic verification for all contributors to ensure the scientific rigor and credibility of our botanical research notebooks.

## 🎯 Why Verification?

Our notebooks are used for:
- 🔬 Scientific research and publication
- 🎓 Educational purposes at universities
- 🌱 Conservation decisions
- 🌾 Agricultural planning
- 📊 Data-driven policy making

We need to ensure all contributions meet academic standards and come from qualified individuals.

## ✅ Who Can Be Verified?

We verify contributors who are affiliated with accredited institutions and have expertise in relevant fields:

### Eligible Categories

| Category | Requirements | Examples |
|----------|--------------|----------|
| **Faculty** | Tenure-track or tenured position | Professor, Associate Professor, Assistant Professor |
| **Researchers** | Active research position | Research Scientist, Principal Investigator, Research Fellow |
| **Postdocs** | Postdoctoral position | Postdoctoral Researcher, Postdoctoral Fellow |
| **Graduate Students** | Enrolled in Masters/PhD program | PhD Student, Masters Student (with advisor confirmation) |
| **Scientists** | Professional position at recognized institution | Curator, Conservation Scientist, Research Botanist |
| **Lecturers** | Teaching position with research involvement | Lecturer, Senior Lecturer |

### Eligible Institutions

- ✅ Accredited universities and colleges
- ✅ Research institutes and laboratories
- ✅ Botanical gardens with research programs
- ✅ Natural history museums
- ✅ Government research agencies (USDA, USGS, etc.)
- ✅ Conservation organizations with research divisions
- ✅ International research centers

## 📋 Verification Process

### Step 1: Submit Your PR

Create your pull request as normal. The verification workflow will automatically:
- Detect that you're a new contributor
- Add the `verification-required` label
- Post a comment with instructions

### Step 2: Provide Your Credentials

**Option A: Email Verification** (Recommended for privacy)

Email: `botanical-research@example.com` (Update with actual contact)

Include:
```
Subject: Academic Verification - [Your GitHub Username]

Full Name: Dr. Jane Smith
GitHub Username: janesmith
Institution: University of Botanical Sciences
Department: Plant Biology
Role: Associate Professor
Email: jane.smith@university.edu
ORCID: 0000-0002-1234-5678
Profile: https://university.edu/faculty/janesmith
Google Scholar: https://scholar.google.com/citations?user=xxxxx
Research Areas: Plant taxonomy, molecular phylogenetics, conservation biology

Brief bio:
I'm an associate professor specializing in plant systematics with 15 years 
of research experience. My work focuses on tropical plant diversity and 
conservation genomics.
```

**Option B: Public Verification** (Comment on PR)

Comment on your PR with:
```markdown
## Academic Verification Request

**Institution:** University of Botanical Sciences
**Role:** Associate Professor
**Email:** jane.smith@university.edu
**Profile:** https://university.edu/faculty/janesmith
**Research:** Plant taxonomy, conservation biology

I confirm my affiliation and request verification for contributing to this project.
```

**Option C: Advisor Verification** (For students)

Have your advisor comment on your PR:
```markdown
## Advisor Verification

I confirm that @studentusername is a PhD student in my laboratory at 
University of Botanical Sciences. They are qualified to contribute to 
this botanical research project.

Dr. John Advisor
Professor of Plant Biology
john.advisor@university.edu
https://university.edu/faculty/johnadvisor
```

### Step 3: Verification Review

A repository maintainer will:
1. ✅ Verify your institutional affiliation (check university website, ORCID, Google Scholar)
2. ✅ Confirm your role and expertise
3. ✅ Add you to `.github/academic-contributors.json`
4. ✅ Remove the `verification-required` label
5. ✅ Add the `verified-academic` label
6. ✅ Approve your PR for review

**Timeline:** 1-3 business days

### Step 4: Future Contributions

Once verified:
- ✅ All future PRs automatically approved for verification
- ✅ Your name appears in the contributors list
- ✅ You can contribute without re-verification
- ✅ You may be invited as a repository collaborator

## 📝 Contributor Database

Verified contributors are stored in `.github/academic-contributors.json`:

```json
{
  "github_username": "janesmith",
  "full_name": "Dr. Jane Smith",
  "institution": "University of Botanical Sciences",
  "department": "Plant Biology",
  "role": "Associate Professor",
  "orcid": "0000-0002-1234-5678",
  "email": "jane.smith@university.edu",
  "profile_url": "https://university.edu/faculty/janesmith",
  "research_interests": [
    "Plant taxonomy",
    "Molecular phylogenetics",
    "Conservation biology"
  ],
  "verified_date": "2025-11-05",
  "verified_by": "outobecca",
  "notes": "Expert in tropical plant diversity"
}
```

## 🔒 Privacy & Data Protection

### What We Collect
- GitHub username (public)
- Full name (you choose visibility)
- Institution and role (public)
- ORCID (optional, public if provided)
- Email (private, only for verification)
- Profile links (you choose visibility)

### What We Display
- GitHub username on contributors page
- Institution and role (in verification badge)
- ORCID link (if you provide it)

### What We Keep Private
- Email addresses (never published)
- Personal notes from verification
- Any sensitive information you mark as private

### Your Rights
- Request removal from contributors list
- Update your information
- Change visibility settings
- Withdraw verification

## 🎓 ORCID Integration

We strongly encourage using ORCID iDs for verification:

### Benefits of ORCID
- ✅ Persistent digital identifier for researchers
- ✅ Links all your research outputs
- ✅ Internationally recognized
- ✅ Free to obtain
- ✅ Simplifies verification process

### Get Your ORCID
1. Visit https://orcid.org
2. Register for free
3. Add your institutional affiliation
4. Link your publications
5. Include in verification request

## 🌍 International Contributors

We welcome international contributors! 

### Language Support
- Primary language: English
- Notebooks can be multilingual
- Documentation should include English abstracts

### Institution Verification
- We verify institutions worldwide
- Provide English translation of credentials if needed
- Include international profile links (ResearchGate, Google Scholar)

## ⚠️ Common Issues

### "My institution isn't listed"

**Solution:** Email us with:
- Institution's official website
- Evidence of accreditation/recognition
- Your official profile page

We'll review and add recognized institutions.

### "I'm a citizen scientist with expertise"

**Solution:** We appreciate citizen science! However, for this repository:
- Contributions require institutional affiliation
- Consider: Co-authoring with an academic collaborator
- Alternative: Fork the repository for personal projects

### "I'm changing institutions"

**Solution:** Email us with:
- New institutional affiliation
- Timeline of transition
- We'll update your record

### "I'm an industry researcher"

**Solution:** We evaluate case-by-case:
- Must be at research-focused company
- Must have relevant publications
- Must demonstrate academic rigor
- Email us to discuss

## 📊 Verification Statistics

We track and publish verification metrics:
- Number of verified contributors
- Institutions represented
- Geographic distribution
- Research areas covered

See [CONTRIBUTORS.md](../CONTRIBUTORS.md) for current statistics.

## 🔄 Updating Your Information

To update your contributor information:

1. **Fork the repository**
2. **Edit** `.github/academic-contributors.json`
3. **Update your entry** with new information
4. **Submit PR** titled "Update contributor info: [Your Name]"
5. **We'll verify** and merge quickly

Or email us and we'll update for you.

## 🚫 Verification Denial

Verification may be denied if:
- ❌ No verifiable institutional affiliation
- ❌ Institution is not accredited/recognized
- ❌ Role doesn't involve research/education
- ❌ Cannot verify credentials
- ❌ Previous violations of scientific integrity

**Appeal Process:**
- Email maintainers with additional information
- Provide alternative credentials
- Explain circumstances
- We'll reconsider within 1 week

## 🎖️ Verified Contributor Badge

Once verified, you receive:
- ✅ `verified-academic` label on PRs
- ✅ Name in CONTRIBUTORS.md
- ✅ Optional: Profile on repository website
- ✅ Recognition in release notes
- ✅ Potential invitation to collaborator team

## 👥 Maintainer Responsibilities

For repository maintainers verifying contributors:

### Verification Checklist
- [ ] Check institutional website for profile
- [ ] Verify ORCID if provided
- [ ] Confirm role is appropriate
- [ ] Review Google Scholar/publications
- [ ] Ensure research area is relevant
- [ ] Check email domain matches institution
- [ ] Look for red flags (fake profiles, etc.)
- [ ] Document verification in notes
- [ ] Add to academic-contributors.json
- [ ] Update PR labels
- [ ] Welcome the contributor

### Verification Standards
- Require at least 2 forms of verification
- Be consistent and fair
- Protect privacy
- Document decisions
- Communicate clearly

## 📞 Contact

### For Verification Questions
- **Email:** botanical-research@example.com
- **GitHub Discussions:** [discussions](https://github.com/outobecca/botanical-colabs/discussions)
- **Issues:** [Open an issue](https://github.com/outobecca/botanical-colabs/issues) with label `verification`

### For Privacy Concerns
- **Email:** privacy@example.com
- **Subject:** "Academic Verification Privacy Concern"

## 📚 Related Documentation

- [Contributing Guidelines](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Peer Review Process](PEER_REVIEW.md)
- [Scientific Standards](../docs/SCIENTIFIC_STANDARDS.md)

## 📄 Schema

Contributor data follows this schema: [academic-contributors.schema.json](academic-contributors.schema.json)

## 🔐 Security

If you discover a security issue with the verification process:
- **DO NOT** create a public issue
- Email: security@example.com
- Use subject: "Security: Verification System"

---

## Summary

✅ **All contributors must be verified**  
✅ **Verification takes 1-3 days**  
✅ **Multiple verification methods available**  
✅ **Privacy protected**  
✅ **One-time process**  

Thank you for helping us maintain the scientific integrity of this repository! 🌿🔬

---

*Last updated: 2025-11-05*  
*Questions? Contact the maintainers*
