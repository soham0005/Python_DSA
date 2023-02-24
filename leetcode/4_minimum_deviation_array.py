def minimumDeviation(nums):
    smallest = min(nums)
    largest = max(nums)
    print(largest,smallest)
    small_index = nums.index(smallest)
    largest_index = nums.index(largest)
    
    if smallest % 2 == 0:
        smallest = smallest / 2
    elif smallest % 2 != 0:
        smallest *= 2
    elif largest % 2 == 0:
        print("helllo")
        largest = largest / 2
    else:
        largest *= 2
    print(largest,smallest)
        
    

minimumDeviation([1,2,3,1,3,12,30])
    
    
