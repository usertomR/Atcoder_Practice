N = int(input())
S = input()
S_Arr = []
Q = int(input())
Q_Arr = []
transitionIdx = -1

for n in range(N):
  S_Arr.append(S[n])

for q in range(Q):
  t, x, c = input().split()
  t, x = int(t), int(x)
  if t != 1:
    transitionIdx = q
  Q_Arr.append((t, x, c))

for q in range(Q):
  t, x, c = Q_Arr[q]

  if t == 1:
    S_Arr[x - 1] = c
  
  if transitionIdx == q:
    if t == 2:
      for n in range(N):
        S_Arr[n] = S_Arr[n].lower()
    elif t == 3:
      for n in range(N):
        S_Arr[n] = S_Arr[n].upper()

print("".join(S_Arr))