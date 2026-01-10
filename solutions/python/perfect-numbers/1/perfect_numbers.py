def classify(number):
    factors = []
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    for n in range(1, int(number**0.5) + 1):
        if number % n == 0:
            factors.append(n)
            factors.append(number // n)
    factors = set(factors)
    factors.remove(number)
    sum = 0
    for n in factors:
        sum += n
    if sum == number:
        return 'perfect'
    if sum > number:
        return 'abundant'
    if sum < number:
        return 'deficient'
