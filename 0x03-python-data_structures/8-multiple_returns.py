#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_r = []
    tuple_r.append(len(sentence))
    if not sentence:
        tuple_r.append(None)
    else:
        tuple_r.append(sentence[0])
    return (tuple(tuple_r))
