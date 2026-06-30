# Alloy Atlas — Engineering Material Selector & Analyzer

A two-part project for selecting and comparing engineering materials, built to bridge a
Metallurgical & Materials Science background with software development skills.

## What's in here

| File | What it does | Skills shown |
|---|---|---|
| `index.html` | Interactive web app: filter ~15 materials by category, strength, density and cost; compare up to 4 on a normalized radar chart; see a specific-strength leaderboard | HTML, CSS, JavaScript (DOM manipulation, event handling, Chart.js) |
| `materials_analysis.py` | Loads the same dataset, computes specific strength/stiffness, category-wise stats, and exports a ranked bar chart | Python, pandas, matplotlib |
| `materials_data.csv` | Shared dataset (15 materials × 8 properties: density, yield strength, modulus, cost, max service temperature, corrosion resistance) | Data structuring |

## Why this dataset / these metrics

- **Specific strength** (yield strength ÷ density) and **specific stiffness** (modulus ÷ density)
  are standard first-pass screening metrics in materials selection for weight-critical
  applications (aerospace, automotive) — covered in Introduction to Engineering Materials /
  Deformation Behaviour of Materials.
- The radar chart axes (Strength, Stiffness, Lightness, Affordability, Corrosion Resistance,
  Heat Resistance) let you see the classic trade-offs at a glance — e.g. titanium alloys
  win on strength-to-weight but lose hard on cost; polymers win on cost but lose on
  heat resistance.

## Running it

**Web app:** just open `index.html` in any browser — no build step, no server needed.

**Python script:**
```bash
pip install pandas matplotlib
python materials_analysis.py
```

## Possible extensions (good "future work" line for interviews)

- Replace the hardcoded dataset with a scraped/larger materials database (e.g. MatWeb)
- Add a regression model (scikit-learn) to predict yield strength from alloy composition
- Convert the dataset loader into a small Flask/FastAPI backend so the web app queries
  live data instead of an embedded array
- Add real tensile-test CSV import + stress-strain curve plotting (ties into lab data)

## Suggested CV bullet points

- *Built a materials selection tool (HTML/CSS/JS + Chart.js) that filters and visually
  compares 15 engineering materials across 6 normalized property axes, including a
  specific-strength ranking algorithm grounded in materials science coursework.*
- *Wrote a pandas/matplotlib analysis script computing specific strength and stiffness
  across material categories to support weight-critical material selection, exporting
  ranked visualizations.*
