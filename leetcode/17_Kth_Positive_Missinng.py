def KthMissingElement(arr,k):
    s = set(arr)
    for i in range(1,10000):
        if i not in s:
            if k == 1:
                return i
            k-=1
    
    
    
    
ans = KthMissingElement([2,3,4,7,11],5)
print(ans)