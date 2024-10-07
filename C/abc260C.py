N, X, Y = map(int, input().split())

red_levelOne_only = False
blue_levelOne_Only = False
red_count_level_Arr = [0] * (N + 1)
blue_count_level_Arr = [0] * (N + 1)
red_count_level_Arr[N] = 1

while not(red_levelOne_only == True and blue_levelOne_Only == True):
  for red_level in reversed(range(2, N + 1)):
    if red_count_level_Arr[red_level] >= 1:
      red_count_level_Arr[red_level - 1] += 1 * red_count_level_Arr[red_level]
      blue_count_level_Arr[red_level] += X * red_count_level_Arr[red_level]
      
      red_count_level_Arr[red_level] = 0
  
  for blue_level in reversed(range(2, N + 1)):
    if blue_count_level_Arr[blue_level] >= 1:
      red_count_level_Arr[blue_level - 1] += 1 * blue_count_level_Arr[blue_level]
      blue_count_level_Arr[blue_level - 1] += Y * blue_count_level_Arr[blue_level]

      blue_count_level_Arr[blue_level] = 0
  
  red_levelOne_only = True
  blue_levelOne_Only = True
  for red_level in reversed(range(2, N + 1)):
    if red_count_level_Arr[red_level] >= 1:
      red_levelOne_only = False
      break
  
  for blue_level in reversed(range(2, N + 1)):
    if blue_count_level_Arr[blue_level] >= 1:
      blue_levelOne_Only = False
      break

print(blue_count_level_Arr[1])