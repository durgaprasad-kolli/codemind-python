def p(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
a = int(input())
b = str(a)
c=0
if p(a) is True:
    while a!=0:
        d = a%10
        a = a//10
        if p(d) is True:
            c+=1
if c==len(b):
    print("Mega Prime")
else:
    print("Not Mega Prime")