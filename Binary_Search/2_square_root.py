def mySqrt(x):
    if x == 0:
        return 0
    
    left = 1
    right = x
    
    while(left<=right):
        mid = left + (right-left) // 2
        
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            right = mid - 1
        else:
            left = mid + 1
    return right

ans = mySqrt(16)
print(ans)