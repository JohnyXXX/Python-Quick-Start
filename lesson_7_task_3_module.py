from pprint import pprint

import numpy as np


def levenshtein(s1, s2):
    size_x = len(s1) + 1
    size_y = len(s2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if s1[x - 1] == s2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )
    return 1 - (matrix[size_x - 1, size_y - 1]) / max(len(s1), len(s2))


def compare(s1, s2):
    s1, s2 = [s.lower() for s in [s1, s2]]
    ngrams = [s1[i:i + 3] for i in range(len(s1) - 1)]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1), len(s2))


def int_val(s):
    try:
        return int(s)
    except ValueError:
        return 0


if __name__ == '__main__':
    out = []
    for a, b in [
        ('алгоритм', 'алгоритм'),
        ('алгоритм', 'алгоритмы'),
        ('алгоритм', 'алгоритмов'),
        ('стол', 'столик'),
        ('стол', 'стул'),
        ('маша', 'даша'),
        ('ольга', 'олег'),
        ('ольга', 'оля'),
        ('маша', 'машенька'),
    ]:
        out += [(a, b, compare(a, b), levenshtein(a, b))]
    pprint(out)
    pprint([int_val(s) for s in ['старше', '30', 'но', '101']])
