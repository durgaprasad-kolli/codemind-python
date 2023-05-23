def FactorSum(n):
    s = 0
    for i in range(1, n) :
        if n%i == 0 :
            s+=i
    return s
    
a = int(input())
b = int(input())
x = FactorSum(a)
y = FactorSum(b)
if x==b and y == a :
    print("Amicable")
else :
    print("Not Amicable")