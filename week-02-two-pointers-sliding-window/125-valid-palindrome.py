#Cach 1
def isPalindrome(s):
    new = ""
    for i in s:
        if i.isalnum():
            new += i.lower()
    return new == new[::-1]

#Cach 2
def isPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        elif not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
    return True
