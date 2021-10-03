import numpy as number


def latest(scores):
    return scores[-1]


def personal_best(scores):
    return number.amax(scores)


def personal_top_three(scores):
    bests = []
    for x in range(0, 3):
        if scores:
            best = number.amax(scores)
            bests.append(best)
            scores.remove(best)
    return bests
