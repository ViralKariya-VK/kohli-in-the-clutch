# Assumptions

This project, "Kohli in the Clutch: A Data-Driven Analysis", is built on a curated dataset of select high-pressure matches featuring Virat Kohli. While efforts have been made to ensure accuracy and consistency, the following assumptions were made during data collection, cleaning, and analysis:

## 1. Match Selection Criteria
- Only **international T20 and ODI matches** were included.
- Focused primarily on matches where **pressure was contextually high**, such as:
  - World Cup knockouts or finals
  - High-stakes group matches (e.g., IND vs PAK)
  - Close chases or significant collapses

## 2. Definition of “Clutch” Matches
- A match is labeled as "Clutch" if it meets **any of the following**:
  - Knockout/Final stage
  - High-pressure chase situation (e.g., chasing >275 in ODIs or >150 in T20s)
  - Early wickets lost (e.g., Kohli comes in at <25/2)
- All other matches are labeled “Normal” for comparison.

## 3. Player Arrival Context
- The `arrival_time` column represents **India's team score** when Kohli arrived at the crease.
- Early arrival is interpreted as increased pressure, especially during chases.

## 4. Player of the Match
- Taken directly from match records and treated as a proxy for **individual match impact**, though it's subjective.

## 5. Clutch Score
- Clutch Score is **not an official statistic** but a custom metric designed for this project.
- It incorporates:
  - Runs scored
  - Balls faced
  - Match context
  - Result and dismissal situation
- While subjective, it provides a comparative index of pressure handling.

## 6. Data Limitations
- Sample size is limited to 10 high-impact matches due to manual data collection.
- No ball-by-ball or over-by-over context was included.
- Subjective elements (like perceived pressure or opposition quality) are not quantified.

---

_This assumptions file is meant to clarify modeling boundaries and help future users interpret the results responsibly._
