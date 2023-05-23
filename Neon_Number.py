def Sum(n):
    s = 0
    while n>0 :
        s+=n%10
        n//=10
    return s
a = int(input())
sq = a*a
b = Sum(sq)
if a == b:
    print("Neon Number")
else :
    print("Not Neon Number")