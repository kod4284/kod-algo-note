from collections import deque

read = lambda: int(input())
INF = int(1e9)

DR = [0, 1, 0, -1]
DC = [1, 0, -1, 0]

global N

def check_OOR(r, c):
    global N
    return r < 0 or r >= N or c < 0 or c >= N

def bfs(x, memo, board):
    queue = deque([x])
    memo[x[0]][x[1]] = 0
    while queue:
        v = queue.popleft()
        temp = []
        for i in range(4):
            dr = v[0] + DR[i]
            dc = v[1] + DC[i]
            if not check_OOR(dr, dc):
                if memo[dr][dc] > memo[v[0]][v[1]] + board[dr][dc]:
                    memo[dr][dc] = memo[v[0]][v[1]] + board[dr][dc]
                    queue.append((dr, dc))

def solve():
    global N
    N = read()
    # board 초기화
    board = [[] for _ in range(N)]
    for i in range(N):
        for l in input():
            board[i].append(int(l))
    memo = [[INF] * N for _ in range(N)]
    # bfs
    bfs((0, 0), memo, board)
    return memo[N - 1][N - 1]
    
TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))