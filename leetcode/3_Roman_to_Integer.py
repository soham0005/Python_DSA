def romanToInt(s):
    map = { 
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result=0;
    
    for i in range(len(s)-1):
        if map[s[i]] < map[s[i+1]]:
            result = result - map[s[i]]
        else:
            result = result + map[s[i]]
            
    return result+map[s[-1]]


ans = romanToInt("XII")
print(ans)