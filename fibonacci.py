def fibonacci(n):
  a, b = 0, 1
  result = []
  for i in range(n):
    result.append(a)
    a, b = b, a+b
  for j in result:
      print(j,end=" ")
a=int(input())
fibonacci(a)
