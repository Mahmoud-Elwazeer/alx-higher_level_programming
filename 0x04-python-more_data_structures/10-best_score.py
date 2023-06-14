#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best = -999
    for i, j in a_dictionary.items():
        if best < j:
            best = j
            best_score = i

    return best_score
