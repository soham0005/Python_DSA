def findInsertPosition(nums,target):
    nums.append(target)
    nums.sort()
    print(nums.index(target))
    
findInsertPosition([1,2,31,2321,1,12],19)

    