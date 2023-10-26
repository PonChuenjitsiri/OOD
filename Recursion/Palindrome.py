def is_Palindrome(str):
    if len(str) == 0:
        return print(True)

    if str[0] == str[-1]:
        return is_Palindrome(str[1:-1:])
    
    return print(False)

is_Palindrome("abbb")