def is_valid(isbn):
    isbn = isbn.replace('-','')
    isbn = isbn.upper()
    if len(isbn) != 10:
        return False
    total = 0
    for index, char in enumerate(isbn):
        if char.isdigit():
            total += int(char) * (10 - index)
        elif char == 'X' and index == 9:
            total += 10 * (10 - index)
        else:
            return False
    return total % 11 == 0