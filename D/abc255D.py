import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ruiseki = [0]
for i in range(N):
  ruiseki.append(ruiseki[-1] + A[i])

for _ in range(Q):
  X = int(input())
  kosu_X_miman = bisect.bisect_left(A, X)

  print((X * kosu_X_miman - ruiseki[kosu_X_miman]) + (ruiseki[N] - ruiseki[kosu_X_miman] - X * (N - kosu_X_miman)))
