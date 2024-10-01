N = int(input())
sx, sy, tx, ty = map(int, input().split())

# idxは1からNまで
x_y_r_Arr = [None]
for _ in range(N):
  x_y_r_Arr.append(list(map(int, input().split())))

#print("sssssssss" ,x_y_r_Arr)

neighborCircleIdx_obj = {}
for n in range(1, N + 1):
  neighborCircleIdx_obj[n] = []

for i in range(1, N + 1):
  for j in range(1, N + 1):
    if i == j:
      pass
    
    xi, yi, ri = x_y_r_Arr[i]
    xj, yj, rj = x_y_r_Arr[j]

    if (ri - rj) ** 2 <= (xi - xj) ** 2 + (yi - yj) ** 2 <= (ri + rj) ** 2:
      neighborCircleIdx_obj[i].append(j)

start_circle_idx = -1
end_circle_idx = -1
for n in range(1, N + 1):
  xn, yn, rn = x_y_r_Arr[n]
  if (sx - xn) ** 2 + (sy - yn) ** 2 == rn ** 2:
    start_circle_idx = n
  
  if (tx - xn) ** 2 + (ty - yn) ** 2 == rn ** 2:
    end_circle_idx = n

if start_circle_idx == end_circle_idx:
  print("Yes")
else:
  stack = [start_circle_idx]
  ans = "No"
  Seen = set()
  Seen.add(start_circle_idx)
  while stack:
    cur_idx = stack.pop()
    Seen.add(cur_idx)
    if cur_idx == end_circle_idx:
      ans = "Yes"
      break

    for next_Idx in neighborCircleIdx_obj[cur_idx]:
      if next_Idx not in Seen:
        stack.append(next_Idx)
  
  print(ans)