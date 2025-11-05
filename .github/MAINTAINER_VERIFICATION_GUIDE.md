# 🔐 Maintainer Guide: Academic Verification

## Overview

This guide is for repository maintainers who verify academic contributors.

## 🎯 Verification Workflow

### 1. New PR Triggers Verification

When a new contributor opens a PR:
1. ✅ Workflow checks `.github/academic-contributors.json`
2. ✅ If not found → adds `verification-required` label
3. ✅ If found → adds `verified-academic` label
4. ✅ Posts appropriate comment

### 2. Contributor Responds

The contributor will either:
- **Email you** with credentials (check repository email)
- **Comment on PR** with credentials
- **Have advisor vouch** (for students)

### 3. Verify Credentials

Follow this checklist:

#### Basic Verification ✅
- [ ] **Check institutional website**
  - Visit official university/institute website
  - Find faculty/staff directory
  - Confirm person exists in stated role
  - Verify department/division

- [ ] **Verify email domain**
  - Email should be from `.edu`, `.ac.uk`, `.gov`, or recognized institution
  - Avoid generic email providers (gmail, yahoo, etc.)
  - Check email appears on institutional profile

- [ ] **Review professional profile**
  - University profile page
  - Google Scholar profile
  - ORCID profile (if provided)
  - ResearchGate or similar

#### Enhanced Verification ✅
- [ ] **Check publications** (for faculty/researchers)
  - Google Scholar citations
  - PubMed/Web of Science
  - Relevant expertise area
  - Recent activity

- [ ] **Verify ORCID** (if provided)
  - Visit https://orcid.org/[their-id]
  - Confirm name matches
  - Check institution listed
  - Review works/affiliations

- [ ] **Check research fit**
  - Research area relevant to botanical science?
  - Appropriate expertise level?
  - Credible track record?

#### For Students 🎓
- [ ] **Check student status**
  - Listed on advisor's lab page
  - Department student directory
  - Recent publications (if any)
  - Advisor confirmation (email or comment)

- [ ] **Verify advisor**
  - Advisor is faculty member
  - Research area matches
  - Active research group

#### Red Flags 🚩
- ❌ Cannot find person on institutional website
- ❌ Email domain doesn't match institution
- ❌ No online presence (profile, publications, etc.)
- ❌ Credentials seem fabricated
- ❌ Institution is not accredited
- ❌ Previous integrity violations

### 4. Add to Contributors Database

If verification passes:

```bash
# Edit the file
code .github/academic-contributors.json
```

Add entry (use this template):

```json
{
  "github_username": "their-github-username",
  "full_name": "Dr. Jane Smith",
  "institution": "University of Example",
  "department": "Department of Botany",
  "role": "Associate Professor",
  "orcid": "0000-0002-1234-5678",
  "email": "jane.smith@example.edu",
  "profile_url": "https://example.edu/faculty/jsmith",
  "research_interests": [
    "Plant taxonomy",
    "Conservation biology",
    "Biodiversity informatics"
  ],
  "verified_date": "2025-11-05",
  "verified_by": "your-github-username",
  "notes": "Expert in tropical plant diversity. 15+ years research experience."
}
```

**Important:** Keep entries alphabetically sorted by `github_username`.

### 5. Update PR

```bash
# Commit the update
git checkout main
git pull origin main
git add .github/academic-contributors.json
git commit -m "chore: verify academic contributor @their-username

- Institution: University of Example
- Role: Associate Professor
- Verified: 2025-11-05"
git push origin main
```

### 6. Update PR Labels & Comment

The workflow will automatically re-run and:
- Remove `verification-required` label
- Add `verified-academic` label
- Post success comment

Or do it manually:

**Remove label:**
- Go to PR
- Click labels
- Remove `verification-required`
- Add `verified-academic`

**Post comment:**
```markdown
## ✅ Verification Approved

Welcome @their-username! You've been verified as an academic contributor.

**Institution:** University of Example  
**Role:** Associate Professor

Your contribution will now proceed through our standard review process.

Please review our [Contributing Guidelines](../CONTRIBUTING.md) and [Peer Review Process](PEER_REVIEW.md).

Thank you for contributing to botanical science! 🌿
```

## 📋 Verification Templates

### Email Response: Approved

```
Subject: Re: Academic Verification - [Username]

Hi [Name],

Thank you for your verification request! I've reviewed your credentials and confirmed your affiliation with [Institution].

You've been added to our verified contributors database and your PR is now approved for review.

Your entry:
- GitHub: @username
- Institution: [Institution]
- Role: [Role]
- Verified: [Date]

Future PRs will be automatically verified. Welcome to the project!

Best regards,
[Your Name]
Repository Maintainer
```

### Email Response: Need More Info

```
Subject: Re: Academic Verification - [Username]

Hi [Name],

Thank you for your verification request. I need a bit more information to complete the verification:

- Could you provide a link to your institutional profile page?
- Can you share your ORCID iD or Google Scholar profile?
- [Any specific concerns]

This helps us ensure the scientific integrity of our repository.

Please reply with this information and I'll complete your verification.

Best regards,
[Your Name]
```

