import itertools

S_list = []
for _ in range(9):
  S_list.append(input())

ans = 0
for pattern in itertools.combinations(list(range(81)), r=4):
    a, b, c, d = pattern
    ax, ay = a % 9, a // 9
    bx, by = b % 9, b // 9
    cx, cy = c % 9, c // 9
    dx, dy = d % 9, d // 9

    if S_list[ay][ax] == "#" and S_list[by][bx] == "#" and S_list[cy][cx] == "#" and S_list[dy][dx] == "#":
      kind = set()
      for pt in itertools.combinations([(ax, ay),(bx, by),(cx, cy),(dx, dy)], r=2):
        J, P = pt
        jx, jy = J
        px, py = P

        kind.add((jy - py) ** 2 + (jx - px) ** 2)

      if len(kind) == 2:
        u, m = kind
        if u == 2*m or m == 2*u:
          ans += 1

      #print("=======", (ax, ay), (bx, by), (cx, cy), (dx, dy), distpow2_ab, distpow2_bc, distpow2_cd, distpow2_da)

      

print(ans)
