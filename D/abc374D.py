import itertools
import math

N, S, T = map(int, input().split())
# 0 ~ N-1
Senbun_hashi_Arr = []
for i in range(N):
  A, B, C, D = map(int, input().split())
  Senbun_hashi_Arr.append([(A, B), (C, D)])
# 0 ~ N-1
Write_order_Arr = []
if N == 1:
  Write_order_Arr.append([0])
else:
  for P in itertools.permutations(list(range(N)), r=N):
    Write_order_Arr.append(P)

ans = 10 ** 10
for order in Write_order_Arr:
  for state in range((2 ** N)):
    state_binStr = bin(state)[2:]
    len_binStr = len(state_binStr)
    state_binStr = "0" * (N - len_binStr) + state_binStr

    moveDistance_Arr = []
    writeDistance_Arr = []
    curPoint = (0, 0)
    for sen_idx in range(N):
      moveDistance_Arr.append(math.sqrt((curPoint[0] - Senbun_hashi_Arr[order[sen_idx]][int(state_binStr[sen_idx])][0]) ** 2 + (curPoint[1] - Senbun_hashi_Arr[order[sen_idx]][int(state_binStr[sen_idx])][1]) ** 2))
      writeDistance_Arr.append(math.sqrt((Senbun_hashi_Arr[order[sen_idx]][0][0] - Senbun_hashi_Arr[order[sen_idx]][1][0]) ** 2 + (Senbun_hashi_Arr[order[sen_idx]][0][1] - Senbun_hashi_Arr[order[sen_idx]][1][1]) ** 2))
      if state_binStr[sen_idx] == "0":
        curPoint = Senbun_hashi_Arr[order[sen_idx]][1]
      else:
        curPoint = Senbun_hashi_Arr[order[sen_idx]][0]
    
    if ans > (sum(moveDistance_Arr) / S + sum(writeDistance_Arr) / T):
      ans = (sum(moveDistance_Arr) / S + sum(writeDistance_Arr) / T)
    
print(ans)