def encode(plain_text):
    plain_text = plain_text.lower()
    plain_text = filter(str.isalnum, plain_text)
    plain_text = ''.join(plain_text)
    plain_text = plain_text.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))
    ciphered_text = []
    for i in range(0, len(plain_text), 5):
        ciphered_text.append(plain_text[i:i+5])
    return ' '.join(ciphered_text)
        

def decode(ciphered_text):
    ciphered_text = ciphered_text.lower()
    ciphered_text = ciphered_text.translate(str.maketrans('zyxwvutsrqponmlkjihgfedcba','abcdefghijklmnopqrstuvwxyz'))
    return ciphered_text.replace(' ', '')
