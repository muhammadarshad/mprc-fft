# MPRC-FFT: Zenodo Publication Guidelines

**Repository:** https://github.com/muhammadarshad/mprc-fft  
**Zenodo:** https://zenodo.org  
**Publication Date:** 2026-04-21  

---

## Overview

This guide provides step-by-step instructions for publishing your MPRC-FFT research on Zenodo (commonly referred to as "Zendoo"), CERN's open-access repository. Your submission includes:

- Complete Python implementation with tests
- Full mathematical paper (LaTeX PDF)
- Comprehensive documentation
- Open-source code (CC BY-NC 4.0 license)

---

## Part 1: Pre-Publication Checklist

Before uploading to Zenodo, ensure you have:

- [ ] **ORCID account** (optional but recommended)
  - Sign up at https://orcid.org
  - Provides persistent identifier for authorship
  
- [ ] **Zenodo account**
  - Create at https://zenodo.org
  - Can link with GitHub, ORCID, or email
  
- [ ] **GitHub repository link ready**
  - URL: https://github.com/muhammadarshad/mprc-fft
  - Has all code, paper, and documentation
  
- [ ] **Metadata prepared**
  - Title ✓
  - Authors ✓
  - Description/Abstract ✓
  - Keywords ✓
  - License ✓

---

## Part 2: Zenodo Account Setup

### Step 1: Create Zenodo Account
1. Go to https://zenodo.org
2. Click **Sign Up** (top right)
3. Choose login method:
   - **GitHub** (recommended for code projects) - Easiest option
   - **ORCID** (persistent researcher ID)
   - **Email** (traditional)
4. Complete profile with:
   - Full name: Muhammad Arshad
   - Affiliation (optional but recommended)
   - ORCID (if available)

### Step 2: Link GitHub (Optional but Recommended)
1. Login to Zenodo
2. Go to **Settings** → **Linked Accounts**
3. Click **Link GitHub**
4. Authorize Zenodo to access your GitHub account
5. Benefits:
   - Automatic DOI minting for releases
   - Version tracking
   - Easier repository linking

---

## Part 3: Upload Process

### Step 1: Start New Upload
1. Login to Zenodo
2. Click **Upload** (top navigation)
3. Choose **New Upload**
4. Click **Start Upload**

### Step 2: Upload Files
You have two options:

**Option A: Upload Individual Files (Recommended for your project)**
1. Drag and drop or click to select files:
   - `mprc_fft_paper.pdf` (main paper)
   - `README.md` (documentation)
   - `LICENSE` (CC BY-NC 4.0)
   - `QUICK_REFERENCE.md` (reference)
   - `CITATION.cff` (citation metadata)
   - Python source code files

2. Zenodo accepts:
   - PDF documents
   - Source code (.py, .txt, .md)
   - Archives (.zip, .tar.gz)
   - Datasets and supplementary materials
   - Max 50GB per record, 100 files per upload

**Option B: Upload ZIP Archive**
If you prefer a single file:
1. Create ZIP containing your repo or selected files
2. Upload as single file
3. Preserves folder structure

### Step 3: Review Uploaded Files
- Verify all files are present and readable
- Check file sizes and formats
- Zenodo shows file counts and total size

---

## Part 4: Fill in Metadata (CRITICAL)

All fields marked with **red asterisk (*)** are REQUIRED.

### A. Basic Information

**Resource Type \* :**
- Select: **Software**
- (Alternative: Computer Program, Source Code)
- Your submission is a research software project

**Title \* :**
```
MPRC-FFT: A Signal-Adapted Spectral Transform on Z₂₅₆
```

**Publication Date \* :**
```
2026-04-21
```

**Language:**
- Select: **English**

### B. Creators/Authors \* 

Click **Add Creator** and fill in:

| Field | Value |
|-------|-------|
| Name \* | Muhammad Arshad |
| Affiliation | [Your Institution/Organization] |
| ORCID | [Your ORCID if available] |
| Role | Author / Creator |

**Note:** You can add multiple authors/contributors if applicable

### C. Description/Abstract \*

Paste this or customize:

