from math import inf
def true_divide(first, second):
    if second != 0:
        div = int(first)/int(second)
        result = div
    if second == 0:
        result = inf
    return result