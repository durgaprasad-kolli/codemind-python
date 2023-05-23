def Palindrome(n):
    rev = 0
    while (n>0) :
        rev = (rev*10) + (n%10)
        n//=10
    return rev

t = int(input())
for i in range(t):
    num = int(input())
    x = Palindrome(num)
    if x == num :
        print("True")
    else :
        print("False")