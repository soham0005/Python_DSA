def twoSum(nums,target):
    map = {}
    
    for i in range(len(nums)):
        ele = target - nums[i]
        
        if ele not in map:
            map[nums[i]] = i
        else:
            return [map[ele],i]