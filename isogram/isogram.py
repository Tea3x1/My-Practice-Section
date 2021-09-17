def is_isogram(string):
    string = [x.upper() for x in string if x.isalpha()]
    return len(set(string)) == len(list(string))
