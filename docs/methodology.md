# Methodology

This document outlines the step-by-step methodology used to analyze Virat Kohli’s performance in high-pressure situations, particularly in clutch matches.

---

## 1. Data Sourcing and Curation

- Match data was manually collected from official sources including **ESPNcricinfo**, **Cricbuzz**, and **Google Search**.
- Each row in the dataset corresponds to a match with Kohli's batting details.
- Metadata includes match stage, result, opposition, target score, and contextual match situations.

---

## 2. Data Cleaning

- Cleaned missing values in fields like `dismissal_time` using `"-1"` for not outs.
- Ensured consistent data types (e.g., `date` → datetime format, `target_score` → integer).
- Standardized categorical variables: `"India Win"`, `"India Lost"`, etc.

---

## 3. Labeling Clutch Matches

- A binary label `clutch_label` was introduced:
  - `"Clutch"`: Knockout matches, high-target chases, or early collapses
  - `"Normal"`: All other situations
- The logic was manually evaluated per match context.

---

## 4. Clutch Score Calculation

- A custom function was created to assign a **Clutch Score** to each match based on:
  - **Runs Scored**: Higher runs → higher score
  - **Balls Faced**: Fewer balls for high runs → bonus
  - **Match Stage**: Knockout/Final stages boost score
  - **Result & Dismissal**: Not outs and wins give a bonus

### Clutch Score Formula (Simplified):

score = runs + (10 if not_out) + (match_stage_bonus) + (5 if India won)


> _Note: Full logic implemented in `src/clutch_scoring.py`_

---

## 5. Visual Analysis

- EDA was performed to understand distributions and context:
  - Run distribution across clutch and normal matches
  - Dismissal types and their influence
  - Comparison of clutch score distributions
- Reusable visual utilities were written in `plot_utils.py` to save and standardize plots.

---

## 6. Insights & Narrative

- Top 3 clutch performances were extracted based on Clutch Score.
- Statistical comparison was made between average clutch and normal scores.
- Scatter plots were used to examine relationship between **runs** and **clutch scores**.

---

_This methodology was designed to be transparent, reproducible, and open for extension in future versions of this project._
