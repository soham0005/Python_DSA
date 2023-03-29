# Return the count of substrings in which the lower and upper case are equal

def countSubstring(s):
    #Brute Force Approach
    ans = 0
    lowerCase,upperCase = 0,0
    for i in range(len(s)):
        lowerCase = 0
        upperCase = 0
        for j in range(i,len(s)):
            if s[j].islower():
                lowerCase+=1
            else:
                upperCase+=1
            
            if lowerCase == upperCase:
                ans+=1
    print(ans)
    
countSubstring("gEEk")