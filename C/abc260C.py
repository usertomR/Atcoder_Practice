N, X, Y = map(int, input().split())

red_Arr = [0] * (N + 1)
blue_Arr = [0] * (N + 1)
red_Arr[N] = 1

for level in reversed(range(2, N + 1)):
  red_Arr[level - 1] += red_Arr[level]
  blue_Arr[level] += X * red_Arr[level]
  red_Arr[level] = 0

  red_Arr[level - 1] += blue_Arr[level]
  blue_Arr[level - 1] += Y * blue_Arr[level]
  blue_Arr[level] = 0

print(blue_Arr[1])