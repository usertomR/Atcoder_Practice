N, M = map(int, input().split())
A = list(map(int, input().split()))

a_idx = 0
for i in range(1, N + 1):
  if i < A[a_idx]:
    print(A[a_idx] - i)
  else:
    print(0)
    a_idx += 1
