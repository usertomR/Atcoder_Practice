N = int(input())
AnsArr = []
for i in range(3 ** N):
  AnsArr.append(["?"] * (3 ** N))


def carpet(level, startIdx_H, startIdx_W):
  if level == 0:
    AnsArr[startIdx_H][startIdx_W] = "#"
    return
  else:
    #???
    #print("level_range", level, startIdx_H, startIdx_W)
    for h_kbn in range(3):
      for w_kbn in range(3):
        sIdx_h = (3 ** (level - 1)) * h_kbn + startIdx_H
        eIdx_h = (3 ** (level - 1)) * (h_kbn + 1) - 1 + startIdx_H
        sIdx_w = (3 ** (level - 1)) * w_kbn + startIdx_W
        eIdx_w = (3 ** (level - 1)) * (w_kbn + 1) - 1 + startIdx_W

        if h_kbn == 1 and w_kbn == 1:
          #???
          #print("WhiteChk", sIdx_h, eIdx_h, sIdx_w, eIdx_w)
          for h in range(sIdx_h, eIdx_h + 1):
            for w in range(sIdx_w, eIdx_w + 1):
              AnsArr[h][w] = "."
        else:
          carpet(level - 1, sIdx_h, sIdx_w)

carpet(N, 0, 0)

for h in range(3 ** N):
  print("".join(AnsArr[h]))

  
