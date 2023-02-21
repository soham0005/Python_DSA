# def singleNonDuplicate(nums):
#     ans = 0
#     for i in range(0,len(nums)):
#         ans = ans ^ nums[i]
#     print(ans)
  
  
 
  
import math


def singleNonDuplicate(nums):
    start = 0
    end = len(nums)
    while(start <= end):
        mid = math.floor(start + (end - start)/2)
        
        if(mid > 0 and mid < len(nums)):
            if(nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]):
                return nums[mid]
            elif(nums[mid] == nums[mid -1] and mid % 2 == 1) or (nums[mid] == nums[mid+1] and mid % 2 ==0):
                start = mid+1
            else:
                end = mid-1 
    return 0
ans = singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print(ans)
            