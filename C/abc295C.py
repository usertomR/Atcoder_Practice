N = int(input())
A = list(map(int, input().split()))

obj = {}
for a in A:
  if a not in obj:
    obj[a] = 1
  else:
    obj[a] += 1

ans = 0
for val in obj.values():
  ans += val // 2

print(ans)