N, K, D = map(int, input().split())
A = list(map(int, input().split()))
# dp[n][k][d]
dp = [[[-1] * D for _ in range(N)] for _ in range(N)]
dp[0][0][A[0] % D] = A[0] 

for n in range(1, N):
  # n + 1番目の項を入れる・入れない
  a_mod = A[n] % D
  # aを入れない場合
  for k in range(n):
    for d in range(D):
      dp[n][k][d] = dp[n - 1][k][d]

  # aを入れて最大値を更新できるなら更新
  # 合計k+1個取り入れる
  for k in range(n + 1):
    if k == 0:
      dp[n][k][a_mod] = max(A[n], dp[n][k][a_mod])
      continue
    for d in range(D):
      orig = dp[n - 1][k - 1][d]
      if orig == - 1:
        continue
      else:
        dp[n][k][(orig % D + a_mod) % D] = max(dp[n][k][(orig % D + a_mod) % D], dp[n - 1][k - 1][d] + A[n])

print(dp[N - 1][K - 1][0])


  