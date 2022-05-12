string = input("Enter the string: ")  
# input function which specify the message, and it is store in variable string

reverse = string[::-1]
# s -> means slicing the string
# :: -> starting and ending point, important to specify if not it will take the entire string
# -1 -> reverse the string
# It is store in reverse variable

# check whether the original value enter by user is the reverse of the value 
# for which if statement is used

if( string == reverse):
    print("Yes, It is palindrome")
else:
    print("No, It is not palindrome")

