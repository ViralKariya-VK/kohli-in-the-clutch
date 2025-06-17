# 🏏 Kohli in the Clutch: A Data-Driven Analysis

> **Does Virat Kohli really deliver when the stakes are highest?**  
This project explores that question using real match data and a custom-built "Clutch Score" system to analyze his performance under pressure.

---

## Project Overview

This project investigates Virat Kohli's performances in high-pressure (clutch) vs. normal situations. Using contextual match data and a scoring algorithm, we attempt to quantify what makes a performance truly “clutch”.

---

## Objectives

- Clean and structure match-level performance data for Virat Kohli.
- Define and implement a **Clutch Score** metric based on match pressure.
- Compare performances labeled as **Clutch** vs **Normal**.
- Visualize and interpret key insights using simple EDA and scoring metrics.
- Tell a story around Kohli’s performances in crucial matches.

---

## Project Structure

```
kohli-in-the-clutch/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/                    # Contains original, unprocessed match-level CSV files
│   ├── processed/              # Contains original, unprocessed match-level CSV files
│   └── database_schema.md      # Describes structure of each dataset (columns, types, relationships)
├── src/
│   ├── data_loader.py          # Functions to load data
│   ├── clutch_scoring.py       # Core logic for computing the "Clutch Score"
│   └── plot_utils.py           # Utility functions to save matplotlib/seaborn plots and textual tables
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb       # Initial notebook for data understanding and sanity checks       
│   └── 02_Kohli-clutch_analysis.ipynb      # Narrative-driven walkthrough of insights, charts, and top performances
├── outputs/
│   ├── visuals/            # Exported static image plots from notebooks (e.g., PNGs)
│   └── textual/            # Textual outputs such as top performances in markdown or CSV format
└── docs/
    ├── assumptions.md
    ├── introduction.md     # Project overview including motivation, scope, and goals
    └── methodology.md

```

---

## Key Highlights

- Cleaned and structured 10+ real match records.
- Developed a **Clutch Score Engine** to quantify pressure.
- Visualized Clutch vs Normal stats, Top 3 Clutch Innings, and more.
- Built a clear storytelling notebook explaining the whole journey.

---

## Installation

Make sure you have Python 3.8+  
Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## How to Run

1. Clone the repo.
2. Explore `notebooks/02_Kohli-clutch_analysis.ipynb` for the full story.
3. Use `src/clutch_scoring.py` to plug the scoring logic into any dataset.

---

## Dataset

- Match-level data curated manually from ESPN Cricinfo, Google Search, and Cricbuzz.
- See `data/data_source.md` for sources and `data/dataset_schema.md` for column descriptions.

---

## Limitations

- Small sample size (~10 matches).
- Subjective assumptions in scoring rubric.
- Focused only on Virat Kohli’s batting.

---

## Author

**Viral Kariya**  
BCA Graduate| Aspiring Data Scientist | Passionate about ML, Cricket & Clean Code  
📫 [Connect on LinkedIn](https://www.linkedin.com/in/kariyaviral/)

---

## License

MIT License — feel free to reuse with credit.
