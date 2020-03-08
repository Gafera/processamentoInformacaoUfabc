def calc(n):
  i = 0
  while n > 1:
    print('{:.0f}'.format(n))
    if n % 2 == 0:
      n = n/2
    elif n % 2  != 0:
      n = n*3 + 1
  return '{:.0f}'.format(n)    

n = int(input())
print(calc(n))
