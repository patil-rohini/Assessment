def checkNumbers(numbers = []): 
    result = []  
    for i in numbers:   
        isDivisible = i%4==0 or i%6==0
        if(isDivisible):   
            result.append(i)  

    return result    
     

print(checkNumbers([1, 4, 6, 7, 8, 9, 20, 24]))   # returns [4, 6, 8, 20, 24] 
print(checkNumbers([3, 7, 9, 17]))  # return []


