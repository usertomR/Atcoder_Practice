N, L, R = map(int, input().split())
A = list(map(int, input().split()))

L_min_Arr = []
R_min_Arr = []

a_ruiseki = 0
for i in range(N):
  a_ruiseki += A[i]
  if i == 0:
    L_min_Arr.append(L *(i + 1) - a_ruiseki)
  else:
    L_min_Arr.append(min(L_min_Arr[i - 1], L *(i + 1) - a_ruiseki))


a_ruiseki = 0
for i in range(N):
  a_ruiseki += A[N - 1 - i]
  if i == 0:
    R_min_Arr.append(R * (i + 1) - a_ruiseki)
  else:
    R_min_Arr.append(min(R_min_Arr[i - 1], R * (i + 1) - a_ruiseki))


#print(L_min_Arr, R_min_Arr)

sum_A = sum(A)
ans = min(sum_A + R_min_Arr[N - 1], sum_A)
for l_idx in range(N - 1):
  ans = min(ans, sum_A + L_min_Arr[l_idx] + R_min_Arr[N - 2 - l_idx])
ans = min(ans, sum_A + L_min_Arr[N - 1])

print(ans)