def valid_palindrome(s):
    temp = ''.join(e for e in s if e.isalnum())
    print(temp.lower())
    return temp.lower() == temp[::-1].lower()
    
ans = valid_palindrome("A man, a plan, a canal: Panama")
print(ans)