def findOccurence(haystack,needle):
    s = haystack.split(needle)
    print(s)
    return haystack.find(needle)
    
ans = findOccurence("sadbutsad","sad")
print(ans)