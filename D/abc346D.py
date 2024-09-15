N = int(input())
S = input()
C = list(map(int, input().split()))

SumCost_right_00 = 0
SumCost_right_11 = 0
SumCost_left_00 = 0
SumCost_left_11 = 0
costS0 = 0
costS1 = 0
if S[0] != "0":
  costS0 = C[0]
if S[1] != "0":
  costS1 = C[1]
costS2ikou_00 = 0
curbit = 1
sumCost_2ikou = 0
for i in range(2, N):
  sumCost_2ikou += C[i]

  #print("curbit S[i]" ,curbit, S[i])
  if str(curbit) != S[i]:
    costS2ikou_00 += C[i]
  curbit = (curbit + 1) % 2

#print("costS2ikou_00", costS2ikou_00)

SumCost_right_00 = costS2ikou_00
SumCost_right_11 = sumCost_2ikou - costS2ikou_00
ans = min(costS0 + costS1 + costS2ikou_00, (C[0] + C[1] - (costS0 + costS1)) + sumCost_2ikou - costS2ikou_00)

#print("最初の1歩", costS0 + costS1 + costS2ikou_00, (C[0] + C[1] - (costS0 + costS1)) + sumCost_2ikou - costS2ikou_00)


if N == 2:
  pass
else:
  for i in range(N - 2):
    idx_i_cost_00 = 0
    if S[i] != "1":
      idx_i_cost_00 += C[i]
    
    idx_iplus1_cost_00 = 0
    if S[i + 1] != "0":
      idx_iplus1_cost_00 += C[i + 1]
    
    idx_iplus2_cost_00 = 0
    if S[i + 2] != "0":
      idx_iplus2_cost_00 += C[i + 2]
    
    cost_00 = (SumCost_left_11 + idx_i_cost_00) + idx_iplus1_cost_00 + idx_iplus2_cost_00 + (SumCost_right_11 - idx_iplus2_cost_00)
    cost_11 = (SumCost_left_00 + (C[i] - idx_i_cost_00)) + (C[i + 1] - idx_iplus1_cost_00) + (C[i + 2] - idx_iplus2_cost_00) + (SumCost_right_00 - (C[i + 2] - idx_iplus2_cost_00))

    if ans > cost_00:
      ans = cost_00
    if ans > cost_11:
      ans = cost_11
    
    tmp_left_00 = SumCost_left_00
    tmp_right_00 = SumCost_right_00
    SumCost_left_00 = (SumCost_left_11 + idx_i_cost_00)
    SumCost_right_00 = (SumCost_right_11 - idx_iplus2_cost_00)
    SumCost_left_11 = (tmp_left_00 + (C[i] - idx_i_cost_00))
    SumCost_right_11 = tmp_right_00 - (C[i + 2] - idx_iplus2_cost_00)
print(ans)