N, M = map(int, input().split())
L = list(map(int, input().split()))
maxElement = max(L)

left = 0
right = 2 * 10 ** 15
ans = -1
while left + 1< right:
  #print(left, right)
  w = (left + right) // 2
  if w < maxElement:
    left = w
    continue
  
  line = 1
  tmp = 0
  for l in L:
    tmp += l
    if tmp < w:
      tmp += 1
    elif tmp == w:
      tmp = 0
      line += 1
    else:
      tmp = l + 1
      line += 1
  if tmp == 0:
    line -= 1

  #print(line, tmp)

  if line <= M:
    right = w
    ans = w
  else:
    left = w

print(ans)
    
