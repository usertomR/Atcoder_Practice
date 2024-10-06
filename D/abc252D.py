N = int(input())
A = list(map(int, input().split()))

Number_kosu_obj = {}
for i in range(1, 2 * (10 ** 5) + 1):
  Number_kosu_obj[i] = 0

for a in A:
  Number_kosu_obj[a] += 1

ans = N * (N - 1) * (N - 2) // 6
for i in range(1, 2 * (10 ** 5) + 1):
  if Number_kosu_obj[i] >= 2:
    ans -= (Number_kosu_obj[i] * (Number_kosu_obj[i] - 1) // 2) * (N - 2 - (Number_kosu_obj[i] - 2))
  if Number_kosu_obj[i] >= 3:
    ans -= Number_kosu_obj[i] * (Number_kosu_obj[i] - 1) * (Number_kosu_obj[i] - 2) // 6

print(ans)