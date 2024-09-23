N, M = map(int, input().split())
neighor_node_edge_obj = {}

for n in range(1, N + 1):
  neighor_node_edge_obj[n] = []

for e in range(1, M + 1):
  u, v = map(int, input().split())

  neighor_node_edge_obj[u].append((v, e))
  neighor_node_edge_obj[v].append((u, e))

ans = "Yes"
AllAreaSeenNodeSet = set()
for n in range(1, N + 1):
  # 連結グラフのノード探索時に挿入
  if n in AllAreaSeenNodeSet:
    continue
  else:
    AreaSeenNodeSet = set()
    AreaSeenEdgeSet = set()
    stack = [n]
    AllAreaSeenNodeSet.add(n)
    AreaSeenNodeSet.add(n)
    prevNode = -1
    while stack:
      curNode = stack.pop()

      for nextNode, edge in neighor_node_edge_obj[curNode]:
        if nextNode != prevNode:
          if nextNode not in AreaSeenNodeSet:
            stack.append(nextNode)
          AllAreaSeenNodeSet.add(nextNode)
          AreaSeenNodeSet.add(nextNode)
          AreaSeenEdgeSet.add(edge)
      prevNode = curNode
    
    if len(AreaSeenNodeSet) != len(AreaSeenEdgeSet):
      ans = "No"
      break


print(ans)