### Email Response: Denied

```
Subject: Re: Academic Verification - [Username]

Hi [Name],

Thank you for your interest in contributing. After reviewing your verification request, I'm unable to verify your academic affiliation at this time because:

[Specific reason - e.g., "I couldn't find your profile on the institution's website" or "The institution is not currently in our recognized list"]

Options:
1. Provide additional verification documents
2. Have an institutional supervisor vouch for you
3. Contact us to discuss alternative arrangements

If you believe this is an error, please reply with additional information.

Best regards,
[Your Name]
```

## 🔍 Verification Scenarios

### Scenario 1: Faculty Member (Easy)

**Contributor provides:**
- Name: Dr. Sarah Johnson
- Institution: Stanford University
- Role: Associate Professor
- Email: sjohnson@stanford.edu

**Verification steps:**
1. Visit https://profiles.stanford.edu
2. Search "Sarah Johnson botany"
3. Confirm profile exists
4. Check publications on Google Scholar
5. Verify email domain (@stanford.edu)
6. ✅ Approve

**Time:** 5 minutes

### Scenario 2: PhD Student (Medium)

**Contributor provides:**
- Name: Alex Chen
- Institution: UC Berkeley
- Role: PhD Student
- Advisor: Dr. Maria Rodriguez

**Verification steps:**
1. Find Dr. Rodriguez's lab page
2. Check if Alex is listed as lab member
3. Look for Alex in department directory
4. Check if advisor has GitHub account to confirm
5. ✅ Approve with note "Confirmed by advisor"

**Time:** 10 minutes

### Scenario 3: International Researcher (Medium)

**Contributor provides:**
- Name: Dr. Yuki Tanaka
- Institution: University of Tokyo
- Role: Research Associate
- Profile: [Japanese and English]

**Verification steps:**
1. Visit university website
2. Use Google Translate if needed
3. Find English version of profile
4. Check ORCID profile
5. Verify publications
6. ✅ Approve

**Time:** 15 minutes

### Scenario 4: Industry Researcher (Hard)

**Contributor provides:**
- Name: John Smith
- Institution: BioTech Research Corp
- Role: Senior Scientist

**Verification steps:**
1. Research the company - is it legitimate?
2. Check if they do published research
3. Find contributor's LinkedIn
4. Check publications in field
5. Evaluate: Does this fit our academic focus?
6. Decision: Case-by-case
   - ✅ If company has strong research reputation
   - ❌ If purely commercial

**Time:** 20-30 minutes

### Scenario 5: Botanist at Museum/Garden (Medium)

**Contributor provides:**
- Name: Emma Wilson
- Institution: Royal Botanic Gardens, Kew
- Role: Research Botanist

**Verification steps:**
1. Visit https://www.kew.org
2. Find staff directory
3. Confirm Emma Wilson exists
4. Check publications/projects
5. ✅ Approve - botanical gardens are recognized institutions

**Time:** 10 minutes

## 🚫 When to Deny Verification

### Clear Denials

❌ **No institutional affiliation**
- Hobbyist without academic connection
- Independent researcher with no institution
- Student at non-accredited institution

❌ **Cannot verify identity**
- No profile on institution website
- Email domain doesn't match
- No online presence at all

❌ **Inappropriate role**
- Undergraduate student (unless supervised)
- Administrative staff without research role
- Industry role unrelated to research

❌ **Red flags**
- Fake credentials
- Previous misconduct
- Suspicious information

### Gray Areas (Use Judgment)

⚠️ **Industry researchers**
- Evaluate case-by-case
- Check research publications
- Consider company reputation

⚠️ **Citizen scientists**
- Generally no (unless co-authoring with academic)
- Exception: Affiliated with recognized program
- Alternative: Suggest forking repository

⚠️ **Recently graduated**
- If between positions: verify previous affiliation
- If starting new position: verify with new institution
- Bridge period: use judgment

⚠️ **International institutions**
- Research if unfamiliar
- Check accreditation status
- Verify through ORCID or publications

## 📊 Tracking Verifications

### Monthly Review

Check verification statistics:

```bash
# Count verified contributors
cat .github/academic-contributors.json | jq 'length'

# List institutions
cat .github/academic-contributors.json | jq -r '.[].institution' | sort | uniq

# List roles
cat .github/academic-contributors.json | jq -r '.[].role' | sort | uniq -c

# Recent verifications
cat .github/academic-contributors.json | jq -r '.[] | select(.verified_date >= "2025-11-01") | .github_username'
```

### Quality Metrics

Track:
- ✅ Verification response time
- ✅ Approval rate
- ✅ Number of requests per month
- ✅ Geographic distribution
- ✅ Institution diversity

## 🔒 Privacy & Security

### Protect Private Information

**DO:**
- ✅ Store emails securely
- ✅ Keep verification notes private
- ✅ Only publish what contributors approve
- ✅ Use encrypted email when possible

