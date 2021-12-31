def solution(numbers):
  str_numbers = list(map(str, numbers))
  str_numbers.sort(key=lambda x: x*3, reverse=True)
  return str(int(''.join(str_numbers)))

test_case_one = [6,10,2]
test_case_two = [3,30,34,5,9]
test_case_three = [0,0,0,0,0]

print(solution(test_case_one))
print(solution(test_case_two))
print(solution(test_case_three))