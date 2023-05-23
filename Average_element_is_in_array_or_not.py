
a = int(input())
k = list(map(int,input().split()))
c=0
for i in k:
    c+=i
p=(c//a)
for i in k:
    if p in k:
        print("True")
        break
    else:
        print("False")
        break
