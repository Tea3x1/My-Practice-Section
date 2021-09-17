def find_anagrams(word, candidates):
    return [i for i in candidates if sorted(i.lower()) == sorted(word.lower()) and i.lower() != word.lower()]
