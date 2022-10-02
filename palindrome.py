'''
WPP to check if given string is a palindrome
'''

def check_palindrome(s):
    n=len(s)
    mid=int(n/2)
    for i in range(mid):
        if s[i]!=s[n-1]:
            print("The given string is not a palindrome!")
            return False
        else:
            n-=1
    return True
s='ABCCBA'
val= check_palindrome(s)
if val==True:
    print("the given string is a palindrome!")
