def checkPalindrome(inputString):
    if(inputString == inputString[::-1]):
        return True
    else:
        return False

print(checkPalindrome("radar")) # return true
print(checkPalindrome("apple")) # return false

