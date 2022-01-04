from itertools import permutations
import math

# 에라토스테네스의 체
n = 10000000
primes = [True] * n
primes[0] = False
primes[1] = False
for i in range(2, int(math.sqrt(n)) + 1):
  if primes[i] == True:
    j = 2
    while i * j < n:
      primes[i * j] = False
      j += 1

def check_prime(x):
  return primes[x]

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




# return 3, 2
test_case_one = "17"
test_case_two = "011"

print(solution(test_case_one))
print(solution(test_case_two))

