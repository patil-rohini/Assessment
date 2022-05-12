def getNumbers(numbers = []): # function to get array
    result = []  # to return the output
    for i in numbers:   # for loop to identify the multiplier 
        isDivisible = i%4==0 or i%6==0
        if(isDivisible):   # if statement for the true false conditions
            result.append(i)  # id statement is true it will append into the result array

    return result     # final array will return
     

print(getNumbers([1, 4, 6, 7, 8, 9, 24]))      # calling function


