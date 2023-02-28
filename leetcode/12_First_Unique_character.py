def firstUniqueCharacter(s):
    for i in s:
        if s.rindex(i) == s.index(i):
            return s.index(i)
    return -1

ans = firstUniqueCharacter("laeetlcode")
print(ans)