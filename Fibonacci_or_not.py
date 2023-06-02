n = 100
a, b = 0, 1
lst = []
for i in range(n):
    lst.append(a)
    c = a+b
    a, b = b, c

n = int(input())
if n in lst :
    print("True")
else :
    print("False")