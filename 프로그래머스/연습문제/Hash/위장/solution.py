from collections import defaultdict

def solution(clothes):
  type_dict = defaultdict(int)
  for cloth in clothes:
    type_dict[cloth[1]] += 1
  result = 1
  for value in type_dict.values():
    result *= (value + 1) # 장비를 안 입는 경우 때문에 +1
  return result - 1 # 장비를 모두 안 입을 경우는 없으므로 -1
input_one = [
  ["yellowhat", "headgear"],
  ["bluesunglasses", "eyewear"],
  ["green_turban", "headgear"]
]

input_two = [
  ["crowmask", "face"],
  ["bluesunglasses", "face"],
  ["smoky_makeup", "face"]
]

print("#{} {}".format(1, solution(input_one)))
print("#{} {}".format(2, solution(input_two)))
