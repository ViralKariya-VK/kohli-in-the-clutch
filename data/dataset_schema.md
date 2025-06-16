# Dataset Schema

This file explains the structure of the processed dataset used for analysis. Each row represents a single match played by India in which Virat Kohli batted.

| Column Name           | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| `match_id`            | Unique identifier for the match (e.g., `INDvPAK_WC2022`)            |
| `date`                | Match date in DD/MM/YYYY format                                     |
| `opposition`          | Opposing team                                                       |
| `match_type`          | Format of the match: ODI / T20 / Test                               |
| `match_stage`         | Match stage: Group / Knockout / Final / Bilateral                   |
| `venue`               | Location of the match (city or stadium name)                        |
| `toss_win`            | Team that won the toss                                              |
| `match_winner`        | Team that won the match                                             |
| `target_score`        | Target score if India was chasing (blank if India batted first)     |
| `is_chasing`          | Boolean: `True` if India was chasing, `False` otherwise             |
| `arrival_time`        | India’s score when Kohli came to bat (e.g., `14/2`)                 |
| `runs_scored`         | Runs scored by Virat Kohli                                          |
| `balls_faced`         | Number of balls faced by Kohli                                      |
| `dismissal`           | Mode of dismissal (e.g., `Caught`, `Bowled`, `Not Out`)             |
| `dismissal_time`      | India’s score at the time of Kohli's dismissal                      |
| `result`              | Outcome for India: `India Win` or `India Lost`                      |
| `clutch_label`        | `Clutch` if match meets high-pressure criteria, else `Normal`       |
| `player_of_the_match` | Name of the official Player of the Match                            |
