from collections import deque

def solution(bridge_length, weight, truck_weights):
  bridge_queue = deque()
  ready_queue = deque(truck_weights)
  time = 0
  while True:
    if not bridge_queue and not ready_queue:
      return time
    time += 1
    if bridge_queue:
      for v in bridge_queue:
        v[1] -= 1
      if bridge_queue[0][1] == -1:
        bridge_queue.popleft()
    
    if ready_queue:
      value = ready_queue.popleft()
      if len(bridge_queue) < bridge_length and (sum(map(lambda x: x[0], bridge_queue)) + value) <= weight:
        bridge_queue.append([value, bridge_length - 1])
      else:
        ready_queue.appendleft(value)

# bridge_length, weight, truck_weights
# return: 8, 101, 110
test_cases = [
  [2, 10, [7,4,5,6]],
  [100, 100, [10]],
  [100, 100, [10,10,10,10,10,10,10,10,10,10]]
]

for i, v in enumerate(test_cases):
  (bl, w, tw) = v
  print("#{} {}".format(i + 1, solution(bl, w, tw)))