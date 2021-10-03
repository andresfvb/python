def latest(scores):
    return scores[-1]


def personal_best(scores):
    mayor = 0
    for score in scores:
        if score > mayor:
            mayor = score
    return mayor


def personal_top_three(scores):
    bests = []
    mayor = 0
    for score in range(0, 3):
        if scores:
            mayor = score
            for score2 in scores:
                if mayor < score2:
                    mayor = score2
            bests.append(mayor)
            scores.remove(mayor)
    return bests
