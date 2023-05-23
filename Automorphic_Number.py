a = int(input())
d = str(a)
b = a*a
c = str(b)
for i in range(len(c)):
    if d in c:
        print("Automorphic Number")
        break
    else:
        print("Not an Automorphic Number") 
        break