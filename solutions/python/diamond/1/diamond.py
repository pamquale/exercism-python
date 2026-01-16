ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rows(letter):
    if letter == 'A':
        return [letter]
    diamond = []
    i = ALPHABET.index(letter)
    n = 1
    while i != 0:
        if i == ALPHABET.index(letter):
            string_to_add = []
            for j in range(0, ALPHABET.index(letter)):
                if j == 0:
                    string_to_add.append(letter) # [D]
                    string_to_add.append(' ') # D, ' '
                    string_to_add.append(letter) # ['D', ' ', 'D']
                    #
                else:
                    string_to_add.insert(1, '  ') # 'D   D'
            diamond.append(''.join(string_to_add))
        else:
            letter_new = ALPHABET[ALPHABET.index(letter) - n]
            string_to_add = []
            for j in range(0, ALPHABET.index(letter_new)):
                if j == 0:
                    string_to_add.append(letter_new) # [B]
                    string_to_add.append(' ') # B, ' '
                    string_to_add.append(letter_new) # ['B', ' ', 'B']
                else:
                    string_to_add.insert(1, '  ')  # 'D   D'
            spaces_to_add = ALPHABET.index(letter) - ALPHABET.index(letter_new)
            for k in range(0, spaces_to_add):
                string_to_add.insert(0, ' ')
                string_to_add.append(' ')
            diamond.insert(0, ''.join(string_to_add))
            diamond.append(''.join(string_to_add))
            n += 1
        i -= 1
    letter_new = ALPHABET[ALPHABET.index(letter) - n]
    spaces_to_add = ALPHABET.index(letter) - ALPHABET.index(letter_new)
    string_to_add = ['A']
    for i in range(0, spaces_to_add):
        string_to_add.insert(0, ' ')
        string_to_add.append(' ')
    diamond.insert(0, ''.join(string_to_add))
    diamond.append(''.join(string_to_add))
    return diamond