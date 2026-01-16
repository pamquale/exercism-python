ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rows(letter):
    indicator = ALPHABET.index(letter)
    width = indicator * 2 + 1
    top = []
    for i in range(indicator + 1):
        char = ALPHABET[i]
        if i == 0:
            row = char
        else:
            spaces_to_add = i * 2 - 1
            row = char + ' ' * spaces_to_add + char
        top.append(row.center(width))
    bottom = top[:-1][::-1]
    return top + bottom