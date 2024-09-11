import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A_ruiseki = []
A_ruiseki.append(A[0])
for i in range(1, N):
  A_ruiseki.append(A_ruiseki[i - 1] + A[i])

if M >= A_ruiseki[-1]:
  print("infinite")
else:
  x_mid = None
  left = 0
  right = 10 ** 9
  while left <= right:
    x_mid = (left + right) // 2
    sum_xIka = bisect.bisect_left(A, x_mid)
    if sum_xIka == 0:
      Cost = N * x_mid
    else:
      Cost = A_ruiseki[sum_xIka - 1] + x_mid * (N - sum_xIka)
    
    if Cost > M:
      right = x_mid
    else:
      if M >= Cost + (N - sum_xIka):
        left = x_mid
      else:
        break
  
  print(x_mid)
