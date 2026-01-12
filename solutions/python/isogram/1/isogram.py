def is_isogram(string):
    string = string.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for index, letter in enumerate(string):
        if letter in alphabet:
            if letter in string[index + 1:]:
                return False
    return True