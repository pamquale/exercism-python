def encode(plain_text):
    plain_text = plain_text.lower()
    plain_text = plain_text.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))
    ciphered_text = []
    for char in plain_text:
        if not char.isalnum():
            plain_text = plain_text.replace(char, '')
    for i in range(0, len(plain_text) - 1, 5):
        ciphered_text.append(plain_text[i:i+5])
    return ' '.join(ciphered_text)
        

def decode(ciphered_text):
    ciphered_text = ciphered_text.lower()
    ciphered_text = ciphered_text.translate(str.maketrans('zyxwvutsrqponmlkjihgfedcba','abcdefghijklmnopqrstuvwxyz'))
    for char in ciphered_text:
        if not char.isalnum():
            ciphered_text = ciphered_text.replace(char, '')
    return ciphered_text
