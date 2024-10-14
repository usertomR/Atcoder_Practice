import sys


N = int(input())
neighbor_obj = {}
AllNameSet = set()

for i in range(N):
  S, T = input().split()

  AllNameSet.add(S)
  AllNameSet.add(T)

  if S not in neighbor_obj:
    neighbor_obj[S] = [T]
  else:
    neighbor_obj.append(T)

Seen = set()
for name in AllNameSet:
  if name not in Seen:
    stack = [name]
    circle_Seen = set()
    while stack:
      curName = stack.pop()
      Seen.add(curName)
      circle_Seen.add(curName)

      if curName in neighbor_obj:
        for nextName in neighbor_obj[curName]:
          if nextName in circle_Seen:
            print("No")
            sys.exit()
          else:
            stack.append(nextName)

print("Yes")
      