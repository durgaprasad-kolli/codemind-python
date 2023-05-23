a = int(input())
k = list(map(int,input().split()))
h = int(input())
for i in k:
    if h in k:
        print("True")
        break
    else:
        print("False")
        break