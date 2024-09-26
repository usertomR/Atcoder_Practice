N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for a in range(10 ** 6 + 1):
  RestMaterialArr = Q[:]

  notCookFlg = 0
  for n in range(N):
    RestMaterialArr[n] -= A[n] * a
    if RestMaterialArr[n] < 0:
      notCookFlg = 1
  
  if notCookFlg == 1:
    break
  
  b = 10 ** 10
  for n in range(N):
    if B[n] >= 1 and b > RestMaterialArr[n] // B[n]:
      b = RestMaterialArr[n] // B[n]
  
  if ans < a + b:
    ans = a + b
    
print(ans)
  
  



