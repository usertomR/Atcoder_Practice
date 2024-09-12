N = int(input())
S_F_Arr = []

for _ in range(N):
  F, S = map(int, input().split())
  S_F_Arr.append((S, F))
S_F_Arr.sort()

s_max, F_smax = S_F_Arr.pop()

ans = 0
for s, f in S_F_Arr:
  if F_smax != f:
    s_sum = s_max + s
  else:
    s_sum = s_max + s // 2
  
  if s_sum > ans:
    ans = s_sum

print(ans)