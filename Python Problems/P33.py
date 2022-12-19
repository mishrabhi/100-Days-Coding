# Get an input string from the user and then check whether it is a palindrome string or not.

def isPalindrome(string):
    if (string == string[::-1]):
        return "The string is Palindrome"
    else:
        return "The string is not a Palindrome"
string = input("Enter String: ")
print(isPalindrome(string))