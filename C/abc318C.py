N, D, P = map(int, input().split())
F = list(map(int,input().split()))
F = sorted(F, reverse=True)
F_ruisekiArr = [0, F[0]]
for i in range(1, N):
  F_ruisekiArr.append(F_ruisekiArr[-1] + F[i])
canUseDays = N
ans = sum(F)
haveUsedIdx = 0

while canUseDays > 0:
  TargetDays = min(canUseDays, D)
  sagaku = F_ruisekiArr[haveUsedIdx + TargetDays] - F_ruisekiArr[haveUsedIdx] - P
  if sagaku > 0:
    ans -= sagaku
    canUseDays -= TargetDays
    haveUsedIdx += TargetDays
  else:
    break

print(ans)
