from collections import defaultdict
readline = lambda: list(map(int, input().split()))

N = int(input())
board = []
g_board = [[0] * N for _ in range(N)]

for _ in range(N):
    board.append(readline())

def make_one(r, c, d1, d2):
    dic = {}
    for i in range(d1 + 1):
        dic[r + i] = c - i
    
    for i in range(r):
        dic[i] = c + 1
    
    for i in range(r + d1):
        for j in range(dic[i]):
            g_board[i][j] = 1

def make_two(r, c, d1, d2):
    dic = {}
    for i in range(r):
        dic[i] = c
    
    for i in range(d2 + 1):
        dic[r + i] = c + i
    for i in range(r + d2 + 1):
        for j in range(dic[i] + 1, N):
            g_board[i][j] = 2

def make_three(r, c, d1, d2):
    dic = {}
    for i in range(r + d1 + d2 + 1, N):
        dic[i] = c + (d2 - d1)
    
    for i in range(d2 + 1):
        dic[r + d1 + i] = c - d1 + i
    
    for i in range(r + d1, N):
        for j in range(dic[i]):
            g_board[i][j] = 3

def make_four(r, c, d1, d2):
    dic = {}
    for i in range(r + d1 + d2 + 1, N):
        dic[i] = c + (d2 - d1) - 1
    
    for i in range(d1 + 1):
        dic[r + d2 + i] = c + d2 - i
    
    for i in range(r + d2 + 1, N):
        for j in range(dic[i] + 1, N):
            g_board[i][j] = 4

def count():
    dic = defaultdict(int)
    for i, gv in enumerate(g_board):
        for j, v in enumerate(gv):
            dic[v] += board[i][j]
    v = dic.values()
    if len(v) < 5:
        return False
    maxv = max(v)
    minv = min(v)
    return maxv - minv
            

def check_IN_R(r, c, d1, d2):
    return 1 <= r + 1 < r + 1 + d1 + d2 <= N and 1 <= c + 1 - d1 < c + 1 < c + 1 + d2 <= N

ans = []
for r in range(N):
    for c in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if not check_IN_R(r, c, d1, d2):
                    continue
                g_board = [[0] * N for _ in range(N)]
                make_one(r, c, d1, d2)
                make_two(r, c, d1, d2)
                make_three(r, c, d1, d2)
                make_four(r, c, d1, d2)
                cnt = count()
                if cnt == False:
                    continue
                ans.append(cnt)
print(min(ans))