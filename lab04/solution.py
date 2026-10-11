def winner(names: list[str], scores: list[float]) -> str:
    best_i = 0
    for i in range(len(scores)):
        if scores[i] > scores[best_i]:
            best_i = i
    return names[best_i]


def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def ranking(names: list[str], scores: list[float]) -> list[str]:
    pairs = []
    for i in range(len(names)):
        pairs.append((scores[i], names[i]))
    pairs.sort(key=lambda x: x[0], reverse=True)
    result = []
    for pair in pairs:
        result.append(pair[1])
    return result


def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i] > avg:
            result.append(names[i])
    return result
