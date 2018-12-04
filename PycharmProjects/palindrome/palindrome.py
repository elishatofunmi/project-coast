# To check if two numbers are palindrome of one another
# check for the length of each number/ else raise len error using try and except
# using list comprehension append each element into a list
# check list

def Palindrome(x, y):
    if len(str(x))== len(str(y)):
        solution = 'unknown'
        name = [i for i in str(x)]
        name_check = [j for j in str(y)]
        solution = (name == name_check)
    else:
        "X and Y are not having equal length"
    return solution


output = Palindrome(234, 2345)
print (output)