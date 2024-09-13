N = int(input())
A = list(map(int, input().split()))

if N == 1:
  print(A[0])
elif N == 2:
  print(A[0] + 2 * A[1])
else:
  kisu_max = A[0]
  gusu_max = A[0] + 2 * A[1]
  for i in range(2, N):
    tmp_g = gusu_max
    tmp_k = kisu_max
    gusu_max = max(tmp_k + 2 * A[i], tmp_g)
    kisu_max = max(tmp_g + A[i], tmp_k)

  print(max(kisu_max, gusu_max))