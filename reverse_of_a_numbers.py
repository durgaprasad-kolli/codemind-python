n = int(input())
rem = 0
while n>0 :
    rem = (rem*10) + (n%10)
    n//=10
print(rem)