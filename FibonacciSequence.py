def fibo(remain, pre1=1, pre2=1):
  cur = pre1 + pre2
  remain -= 1
  if remain == 0:
    print(cur)
  else:
    fibo(remain, pre2, cur)

#while True:
n = int(input("Enter nth term:	"))
if n == 1 or n == 2:
  print(1)
else:
  fibo(n - 2)