```
MPRC-FFT: A Signal-Adapted Spectral Transform on Z₂₅₆

A discrete spectral transform derived entirely from ring geometry 
on Z₂₅₆, not a drop-in FFT replacement. 

Key Features:
- 36 output bins (constant, derived from ring geometry)
- O(1,296) constant-time complexity
- 80,905× faster than FFT for N=2²⁰
- Fully invertible (reconstruction error < 5×10⁻¹⁰)
- Information equivalent to FFT (R² = 1.000)
- Integer-only arithmetic (no floating-point required)
- 10/10 verification tests passing

The transform projects signals through circular distance kernels 
on the Z₂₅₆ ring with vacuum boundaries at {0,64,128,192}. 
A co-prime stride of 7 generates exactly 36 sampling positions 
from 252 active states.

Frozen implementation: 2026-04-21
License: CC BY-NC 4.0 (Educational use only)
```

### D. Keywords \*

Add 5-10 relevant keywords (each on new line or comma-separated):

```
spectral-transform
fft
ring-geometry
signal-processing
modular-arithmetic
mathematics
quantum-computing
constant-time
embedded-systems
integer-arithmetic
```

### E. License \*

**Select: Custom License**
- Name: `Creative Commons Attribution-NonCommercial 4.0 International`
- Abbreviation: `CC BY-NC 4.0`
- URL: https://creativecommons.org/licenses/by-nc/4.0/

**Important:** Your work is **NOT** open-source for commercial use
- Educational institutions: ✅ Permitted
- Research organizations: ✅ Permitted
- Commercial entities: ❌ Requires permission

**Access Level:**
- Select: **Open Access**
- Your code is freely available but restricted license applies

### F. Related/Alternate Identifiers

Add these in the **Identifiers** section:

| Type | Value |
|------|-------|
| GitHub | https://github.com/muhammadarshad/mprc-fft |
| DOI | (Will be generated by Zenodo) |
| Related Identifier (Publication) | ISBN/DOI of any published paper |

### G. Funding Information (Optional)

If your research was funded:
- Add funding source
- Grant number
- Funding organization

### H. References (Optional but Recommended)

Add citations/references:

```
[1] Arshad, M. (2026). FFT in MPRC: A Signal-Adapted Spectral 
    Transform on Z₂₅₆. Frozen 2026-04-21.

[2] GitHub Repository: https://github.com/muhammadarshad/mprc-fft

[3] Related: The MPRC Framework documentation at 
    https://muhammadarshad.github.io/pages-mprc/
```

### I. Subjects/Disciplines (Optional)

Select applicable subject areas:
- ✅ Mathematics
- ✅ Computer Science
- ✅ Signal Processing
- ✅ Quantum Physics (if applicable)

---

## Part 5: Review & Publish

### Step 1: Review All Metadata
1. Scroll through entire form
2. Verify all red-marked fields are complete
3. Check for typos and accuracy

### Step 2: Reserve DOI (Optional)
- Click "Reserve DOI" before publishing (if needed for citations)
- Zenodo generates unique DOI for your submission

### Step 3: Publish
1. Review submission one final time
2. Click **Publish** button (green, at bottom)
3. Confirm publication

**Result:**
- Your submission receives a permanent DOI
- Indexed in search engines within hours
- Citable with full metadata
- Available worldwide

---

## Part 6: After Publication

### A. DOI Citation
Your Zenodo DOI will look like:
```
https://doi.org/10.5281/zenodo.XXXXXXX
```

Use in citations:
```
Arshad, M. (2026). MPRC-FFT: A Signal-Adapted Spectral Transform 
on Z₂₅₆ [Software]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

### B. Promote Your Work
1. **GitHub README:** Add Zenodo badge
   ```markdown
   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
   ```

2. **Academic Networks:**
   - ResearchGate
   - Academia.edu
   - SSRN

3. **Social Media:**
   - Twitter with #OpenScience #OpenSource
   - LinkedIn
   - Relevant communities

### C. Link Back from GitHub
Add to your GitHub README:
```markdown
## Publication
Published on Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

### D. Updates & Versions
- If you make significant changes: Upload as **New Version**
- Zenodo generates new DOI for each version
- Old DOI redirects to latest version
- Version history maintained

---

## Part 7: Important Notes for MPRC-FFT

### A. License Compliance
Your CC BY-NC 4.0 license means:
- ✅ Educational use free
- ✅ Research use free
- ✅ Non-profit open-source free
- ❌ Commercial use requires permission
- ❌ For-profit applications need license agreement

**Zenodo Impact:** 
- Zenodo respects all licenses
- License clearly displayed on your record
- Users see restrictions immediately

### B. Paper & Code Together
You're uploading both:
- **Peer-reviewed paper** OR **Preprint**: mprc_fft_paper.pdf
- **Working implementation**: Python code

