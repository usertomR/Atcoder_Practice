N, A, B = map(int, input().split())
S = input()
S_plus_S_Str = S + S

ans = 10 ** 20
for i in range(N):
  a = A * i
  b = 0

  left_idx = i
  right_idx = i + (N - 1)
  while left_idx <= right_idx:
    if S_plus_S_Str[left_idx] != S_plus_S_Str[right_idx]:
      b += B
    left_idx += 1
    right_idx -= 1

  if ans > a + b:
    ans = a + b

print(ans)
