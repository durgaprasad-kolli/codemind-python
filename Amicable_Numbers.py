a = int(input())
b = int(input())
sum=0
count=0
for i in range(1,a-1):
    if a%i==0:
        sum+=i
for j in range(1,b-1):
    if b%j==0:
        count+=j
if count==a and sum==b:
    print("Amicable")
else:
    print("Not Amicable")
        