#primes in range
m=int(input())
n =int(input())
f = 0
for i in range(m,n):
    if(i>1):
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)
            