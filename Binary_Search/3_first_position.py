def firstPosition(nums,target):
    start = 0
    end = len(nums) - 1
    occ = -1
    
    while(start<=end):
        mid = start + (end-start)//2
        if nums[mid] == target:
            occ = mid
            end = mid -1
        elif nums[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return occ

ans = firstPosition([1,2,4,5,5,5],5)
print(ans)
