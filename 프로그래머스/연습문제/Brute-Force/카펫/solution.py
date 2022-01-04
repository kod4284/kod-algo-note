def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for h, v in get_all_divsor_pairs(total):
      if brown == get_brown(h, v):
        return [v, h]

def get_all_divsor_pairs(x):
  temp_list = []
  pairs = []
  for i in range(1, x + 1):
    if x % i == 0:
      temp_list.append(i)
  for i in range(len(temp_list) // 2 + 1):
    pairs.append([temp_list[i], temp_list[len(temp_list) - i - 1]])
  return pairs

def get_brown(b, y):
  return 2 * b + 2 * y - 4


test_cases = [
  [10, 2],
  [8, 1],
  [24, 24],
]

for b, y in test_cases:
  print(solution(b, y))