def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    sum = 0
    number_length = len(digits) - 1
    for digit in digits:
        if input_base <= digit or digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        sum += digit * input_base ** number_length
        number_length -= 1
    output_digits =[]
    while sum // output_base != 0:
        quotient = sum // output_base
        nuber_to_append = sum - (output_base * quotient)
        sum //= output_base
        output_digits.append(nuber_to_append)
    output_digits.append(sum)
    output_digits.reverse()
    return output_digits