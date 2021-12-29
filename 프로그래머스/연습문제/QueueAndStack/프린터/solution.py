from collections import deque

def solution(priorities, location):
  queue = deque(enumerate(priorities))
  target = queue[location][0]
  cnt = 0
  while (True):
    if queue:
      first = queue.popleft()
      found = [e for e in list(queue) if (e[1] > first[1])]
      
      if len(found) > 0:
        queue.append(first)
      else:
        cnt += 1
        if target == first[0]:
          return cnt
      
      

priorities_one = [2, 1, 3, 2]
location_one = 2
priorities_two = [1, 1, 9, 1, 1, 1]	
location_two = 0

print("#1 {}".format(solution(priorities_one, location_one)))
print("#2 {}".format(solution(priorities_two, location_two)))
