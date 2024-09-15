N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

colorKindObj = {}
for m in range(1, M + 1):
  colorKindObj[m] = []

S_Arr = []
for i in range(N):
  S_Arr.append(S[i])
  colorKindObj[C[i]].append(i)

AnsStr_Arr = S_Arr[:]
for m in range(1, M + 1):
  colorM_kosu = len(colorKindObj[m])
  for idx_objArr in range(colorM_kosu):
    AnsStr_Arr[colorKindObj[m][idx_objArr]] = S_Arr[colorKindObj[m][(idx_objArr - 1) % colorM_kosu]]

print("".join(AnsStr_Arr))