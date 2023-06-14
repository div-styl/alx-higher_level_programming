#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_grade = None
    for key, value in a_dictionary.items():
        if best_grade is None or value > a_dictionary[best_grade]:
            best_grade = key
    return best_grade
