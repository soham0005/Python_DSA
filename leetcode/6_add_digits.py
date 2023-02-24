def addDigits(num):
    num = [int(x) for x in num]
    return sum(num)

ans = addDigits("91")
print(ans)