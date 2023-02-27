def kidsWithCandies(candies,extraCandies):
    finalAns = []
    for i in range(len(candies)):
        candies[i] += extraCandies
        if(max(candies) == candies[i]):
            finalAns.append(True)
            candies[i] -= extraCandies
        else:
            finalAns.append(False)
    print(finalAns)
    
    return [x+extraCandies >= max(candies) for x in candies]
        
        
ans = kidsWithCandies([12,1,12],10)