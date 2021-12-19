from copy import deepcopy
from collections import deque
from itertools import combinations

readline = lambda: list(map(int, input().split()))

N, M = readline()
virus = []
empty = []
board = [[] for _ in range(N)]

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def check_OOR(r, c):
    return r < 0 or c < 0 or r >= N or c >= M


def bfs(start, b):
    cnt = 0
    queue = deque([start])
    b[start[0]][start[1]] = 2
    while queue:
        r, c = queue.popleft()
        for rr, cc in DIR:
            dr, dc = r + rr, c + cc
            if check_OOR(dr, dc) or b[dr][dc] != 0:
                continue
            b[dr][dc] = 2
            queue.append((dr, dc))
            cnt += 1
    return cnt


for i in range(N):
    for j, value in enumerate(readline()):
        if value == 0:
            empty.append((i, j))
        elif value == 2:
            virus.append((i, j))
        board[i].append(value)

all_cases = combinations(empty, 3)

ans = []
for c in all_cases:
    tmp_board = deepcopy(board)
    cnt = len(empty)
    for r, c in c:
        tmp_board[r][c] = 1
        cnt -= 1
    for r, c in virus:
        cnt -= bfs((r, c), tmp_board)
    ans.append(cnt)
print(max(ans))