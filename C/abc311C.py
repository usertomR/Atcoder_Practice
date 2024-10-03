N = int(input())
A = list(map(int, input().split()))

obj = {}

for i in range(N):
  obj[i + 1] = A[i]

Seen = set()
BM_Node = -1
keiro = []
for n in range(1, N + 1):
  if n not in Seen:
    stack = [n]
    keiro = []
    while stack:
      curNode = stack.pop()
      Seen.add(curNode)
      keiro.append(curNode)
      if obj[curNode] in Seen:
        BM = obj[curNode]
        break
      stack.append(obj[curNode])
  
  if BM >= 1:
    break

startIdx = -1
for i in range(len(keiro)):
  if keiro[i] == BM:
    startIdx = i
    break

print(len(keiro[startIdx:]))
print(*keiro[startIdx:])