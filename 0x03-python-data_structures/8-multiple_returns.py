#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    len_s = len(sentence)
    return (len_s, sentence[0])
