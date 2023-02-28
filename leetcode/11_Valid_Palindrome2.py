def valindPalindrome(s):
    start = 0
    end = len(s)-1
    
    while(start<end):
        if s[start] == s[end]:
            start+=1
            end-=1
        else:
            tempI = s[:start] + s[start+1:]
            tempJ = s[:end] + s[end+1:]
            if tempI == tempI[::-1] or tempJ == tempJ[::-1]:
                return True
            else:
                return False
    return True

ans = valindPalindrome("aba")
print(ans)
                
        