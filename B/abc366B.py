N = int(input())

first_status_Arr = [""] * N
All_T = []
for i in range(100):
  All_T.append(first_status_Arr[:])

M = 0
for i in range(N):
  S = input()

  S_len = len(S)
  if S_len > M:
    M = S_len
  
  for j in range(S_len):
    #print("?????", S[j], All_T[j])
    All_T[j][N - i - 1] = S[j]
  
  
  
  
  


for i in range(100):
  flg = 0
  for n in reversed(range(N)):
    if flg == 0:
      if All_T[i][n] != "":
        flg = 1
    else:
      if All_T[i][n] == "":
        All_T[i][n] = "*"

for m in range(M):
  print("".join(All_T[m]))

