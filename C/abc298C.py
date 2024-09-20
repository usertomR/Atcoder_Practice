from sortedcontainers import SortedList, SortedSet


N = int(input())
Q = int(input())

boxList = [None]
numberObj = {}
for i in range(1, 2 * (10 ** 5) + 1):
  boxList.append(SortedList([]))
  numberObj[i] = SortedSet([])

for _ in range(Q):
  query = list(map(int, input().split()))

  if query[0] == 1:
    boxList[query[2]].add(query[1])
    numberObj[query[1]].add(query[2])
  elif query[0] == 2:
    print(*boxList[query[1]][:])
  elif query[0] == 3:
    print(*numberObj[query[1]][:])