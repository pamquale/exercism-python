def translate(text):
    words = text.split()
    translated_words = []
    for word in words:
        vowels = 'a', 'e', 'i', 'o', 'u'
        for index, char in enumerate(word):
            if word.startswith(vowels) or word.startswith(('xr', 'yt')):
                translated_words.append(word + 'ay')
                break
            if char in vowels:
                translated_words.append(word[index:] + word[:index] + 'ay')
                break
            if char == 'q' and word[index + 1] == 'u':
                translated_words.append(word[index + 2:] + word[:index + 2] + 'ay')
                break
            if word[index] == 'y' and index != 0:
                translated_words.append(word[index:] + word[:index] + 'ay')
                break
    return ' '.join(translated_words)