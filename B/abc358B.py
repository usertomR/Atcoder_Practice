import collections

N, A = map(int, input().split())
T = list(map(int, input().split()))

deq = collections.deque([])
time = T[0]
deq.append(0)

while True:
  tempPerson = deq[-1]
  nextPerson = deq.popleft()
  prevtime = time
  time += A
  
  print(time)
  if nextPerson + 1 == N:
    break
  
  for t in T:
    if prevtime < t <= time:
      tempPerson += 1
      deq.append(tempPerson)

  # あとで消す。
  #print("nextPerson:",nextPerson, "prevtime:", prevtime, "time:", time, "tempPerson:", tempPerson)
  
  if deq:
    pass
  else:
    time = T[tempPerson + 1]
    deq.append(tempPerson + 1)