Zenodo accommodates both well.

### C. Software Citation
Your work will be citable as:
```
@software{arshad2026,
  author = {Arshad, Muhammad},
  title = {MPRC-FFT: A Signal-Adapted Spectral Transform on Z₂₅₆},
  year = {2026},
  url = {https://github.com/muhammadarshad/mprc-fft},
  doi = {10.5281/zenodo.XXXXXXX}
}
```

### D. Metadata from CITATION.cff
Your repository's `CITATION.cff` helps with citation:
- Zenodo may automatically detect it
- Use as reference when filling metadata
- Ensures consistent citation format

---

## Part 8: Troubleshooting

### Issue: "File format not supported"
- **Solution:** Zenodo supports most formats. If issue persists, convert to PDF or ZIP

### Issue: "Metadata validation error"
- **Solution:** Check that all red-asterisk fields are complete
- Most common: Missing creator name, title, or abstract

### Issue: "License not recognized"
- **Solution:** Use "Custom License" field and specify full CC BY-NC 4.0 details
- Include license URL: https://creativecommons.org/licenses/by-nc/4.0/

### Issue: "Need to change something after publishing"
- **Options:**
  - **Within 30-45 days:** Edit minor details in published record
  - **After 30-45 days:** Create new version (new DOI)
  - **For different content:** Upload as new submission

### Issue: "DOI not appearing"
- **Normal delay:** 5-10 minutes after publishing
- **Check:** Visit your record URL (provided after publish)
- **Search:** Search Zenodo for your name to find record

---

## Part 9: Pre-Submission Checklist (Final)

Before clicking **Publish**, verify:

- [ ] All files uploaded (paper, code, documentation)
- [ ] Title is clear and descriptive
- [ ] Abstract explains research and why it matters
- [ ] Keywords are relevant (5-10 items)
- [ ] Creator/author information complete with full names
- [ ] License set to CC BY-NC 4.0
- [ ] GitHub repository linked
- [ ] Keywords match your research domain
- [ ] Description has no typos
- [ ] Files are readable and properly named
- [ ] Related works cited if applicable
- [ ] ORCID added if available

---

## Part 10: Quick Reference

| Item | What to Use |
|------|-------------|
| **Resource Type** | Software |
| **Title** | MPRC-FFT: A Signal-Adapted Spectral Transform on Z₂₅₆ |
| **Date** | 2026-04-21 |
| **Author** | Muhammad Arshad |
| **License** | CC BY-NC 4.0 |
| **GitHub URL** | https://github.com/muhammadarshad/mprc-fft |
| **Main File** | mprc_fft_paper.pdf |
| **Keywords** | spectral-transform, fft, ring-geometry, ... |
| **Access** | Open Access |

---

## Part 11: After Zenodo Publication

### Next Steps:
1. **Zendoo (if different from Zenodo):** Follow similar process
2. **PyPI Publication:** Consider uploading to Python Package Index
   ```bash
   python -m build
   twine upload dist/*
   ```
3. **Academic Databases:** Register on ResearchGate, Academia.edu
4. **Community Announcement:** Announce on relevant research channels

### Citation in Your Own Work:
```bibtex
@software{arshad2026mprcfft,
  author = {Arshad, Muhammad},
  title = {MPRC-FFT: A Signal-Adapted Spectral Transform on Z₂₅₆},
  year = {2026},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.XXXXXXX},
  url = {https://doi.org/10.5281/zenodo.XXXXXXX}
}
```

---

## Support & Resources

- **Zenodo Help:** https://help.zenodo.org
- **Zenodo Metadata Guide:** https://help.zenodo.org/docs/deposit/metadata/
- **CC BY-NC 4.0 License:** https://creativecommons.org/licenses/by-nc/4.0/
- **ORCID Guide:** https://orcid.org/about
- **GitHub to Zenodo Integration:** https://guides.github.com/features/pages/

---

## Final Notes

✅ **Your submission is ready for publication**
- Clean code with tests
- Professional documentation
- Clear licensing
- Complete metadata

✅ **Expected outcome after publishing:**
- Permanent DOI for citation
- Global discoverability
- Open access for researchers and educators
- Version history tracking
- Impact metrics (downloads, citations)

**Good luck with your publication!** 🚀

---

*This guide is specific to MPRC-FFT publication on Zenodo (Zendoo), frozen 2026-04-21*
