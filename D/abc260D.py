from sortedcontainers import SortedList

N, K = map(int, input().split())
P = list(map(int, input().split()))

# 添字 = カード番号。全部-1(cannot Eat)で初期化
eat_turn_Arr = [-1] * (N + 1)

number_in_place = SortedList([])
for n in range(N):
  cur_cardNo = P[n]

  grp_No, grp_card_kosu, grp_set = 0, 0, set()

  if len(number_in_place) == 0:
    grp_set.add(cur_cardNo)
    grp_card_kosu = 1
    grp_No = cur_cardNo
    number_in_place.add((grp_No, grp_set))
  else:
    insert_idx = number_in_place.bisect_left((cur_cardNo, set()))
    if insert_idx == len(number_in_place):
      # 場にカードがない場合と同じ
      grp_set.add(cur_cardNo)
      grp_card_kosu = 1
      grp_No = cur_cardNo
      number_in_place.add((grp_No, grp_set))
    else:
      grp_No, grp_set = number_in_place.pop(insert_idx)
      grp_No = cur_cardNo
      grp_set.add(cur_cardNo)
      grp_card_kosu = len(grp_set)
      number_in_place.add((grp_No, grp_set))
  
  if grp_card_kosu >= K:
    NotNeed, cardSet = number_in_place.pop(number_in_place.bisect_left((cur_cardNo, set())))
    for s in cardSet:
      eat_turn_Arr[s] = n + 1

for n in range(1, N + 1):
  print(eat_turn_Arr[n])





"""
from sortedcontainers import SortedList
kazu_in_place = SortedList([])
kazu_in_place.add((14, set()))
kazu_in_place.add((3, set()))
print(kazu_in_place)
tmp = kazu_in_place.pop(0)
tmp_number, tmp_set = tmp
print("tmp", tmp_number, tmp_set)
tmp_set.add(8)
kazu_in_place.add((tmp_number, tmp_set))
print(kazu_in_place)
"""
