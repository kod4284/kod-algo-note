from collections import deque
readline = lambda: list(map(int, input().split()))

N, L, R = readline()
board = []
for _ in range(N):
    board.append(readline())

def check_OOR(r, c):
    return r < 0 or c < 0 or r >= N or c >= N

def init():
    global verti, horiz, visited
    verti = [[1] * N for _ in range(N)]
    horiz = [[1] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not check_OOR(i, j + 1):
                sub = abs(board[i][j] - board[i][j + 1])
                if sub >= L and sub <= R:
                    verti[i][j] = 0

            if not check_OOR(i + 1, j):
                sub = abs(board[i][j] - board[i + 1][j])
                if sub >= L and sub <= R:
                    horiz[i][j] = 0

def print_board(b):
    for i in b:
        print(i)
    print()

def bfs(start, mark):
    global visited
    if visited[start[0]][start[1]] != 0:
        return 0
    cnt = 1
    sumv = board[start[0]][start[1]]
    q = deque([start])
    visited[start[0]][start[1]] = mark
    while q:
        r, c = q.popleft()
        if not check_OOR(r, c - 1):
            if visited[r][c - 1] == 0 and verti[r][c - 1] == 0:
                visited[r][c - 1] = mark
                cnt += 1
                sumv += board[r][c - 1]
                q.append((r, c - 1))
        if not check_OOR(r, c + 1):
            if visited[r][c + 1] == 0 and verti[r][c] == 0:
                visited[r][c + 1] = mark
                cnt += 1
                sumv += board[r][c + 1]
                q.append((r, c + 1))
        if not check_OOR(r + 1, c):
            if visited[r + 1][c] == 0 and horiz[r][c] == 0:
                visited[r + 1][c] = mark
                cnt += 1
                sumv += board[r + 1][c]
                q.append((r + 1, c))
        if not check_OOR(r - 1, c):
            if visited[r - 1][c] == 0 and horiz[r - 1][c] == 0:
                visited[r - 1][c] = mark
                cnt += 1
                sumv += board[r - 1][c]
                q.append((r - 1, c))
    return 0 if cnt == 1 else sumv // cnt

def fill(a, b):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == a:
                board[i][j] = b


def solve():
    move = 0
    m = 0
    for i in range(N):
        for j in range(N):
            m += 1
            avg = bfs((i, j), m)
            if avg > 0:
                fill(m, avg)
                move += 1
    return move

net_cnt = 0
while True:
    init()
    m = solve()
    if m > 0:
        net_cnt += 1
        continue
    else:
        break
print(net_cnt)
                