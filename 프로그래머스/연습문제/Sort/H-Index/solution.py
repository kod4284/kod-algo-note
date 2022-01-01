# 오름차순
# def solution(citations):
#   citations.sort()
#   for i in range(len(citations)):
#     if citations[i] >= len(citations) - i: # 나머지 논문 수
#       return len(citations) - i
#   return 0

# 내림차순
def solution(citations):
  citations.sort(reverse=True)
  for i in range(len(citations)):
    if citations[i] <= i:
      return i
  return len(citations)
# return
# 오름차순
# 1: 0 1 3 5 6: 3
# 2: 3 4 5 8 10: 4
# 3: 3 3 5 8 25: 3
# 내림차순
# 1: 6 5 3 1 0: 3
# 2: 10 8 5 4 3: 4
# 3: 25 8 5 3 3: 3
test_case_one = [3,0,6,1,5]
test_case_two = [10,8,5,4,3]
test_case_three = [25,8,5,3,3]
test_case_four = [25]

print(solution(test_case_one))
print(solution(test_case_two))
print(solution(test_case_three))
print(solution(test_case_four))