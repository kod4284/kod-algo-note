def solution(array, commands):
  answer = []
  for i, j, k in commands:
    answer.append(sorted(array[i-1:j])[k-1])
  return answer

# return [5, 6, 3]
test_case = [[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]]
print(solution(test_case[0], test_case[1]))