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
        string_to_add = []
        for j in range(0, ALPHABET.index(letter_new)):
            if j == 0:
                string_to_add.append(letter_new)
                string_to_add.append(' ')
                string_to_add.append(letter_new)
            else:
                string_to_add.insert(1, '  ')
        string_to_add = ''.join(string_to_add).center(diamond_len)
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