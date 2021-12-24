read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

from collections import deque

def solution(progresses, speeds):
    queue = deque(progresses)
    speedQ = deque(speeds)
    sol = []
    while (True):
        if len(queue) == 0:
            break
        cnt = 0
        for idx in range(len(speedQ)):
            queue[idx] += speedQ[idx]
        while (True):
            if len(queue) == 0:
                break
            if queue[0] >= 100:
               queue.popleft()
               speedQ.popleft()
               cnt += 1 
            else:
                break
        if cnt > 0:
            sol.append(cnt)
    return sol

TC = read()
for i in range(1, TC + 1):
    progs = readline()
    speeds = readline()
    print("# {} {}".format(i, solution(progs, speeds)))
