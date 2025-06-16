# src/clutch_scoring.py

import pandas as pd


def score_match_stage(stage: str) -> float:
    stage_scores = {
        "Final": 4,
        "Semi-Final": 3,
        "Knockout": 2.5,
        "Group": 1,
        "Biletral": 0.5
    }
    return stage_scores.get(stage, 0)


def score_opposition(opponent: str) -> float:
    opposition_scores = {
        "Pakistan": 3,
        "Australia": 3,
        "New Zeland": 2.5,
        "South Africa": 2,
        "Bangladesh": 1,
        "Sri Lanka": 1
    }
    return opposition_scores.get(opponent, 0)


def score_result(result: str) -> int:
    return 1 if result.strip().lower() == 'india win' else 0


def score_chasing(is_chasing: str) -> int:
    return 1 if str(is_chasing).strip().lower() == 'true' else 0


def score_arrival_time(arrival_time: str) -> float:
    try:
        runs, wickets = map(int, arrival_time.split('/'))
        if wickets >= 2:
            return 1
        elif wickets == 1:
            return 0.5
        else:
            return 0
    except:
        return 0


def score_target_score(is_chasing: str, target_score: int, match_type: str) -> int:
    if str(is_chasing).strip().lower() != 'true':
        return 0

    match_type = match_type.strip().upper()

    if match_type == "T20":
        if target_score >= 180:
            return 2
        elif target_score >= 160:
            return 1
    elif match_type == "ODI":
        if target_score >= 300:
            return 2
        elif target_score >= 260:
            return 1

    return 0


def failure_penalty(row) -> float:
    """
    Deduct points for failing under pressure.
    """
    try:
        runs = float(row['runs_scored'])
        dismissal = str(row['dismissal']).strip().lower()
        context_score = (
            score_match_stage(row['match_stage']) +
            score_opposition(row['opposition']) +
            score_chasing(row['is_chasing']) +
            score_arrival_time(row['arrival_time']) +
            score_target_score(row['is_chasing'], row['target_score'], row['match_type'])
        )

        if runs <= 15 and dismissal != 'not out' and context_score >= 7:
            return -2
        elif runs <= 25 and context_score >= 6:
            return -1
        else:
            return 0
    except:
        return 0


def score_runs(runs, not_out: bool, context: str) -> float:
    """
    Runs scoring with context multiplier.
    """
    try:
        runs = float(runs)
    except:
        runs = 0

    base = runs / 10
    bonus = 1 if not_out else 0
    multiplier = 1.5 if context.lower() == 'clutch' else 1.0

    return (base + bonus) * multiplier


def compute_clutch_score(row) -> float:
    context = row['clutch_label']
    not_out = pd.isna(row['dismissal']) or row['dismissal'].strip().lower() == 'not out'

    base_score = (
        score_match_stage(row['match_stage']) +
        score_opposition(row['opposition']) +
        score_result(row['result']) +
        score_chasing(row['is_chasing']) +
        score_arrival_time(row['arrival_time']) +
        score_target_score(row['is_chasing'], row['target_score'], row['match_type'])
    )

    performance_score = score_runs(row['runs_scored'], not_out, context)
    penalty = failure_penalty(row)

    total_score = base_score + performance_score + penalty

    # 👉 Apply cap if the match is NOT a clutch match
    if context.strip().lower() != 'clutch':
        total_score = min(total_score, 18)

    return total_score
