import itertools


N, M = map(int, input().split())
T_list = []
for _ in range(N):
  T_list.append(input())

ans = ""
for narabekae in itertools.permutations(range(N), r=N):
  ans = "Yes"
  for T_idx in range(N - 1):
    diff_cnt = 0
    for char_idx in range(M):
      if T_list[narabekae[T_idx]][char_idx] != T_list[narabekae[T_idx + 1]][char_idx]:
        diff_cnt += 1
    if diff_cnt != 1:
      ans ="No"
  if ans == "Yes":
    break

print(ans)
