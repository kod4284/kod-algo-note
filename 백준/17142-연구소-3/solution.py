from itertools import combinations
from collections import deque

readline = lambda: list(map(int, input().split()))
N, M = readline()
board = []
virus = []
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
empty_cnt = 0
for i in range(N):
    block = readline()
    for j, v in enumerate(block):
        if v == 0:
            empty_cnt += 1
        if v == 2:
            virus.append((i, j))
    board.append(block)
def print_arr(arr):
    for i in arr:
        print(i)
    print()

cases = combinations(virus, M) 
def check_OOR(r, c):
    return r < 0 or c < 0 or r >= N or c >= N

def bfs():
    times = []
    for case in cases:
        visited = [[-1] * N for _ in range(N)]
        queue = deque(case)
        cnt = 0
        maxv = 0
        stop = False
        for r, c in case:
            visited[r][c] = 0
        while queue:
            vr, vc = queue.popleft()
            for tr, tc in DIR:
                dr, dc = vr + tr, vc + tc
                if check_OOR(dr, dc) or visited[dr][dc] >= 0 or board[dr][dc] == 1:
                    continue
                if visited[dr][dc] == -1:
                    if board[dr][dc] == 0:
                        cnt += 1
                        visited[dr][dc] = visited[vr][vc] + 1
                        maxv = max(maxv, visited[dr][dc])
                    elif board[dr][dc] == 2:
                        visited[dr][dc] = visited[vr][vc] + 1
                    if cnt == empty_cnt:
                        times.append(maxv)
                        stop = True
                        break
                queue.append((dr, dc))
            if stop:
                stop = False
                break
    return min(times) if times else -1

if empty_cnt == 0:
    print(0)
else:
    print(bfs())