def score(x, y):
    outer = 10
    middle = 5
    inner = 1
    if x ** 2 + y ** 2 > outer ** 2:
        return 0
    if outer ** 2 >= x ** 2 + y ** 2 > middle ** 2:
        return 1
    if middle ** 2 >= x ** 2 + y ** 2 > inner ** 2:
        return 5
    if x ** 2 + y ** 2 <= inner ** 2:
        return 10