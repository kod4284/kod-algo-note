from collections import deque

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

board = [[-1]]
temp = [[-1] * 150 for _ in range(150)]

DIR = [(-1, 0), (-1, -1), (0, -1), (1, 0), (1, 1), (0, 1)]

def check_OOR(r, c):
    return r < 0 or r >= 150 or c < 0 or c > 150

def bfs(a, b):
    dis = [0] * 12000
    visited = [0] * 12000
    visited[b] = 2
    if visited[a] == 2:
        return 0

    queue = deque([a])
    visited[a] = 1
    while queue:
        v = queue.popleft()
        for i in board[v]:
            if visited[i] == 2:
                return dis[v] + 1
            if visited[i]:
                continue
            queue.append(i)
            dis[i] = dis[v] + 1
            visited[i] = 1
def init():
    cnt = 0
    for i in range(150):
        for j in range(1, i):
            cnt += 1
            temp[i][j] = cnt

    for i in range(150):
        for j in range(1, i):
            arr = []
            for r, c in DIR:
                if not check_OOR(i + r, j + c) and temp[i + r][j + c] != -1:
                    arr.append(temp[i + r][j + c])
            board.append(arr)

def solve():
    a, b = readline()
    return bfs(a, b)

TC = read()
init()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))