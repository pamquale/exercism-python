def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    else:
        steps_amount = 0
        while number != 1:
            if number % 2 == 0:
                number /= 2
                steps_amount += 1
            else:
                number *= 3
                number += 1
                steps_amount += 1
        return steps_amount
