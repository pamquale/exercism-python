ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rows(letter):
    if letter == 'A':
        return [letter]
    diamond = []
    i = ALPHABET.index(letter)
    n = 0
    diamond_len = ALPHABET.index(letter) * 2 + 1
    while i != 0:
        letter_new = ALPHABET[ALPHABET.index(letter) - n]
        spaces_to_add = ALPHABET.index(letter_new) * 2 - 1
        string_to_add = letter_new + ' ' * spaces_to_add + letter_new
        string_to_add = string_to_add.center(diamond_len)
        if i == ALPHABET.index(letter):
            diamond.append(string_to_add)
        else:
            diamond.insert(0, string_to_add)
            diamond.append(string_to_add)
        n += 1
        i -= 1
    string_to_add = ('A'.center(diamond_len))
    diamond.insert(0, string_to_add)
    diamond.append(string_to_add)
    return diamond