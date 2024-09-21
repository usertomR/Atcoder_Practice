N = int(input())
dp_a = [0] * N
dp_b = [0] * N

for i in range(N):
  a, b = map(int, input().split())
  if i == 0:
    dp_a[0] = 1
    dp_b[0] = 1
    prev_a = a
    prev_b = b
    continue

  if prev_a != a:
    dp_a[i] += dp_a[i - 1] % 998244353
  if prev_b != a:
    dp_a[i] += dp_b[i - 1] % 998244353
  if prev_a != b:
    dp_b[i] += dp_a[i - 1] % 998244353
  if prev_b != b:
    dp_b[i] += dp_b[i - 1] % 998244353
  
  prev_a = a
  prev_b = b

print((dp_a[N - 1] + dp_b[N - 1]) % 998244353)
