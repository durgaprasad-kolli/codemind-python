a = input()
b = a[::-1]
c = int(a)
d = c*c
e = int(b)
f = e*e
g = str(f)[::-1]
h = str(d)
if(g==h):
    print("True")
else:
    print("False")