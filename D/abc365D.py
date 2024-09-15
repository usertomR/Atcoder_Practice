N = int(input())
S = input()

dp_hikiwake = [0] * N
dp_kachi = [0] * N
dp_kachi[0] = 1
obj_henkan = {"R":0, "P":1, "S":2}

for i in range(1, N):
  aoki_prev = obj_henkan[S[i - 1]]
  aoki_curr = obj_henkan[S[i]]

  takahashi_prev_kachi = (aoki_prev + 1) % 3
  takahashi_prev_hikiwake = aoki_prev

  #引き分け
  dp_takahashi_curr_hikiwake = -1
  if takahashi_prev_hikiwake != aoki_curr:
    dp_takahashi_curr_hikiwake = dp_hikiwake[i - 1]
  if takahashi_prev_kachi != aoki_curr:
    if dp_kachi[i - 1] > dp_takahashi_curr_hikiwake:
      dp_takahashi_curr_hikiwake = dp_kachi[i - 1]
  dp_hikiwake[i] = dp_takahashi_curr_hikiwake

  #勝ち
  dp_takahashi_curr_kachi = -1
  if takahashi_prev_hikiwake != (aoki_curr + 1) % 3:
    dp_takahashi_curr_kachi = dp_hikiwake[i - 1] + 1
  if takahashi_prev_kachi != (aoki_curr + 1) % 3:
    if dp_kachi[i - 1] + 1 > dp_takahashi_curr_kachi:
      dp_takahashi_curr_kachi = dp_kachi[i - 1] + 1
  dp_kachi[i] = dp_takahashi_curr_kachi

print(max(dp_kachi[N - 1], dp_hikiwake[N - 1]))