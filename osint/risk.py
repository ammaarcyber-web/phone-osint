def calculate_risk(public_mentions=0):

    score = 0

    if public_mentions >= 1:
        score += 15

    if public_mentions >= 3:
        score += 15

    if public_mentions >= 5:
        score += 20

    if public_mentions >= 10:
        score += 20

    score = min(score, 100)

    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level
    }
