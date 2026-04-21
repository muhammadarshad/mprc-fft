# Zenodo Publication Quick Reference

## 📋 Zenodo Submission Checklist

### Account Setup
- [ ] Create Zenodo account at https://zenodo.org
- [ ] (Recommended) Link GitHub account
- [ ] (Recommended) Add ORCID profile

### Files to Upload
- [ ] `mprc_fft_paper.pdf` - Main mathematical paper
- [ ] `README.md` - Primary documentation
- [ ] Source code files (`.py` files)
- [ ] `LICENSE` - CC BY-NC 4.0 license
- [ ] `CITATION.cff` - Citation metadata
- [ ] `QUICK_REFERENCE.md` - Math reference

### Required Metadata Fields (marked with *)

| Field | Value |
|-------|-------|
| **Resource Type** \* | Software |
| **Title** \* | MPRC-FFT: A Signal-Adapted Spectral Transform on Z₂₅₆ |
| **Publication Date** \* | 2026-04-21 |
| **Creator/Author** \* | Muhammad Arshad |
| **Description** \* | See ZENODO_PUBLICATION_GUIDE.md Section 4C |
| **Keywords** \* | spectral-transform, fft, ring-geometry, signal-processing, modular-arithmetic, mathematics |
| **License** \* | Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) |
| **Access** | Open Access |

### Optional but Recommended Metadata

| Field | Value |
|-------|-------|
| **Affiliation** | Your Institution |
| **ORCID** | Your ORCID ID |
| **Related Identifier** | https://github.com/muhammadarshad/mprc-fft |
| **Funding** | [If applicable] |
| **References** | Related works and citations |

---

## 🔗 Key URLs

| Resource | URL |
|----------|-----|
| **Zenodo** | https://zenodo.org |
| **GitHub Repository** | https://github.com/muhammadarshad/mprc-fft |
| **CC BY-NC 4.0 License** | https://creativecommons.org/licenses/by-nc/4.0/ |
| **Zenodo Help** | https://help.zenodo.org |
| **Zenodo Metadata Guide** | https://help.zenodo.org/docs/deposit/metadata/ |

---

## 📝 Keywords (Use At Least 5)

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

---

## 📄 Abstract/Description Template

Copy and customize:

```
MPRC-FFT: A Signal-Adapted Spectral Transform on Z₂₅₆

A discrete spectral transform derived entirely from ring geometry on Z₂₅₆, 
NOT a drop-in FFT replacement.

KEY FEATURES:
• 36 output bins (constant, derived from ring geometry)
• O(1,296) constant-time complexity (80,905× faster than FFT for N=2²⁰)
• Fully invertible with exact reconstruction (error < 5×10⁻¹⁰)
• Information equivalent to FFT (R² = 1.000 both directions)
• Integer-only arithmetic (u8/u16/u32/u64, no floating-point required)
• 10/10 verification tests passing

TECHNICAL OVERVIEW:
The transform projects signals through circular distance kernels on the Z₂₅₆ 
ring with vacuum boundaries at {0, 64, 128, 192}. A co-prime stride of 7 
generates exactly 36 sampling positions from 252 active states.

RING GEOMETRY:
- τ = 256 (ring order)
- H = 128 (vacuum axis)
- V = {0, 64, 128, 192} (vacuum boundaries)
- g = 7 (co-prime stride)
- B = 36 (output bins, derived not chosen)

IMPLEMENTATION:
- Python 3.8+
- NumPy-based
- Complete test suite (10/10 passing)
- Licensed under CC BY-NC 4.0 (educational use only)

FROZEN: 2026-04-21
```

---

## ⚖️ License Notes

Your project uses **CC BY-NC 4.0**:

✅ **PERMITTED:**
- Educational institutions
- Research organizations
- Non-profit open-source projects
- Academic papers and citations
- Teaching and learning

❌ **NOT PERMITTED:**
- Commercial use
- For-profit products
- Revenue-generating applications
- Proprietary software

**For commercial use:** Contact author for explicit permission

---

## 🚀 Step-by-Step Publication Process

### 1. Create Account
```
https://zenodo.org → Sign Up → Link GitHub (optional)
```

### 2. Start Upload
```
Click Upload → New Upload → Start Upload
```

### 3. Add Files
```
Drag and drop or select:
- mprc_fft_paper.pdf
- *.py files
- README.md
- LICENSE
- CITATION.cff
```

### 4. Fill Metadata
```
All fields marked with * are REQUIRED:
✓ Resource Type: Software
✓ Title: [full title]
✓ Publication Date: 2026-04-21
✓ Creator: Muhammad Arshad
✓ Description: [abstract/overview]
✓ Keywords: [5+ keywords]
✓ License: CC BY-NC 4.0
```

### 5. Review & Publish
```
Review all metadata → Click Publish → Confirm
```

### 6. Get DOI
```
Zenodo assigns permanent DOI:
https://doi.org/10.5281/zenodo.XXXXXXX
```

---

## 📖 Citation Formats

### APA
```
Arshad, M. (2026). MPRC-FFT: A signal-adapted spectral transform on Z₂₅₆ 
[Software]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

### BibTeX
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

### Chicago
```
Arshad, Muhammad. "MPRC-FFT: A Signal-Adapted Spectral Transform on Z₂₅₆." 
Software. Zenodo, 2026. https://doi.org/10.5281/zenodo.XXXXXXX.
```

---

## ✅ Pre-Publish Verification

Before clicking Publish, verify:

- [ ] All red-marked (\*) fields completed
- [ ] At least 5 keywords added
- [ ] License set to CC BY-NC 4.0
- [ ] GitHub repository linked
- [ ] Description/abstract filled
- [ ] Creator name correct
- [ ] Files uploaded and readable
- [ ] No typos in metadata
- [ ] Title matches your GitHub repo
- [ ] Keywords are relevant

---

## 🎯 What Happens After Publishing

### Immediately:
- ✅ Record created with unique URL
- ✅ DOI reserved
- ✅ Can be cited

### Within Hours:
- ✅ Indexed in search engines (Google, etc.)
- ✅ Discoverable on Zenodo
- ✅ Accessible worldwide

### DOI Format:
```
https://doi.org/10.5281/zenodo.XXXXXXX
```
(Replace XXXXXXX with your actual number)

---

## 🔄 Updates & Versions

### Minor Corrections (within 30-45 days)
- Can edit metadata directly
- Files cannot be changed
- Same DOI

### Major Updates (after 30-45 days)
- Upload as **New Version**
- Zenodo creates new DOI
- Old DOI redirects to latest
- Version history maintained

---

## 📞 Support

- **Zenodo Help:** https://help.zenodo.org
- **Contact Support:** support@zenodo.org
- **FAQ:** https://help.zenodo.org/docs/faq/

---

## 🎓 Educational Use

Your CC BY-NC 4.0 license makes this perfect for:

✅ **Universities & Schools**
- Classroom teaching
- Student projects
- Research programs

✅ **Open Education**
- MOOCs
- Educational repositories
- Learning platforms

✅ **Research Institutions**
- Academic papers citing your work
- Derivative research
- Non-commercial projects

---

*Complete guide: See ZENODO_PUBLICATION_GUIDE.md*