**DON'T:**
- ❌ Publish email addresses
- ❌ Share verification notes publicly
- ❌ Discuss individuals publicly
- ❌ Keep unnecessary personal data

### Handling Sensitive Data

If contributor requests privacy:
- Mark certain fields as private
- Don't publish full name if requested
- Use initials or shortened version
- Document privacy preferences

## 🔄 Updating Records

### Contributor Changes Institution

```json
{
  "github_username": "researcher",
  "full_name": "Dr. Jane Smith",
  "institution": "New University",  // Updated
  "previous_institutions": [         // Added
    "Old University (2020-2025)"
  ],
  "role": "Associate Professor",
  "verified_date": "2025-11-05",
  "last_updated": "2025-12-01",      // Added
  "verified_by": "maintainer"
}
```

### Contributor Leaves Academia

Options:
1. **Keep record** - Mark as "Former [Role]"
2. **Remove verification** - If requested
3. **Emeritus status** - For retired faculty

### Handling Departures

```json
{
  "github_username": "emeritus",
  "full_name": "Dr. John Retired",
  "institution": "Example University",
  "role": "Professor Emeritus",
  "status": "retired",
  "verified_date": "2020-01-15",
  "verified_by": "maintainer",
  "notes": "Retired 2025, maintaining emeritus status"
}
```

## 📞 Communication Tips

### Be Professional
- Use formal tone in first contact
- Address by appropriate title (Dr., Prof., etc.)
- Be respectful of time

### Be Clear
- Explain what you need
- Give specific examples
- Provide timeline

### Be Helpful
- Offer alternatives if initial verification fails
- Guide them through process
- Answer questions promptly

### Be Consistent
- Apply same standards to all
- Document decisions
- Follow established procedures

## 🆘 Escalation Process

### When to Escalate

Contact senior maintainers if:
- ❓ Unsure about verification decision
- ⚠️ Potential integrity issue
- 🤔 Edge case not covered in guidelines
- 🚨 Security concern

### How to Escalate

1. **Document the case**
   - Gather all information
   - Note your concerns
   - List options considered

2. **Contact team**
   - Email maintainers list
   - Or: Open private issue
   - Or: Schedule call

3. **Get decision**
   - Discuss as team
   - Vote if needed
   - Document outcome

4. **Implement**
   - Follow team decision
   - Update guidelines if needed
   - Communicate to contributor

## 📚 Resources

### Verification Tools
- [ORCID](https://orcid.org) - Researcher identifiers
- [Google Scholar](https://scholar.google.com) - Publications
- [ResearchGate](https://www.researchgate.net) - Academic network
- [Web of Science](https://webofscience.com) - Citations
- [PubMed](https://pubmed.ncbi.nlm.nih.gov) - Life sciences

### Institution Databases
- [Times Higher Education](https://www.timeshighereducation.com) - University rankings
- [Carnegie Classification](https://carnegieclassifications.acenet.edu) - US institutions
- [QS World Rankings](https://www.topuniversities.com) - Global universities

### Professional Organizations
- [Botanical Society of America](https://botany.org)
- [International Association for Plant Taxonomy](https://www.iapt-taxon.org)
- [Society for Conservation Biology](https://conbio.org)

## 📝 Maintaining the System

### Regular Tasks

**Weekly:**
- [ ] Check for new verification requests
- [ ] Respond to pending requests
- [ ] Update contributor database

**Monthly:**
- [ ] Review verification statistics
- [ ] Check for stale requests
- [ ] Update guidelines if needed

**Quarterly:**
- [ ] Audit contributor list
- [ ] Check for institution changes
- [ ] Review verification criteria

**Annually:**
- [ ] Comprehensive review of system
- [ ] Update documentation
- [ ] Train new maintainers
- [ ] Collect feedback from contributors

## 🎓 Training New Maintainers

### Checklist for new verifiers:

- [ ] Read this guide completely
- [ ] Review `academic-contributors.json` structure
- [ ] Practice with test verification
- [ ] Shadow experienced maintainer
- [ ] Complete 3 verifications under supervision
- [ ] Get access to verification email
- [ ] Added to maintainers team

### Shadowing Process

1. **Week 1:** Observer
   - Watch experienced maintainer verify 3-5 contributors
   - Ask questions
   - Review documentation

2. **Week 2:** Assistant
   - Help with verification research
   - Draft verification responses
   - Get feedback

3. **Week 3:** Primary (supervised)
   - Lead 3 verifications
   - Get approval before finalizing
   - Debrief each case

4. **Week 4:** Independent
   - Verify contributors independently
   - Available for questions
   - Periodic check-ins

---

## Summary

✅ **Verify thoroughly but efficiently**  
✅ **Document all decisions**  
✅ **Protect privacy**  
✅ **Be consistent and fair**  
✅ **Communicate clearly**  

Thank you for maintaining the scientific integrity of this repository! 🔬

---

*Last updated: 2025-11-05*  
*Questions? Contact senior maintainers*
