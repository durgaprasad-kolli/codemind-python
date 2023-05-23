a = int(input())
s=0
p=1
while a!=0:
    d=a%10
    s+=d
    p*=d
    a = a//10
if p==s:
    print("Spy Number")
else:
    print("Not Spy Number")