from math import floor


def searchInsert(nums,target):
    left = 0
    right = len(nums) - 1
    
    while(left<=right):
        mid = floor(left + (right - left)/2)  
        
        if(nums[mid] == target):
            return mid
        elif(nums[mid]>target):
            right = mid-1
        else:
            left = mid+1
    return right+1


ans = searchInsert([1,3,5,6],2)
print(ans)