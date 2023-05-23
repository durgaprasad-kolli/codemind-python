import math
x, y, m = map(int, input().split())
new = math.pow(x,y)
print(int(new%m))