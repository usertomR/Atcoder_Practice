import sortedcontainers


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
A = sortedcontainers.SortedList(A)

buyFlg = 1
rest = len(A)
ans = 0

for b in B:
  idx = A.bisect_left(b)

  if idx == rest:
    buyFlg = 0
    break
  else:
    ans += A[idx]
    A.pop(idx)
    rest -= 1

if buyFlg == 0:
  print(-1)
else:
  print(ans)