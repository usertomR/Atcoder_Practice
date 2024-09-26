N, M, H, K = map(int, input().split())
S = input()
Item_Set = set()
for _ in range(M):
  x, y = map(int, input().split())
  Item_Set.add((x, y))

HitPoint = H
currPlaceArr = [0, 0]
ans = "Yes"
for s in S:
  H -= 1
  if s == "R":
    currPlaceArr[0] += 1
  elif s == "L":
    currPlaceArr[0] -= 1
  elif s == "U":
    currPlaceArr[1] += 1
  elif s == "D":
    currPlaceArr[1] -= 1

  if H < 0:
    ans = "No"
    break
    
  if (currPlaceArr[0], currPlaceArr[1]) in Item_Set and H < K:
    Item_Set.discard((currPlaceArr[0], currPlaceArr[1]))
    H = K

print(ans)
