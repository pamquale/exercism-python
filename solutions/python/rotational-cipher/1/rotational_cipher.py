def rotate(text, key):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet_lower.upper()
    output_text = ''
    for i, letter in enumerate(text):
        if letter in alphabet_upper:
            output_text += alphabet_upper[(alphabet_upper.index(letter) + key) % 26]
        elif letter in alphabet_lower:
            output_text += alphabet_lower[(alphabet_lower.index(letter) + key) % 26]
        else:
            output_text += letter
    return output_text
            