from collections import deque

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N = read()

board = []
fishes = []
shark_cnt = 0
distance = [[0] * N for _ in range(N)]
for i in range(N):
    tmp = readline()
    board.append(tmp)
    for j, v in enumerate(tmp):
        if v == 9:
            shark = [i, j, 2]
            board[i][j] = 0
        elif v != 0:
            fishes.append((i, j, v))

def check_OOR(r, c):
    return r < 0 or c < 0 or r >= N or c >= N

def bfs():
    global distance
    r, c, _ = shark
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    queue = deque([(r, c)])
    visited[r][c] = 1
    while queue:
        pr, pc = queue.popleft()
        for cr, cc in DIR:
            dr, dc = pr + cr, pc + cc
            if check_OOR(dr, dc):
                continue
            if board[dr][dc] > shark[2] or visited[dr][dc]:
                continue
            visited[dr][dc] = 1
            distance[dr][dc] = distance[pr][pc] + 1
            if 1 <= board[dr][dc] <= 6 and board[dr][dc] < shark[2]:
                continue
            queue.append((dr, dc))
def eat_fish(r, c):
    global shark_cnt, board
    shark[0], shark[1] = r, c
    shark_cnt += 1
    if shark_cnt == shark[2]:
        shark[2] += 1
        shark_cnt = 0
    fishes.remove((r, c, board[r][c]))
    board[r][c] = 0

def eat_closest_fish():
    ans = []
    for r, c, f_size in fishes:
        dis = distance[r][c]
        if dis > 0 and board[r][c] < shark[2]:
            ans.append((dis, r, c))
    if len(ans) == 0:
        return False
    mins = min(ans)[0]
    min_vs = list(filter(lambda x: x[0] == mins, ans))
    min_vs = list(filter(lambda x: x[1] == min(min_vs, key=lambda x: x[1])[1], min_vs))
    min_vs = list(filter(lambda x: x[2] == min(min_vs, key=lambda x: x[2])[2], min_vs))
    d, r, c = min_vs[0]
    eat_fish(r, c)
    return d

cnt = 0
while True:
    bfs()
    d = eat_closest_fish()
    if not d:
        break
    cnt += d

print(cnt)
