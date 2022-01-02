def solution(answers):
  method_one = [1,2,3,4,5]
  method_two = [2,1,2,3,2,4,2,5]
  method_three = [3,3,1,1,2,2,4,4,5,5]
  scores = [0,0,0]
  for idx, a in enumerate(answers):
    if method_one[idx % len(method_one)] == a:
      scores[0] += 1
    if method_two[idx % len(method_two)] == a:
      scores[1] += 1
    if method_three[idx % len(method_three)] == a:
      scores[2] += 1

  max_value = max(scores)
  answer = []
  for idx, score in enumerate(scores):
    if max_value == score:
      answer.append(idx + 1)
  return answer

# return [1] [1,2,3]
test_case_one = [1,2,3,4,5]
test_case_two = [1,3,2,4,2]

print(solution(test_case_one))
print(solution(test_case_two))