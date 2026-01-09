def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if len(sentence) < 26:
        return False
    sentence = sentence.lower()  
    for char in alphabet:
        if char not in sentence:
            return False
    return True