H, W = map(int, input().split())
C = []
for _ in range(H):
  C.append(input())

S = [0] * min(H, W)

def batu_or_not(center_mass, size):
  h, w = center_mass
  
  if h + size <= H - 1 and 0 <= h - size and w + size <= W - 1 and 0 <= w - size:
    if C[h + size][w + size] == "#" and C[h + size][w - size] == "#" and C[h - size][w + size] == "#" and C[h - size][w - size] == "#":
      return True
    else:
      return False
  else:
    return False

for h in range(H):
  for w in range(W):
    if batu_or_not((h, w), 1):
      zantei_size = 1
      while True:
        if batu_or_not((h, w), zantei_size + 1):
          zantei_size += 1
        else:
          S[zantei_size - 1] += 1
          break

print(*S)
