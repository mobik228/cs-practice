def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def winner(names: list[str], scores: list[float]) -> str:
    best_index = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i
    return names[best_index]


def ranking(names: list[str], scores: list[float]) -> list[str] associations:
    sorted_pairs = sorted(zip(names, scores), key=lambda pair: pair[1], reverse=True)
    return [name for name, _ in sorted_pairs]


def above_average(names: list[str], scores: list[float]) -> list[str]:
    return [name for name, score in zip(names, scores) if score > avg_score]
