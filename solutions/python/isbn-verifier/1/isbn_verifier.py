def is_valid(isbn):
    isbn = isbn.replace('-','')
    isbn = isbn.lower()
    if len(isbn) != 10:
        return False
    allowed_symbols = '1234567890'
    if isbn[9] not in allowed_symbols and isbn[9] != 'x':
        return False
    total = 0
    number_to_multiply = 10
    for index, digit in enumerate(isbn):
        if digit not in allowed_symbols and index != 9:
            return False
        if index == 9 and digit == 'x':
            total += 10 * number_to_multiply
            break
        total += int(digit) * number_to_multiply
        number_to_multiply -= 1
    return total % 11 == 0