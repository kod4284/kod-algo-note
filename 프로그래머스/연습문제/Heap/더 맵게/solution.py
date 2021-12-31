import heapq

def solution(scoville, K):
  answer = 0
  heapq.heapify(scoville)
  cnt = 0
  
  while scoville[0] < K:
    if len(scoville) < 2:
      return -1
    cnt += 1
    first = heapq.heappop(scoville)
    second = heapq.heappop(scoville)
    new_s = first + second * 2
    heapq.heappush(scoville, new_s)
  return cnt

test_values = [[1,2,3,9,10,12], 7]
test_values = [[1,2], 7]
print(solution(test_values[0], test_values[1]))