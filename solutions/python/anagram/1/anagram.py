def find_anagrams(word, candidates):
    word_sorted = sorted(word.lower())
    result = []
    for wrd in candidates:
        if sorted(wrd.lower()) == word_sorted and word.lower() != wrd.lower():
            result.append(wrd)
    return result
