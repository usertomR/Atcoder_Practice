N, K = map(int, input().split())
R = list(map(int, input().split()))
ansArr = []

def suuretu(stateArr, digit):
  for r in range(1, R[digit - 1] + 1):
    otherArr = stateArr[:]
    otherArr.append(r)
    if digit == N:
      ansArr.append(otherArr)
    else:
      suuretu(otherArr, digit + 1)

suuretu([], 1)

#print("---", ansArr)

for e in ansArr:
  if sum(e) % K == 0:
    print(*e)