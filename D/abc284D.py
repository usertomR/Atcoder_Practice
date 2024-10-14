import math


T = int(input())

for _ in range(T):
  N = int(input())

  for i in range(2, 3 * (10 ** 6) + 1):
    p, q = (0, 0)

    if N % i == 0:
      if N % i**2 == 0:
        p = i
        q = N // i**2
      else:
        p = int(math.sqrt(N // i))
        q = i
      break
  
  print(p, " ", q)
  
