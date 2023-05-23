import math as m
num = input()
int_num = int(num)
new_lst = [int(i) for i in num]
lst = [m.factorial(i) for i in new_lst]
s = 0
for k in lst:
    s+=k
if int_num == s:
    print(f"The number {int_num} is a strong number")
else :
    print(f"The number {int_num} is not a strong number")