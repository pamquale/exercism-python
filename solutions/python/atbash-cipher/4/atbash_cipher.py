def encode(plain_text):
    plain_text = ''.join(char for char in plain_text.lower() if char.isalnum())
    plain_text = plain_text.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))
    return ' '.join(plain_text[i:i+5] for i in range(0, len(plain_text), 5))
        
def decode(ciphered_text):
    ciphered_text = ciphered_text.translate(str.maketrans('zyxwvutsrqponmlkjihgfedcba','abcdefghijklmnopqrstuvwxyz'))
    return ciphered_text.replace(' ', '')
