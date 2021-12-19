from collections import deque
readline = lambda: list(map(int, input().split()))

N, M, T = readline()
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
board = [-1]
for _ in range(N):
    board.append(readline())

def check_OOR(r, c):
    return r < 1 or c < 0 or r > N or c >= M

def bfs(r, c):
    target = board[r][c]
    if target == -1:
        return False
    queue = deque([(r, c)])
    visited = [[0] * M for _ in range(N + 1)]
    visited[r][c] = 1
    cords = set()
    cords.add((r, c))
    erased = False
    while queue:
        vr, vc = queue.popleft()
        for tr, tc in DIR:
            dr, dc = vr + tr, (vc + tc) % M
            if check_OOR(dr, dc) or visited[dr][dc] or board[dr][dc] != target:
                continue
            visited[dr][dc] = 1
            cords.add((dr, dc))
            erased = True
            queue.append((dr, dc))
    if len(cords) >= 2:
        for cr, cc in cords:
            board[cr][cc] = -1
    return erased

def rotate(x, d, k):
    for i in range(1, N + 1):
        if i % x == 0:
            block = [0] * M
            for j in range(M):
                if d == 0:
                    block[(j + k) % M] = board[i][j]
                else:
                    block[(j - k) % M] = board[i][j]
            board[i] = block

def get_sum_and_avg():
    sumv = 0
    cnt = 0
    for i in range(1, N + 1):
        for j in range(M):
            if board[i][j] != -1:
                cnt += 1
                sumv += board[i][j]
    avg = (sumv / cnt) if cnt > 0 else 0
    return sumv, avg

def adjust(avg):
    for i in range(1, N + 1):
        for j in range(M):
            if board[i][j] != -1:
                if board[i][j] > avg:
                    board[i][j] -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1

for _ in range(T):
    x, d, k = readline()
    rotate(x, d, k)
    erased = False
    for i in range(1, N + 1):
        for j in range(M):
            if bfs(i, j):
                erased = True
    if not erased:
        _, avg = get_sum_and_avg()
        adjust(avg)

sumv, _ = get_sum_and_avg()
print(sumv)