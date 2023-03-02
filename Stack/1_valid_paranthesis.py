def validParanthesis(s):
    data = {"(":")","{":"}","[":"]"}
    stack =[]
    
    for i in s:
        if i in data:
            stack.append(i)
        elif len(stack) == 0 or data[stack.pop()]!=i:
            return False
    return len(stack) == 0

ans = validParanthesis("()")
print(ans)
            