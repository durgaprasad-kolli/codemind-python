a = int(input())
c=0
for j in range(1,a-1):
    if a%j==0:
        c+=j
if c>a:
    print("True")
else:
    print("False")
        