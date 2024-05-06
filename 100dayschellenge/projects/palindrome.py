"""a = input("Enter the number")
b = len(a)
c = ""
d = ""
if len(a) % 2 == 0:
    e = int(b/2)
    c = a[:e]
    d = a[e:]
else:
    e = int((len(a) - 1)/2)
    c = a[:e]
    d = a[e + 1:][::-1]

if c == d:
    print("True")
else:
    print("False")
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        #print(a)
        b = len(a)
        c = ""
        d = ""
        if len(a) % 2 == 0:
            e = int(b/2)
            c = a[:e]
            d = a[e:][::-1]
        else:
            e = int((len(a) - 1)/2)
            c = a[:e]
            d = a[e + 1:][::-1]

        print(d)
        print(c)
        if c == d:
            return True
        else:
            return False

f = int(input("Enter the word"))
solution = Solution()
print(solution.isPalindrome(f))