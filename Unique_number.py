a = input()
b=len(a)
c=0
for i in a:
    if a.count(i)==1:
        c+=1
if c==b:
    print("Unique Number")
else:
    print("Not Unique Number")