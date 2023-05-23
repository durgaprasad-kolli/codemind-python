a = input()
b = a[::-1]
k=[]
for i in b:
    k.append(i)
for j in range(0,len(k)):
    if k[0]=="0":
        k.remove(k[0])
    elif k[-1]=="-":
        k.remove(k[-1])
        k.insert(0,"-")
for l in k:
    print(l,end='')
    
    