def detectCapital(word):
    import string
    if word ==  word.lower() or word == word.upper() or word == string.capwords(word):
        return True
    else:
        return False

ans = detectCapital("USA")
print(ans)
