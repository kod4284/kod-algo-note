from itertools import permutations

def solution(numbers):
  number_list = list(numbers)
  check_list = []
  dup_list = {}
  for i in range(1, len(number_list)+ 1):
    check_list.append(list(permutations(number_list, i)))
  cnt = 0
  for nums in check_list:
    for num in nums:
      joined = int(''.join(num))
      if dup_list.get(joined):
        continue
      else:
        dup_list[joined] = True
      if check_prime(joined):
        cnt += 1
  return cnt

def check_prime(x):
  if x == 0 or x == 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

# return 3, 2
test_case_one = "17"
test_case_two = "011"

print(solution(test_case_one))
print(solution(test_case_two))