from collections import defaultdict

readline = lambda: list(map(int, input().split()))

R, C, T = readline()
dusts = set()
purifier = []
board = [[] for _ in range(R)]
DIR = [(0, -1), (-1, 0), (0, 1), (1, 0)]

for i in range(R):
    for j, v in enumerate(readline()):
        board[i].append(v)
        if v == -1:
            purifier.append((i, j))
        elif v != 0:
            dusts.add((i, j))

def check_OOR(r, c):
    return r < 0 or c < 0 or r >= R or c >= C

for _ in range(T):
    dic = defaultdict(int)
    for i in range(R):
        for j in range(C):
            tmp = 0
            if (i, j) in purifier:
                continue
            for cr, cc in DIR:
                dr, dc = i + cr, j + cc
                if check_OOR(dr, dc) or (dr, dc) in purifier:
                    continue
                expended = board[i][j] // 5
                if expended == 0:
                    continue
                dic[(dr, dc)] += expended
                dusts.add((dr, dc))
                tmp += expended
            board[i][j] -= tmp
    for kr, kc in dic.keys():
        board[kr][kc] += dic[(kr, kc)]

    up_r, _ = purifier[0]
    for i in range(up_r - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    for i in range(C - 1):
        board[0][i] = board[0][i + 1]
    for i in range(up_r):
        board[i][C - 1] = board[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[up_r][i] = board[up_r][i - 1]
        if i == 2:
            board[up_r][1] = 0

    down_r, _  = purifier[1]
    for i in range(down_r + 1, R - 1):
        board[i][0] = board[i + 1][0]
    for i in range(C - 1):
        board[R - 1][i] = board[R - 1][i + 1]
    for i in range(R - 1, down_r, -1):
        board[i][C - 1] = board[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[down_r][i] = board[down_r][i - 1]
        if i == 2:
            board[down_r][1] = 0

sumv = 0
for i in range(R):
    for j in range(C):
        if (i, j) in purifier:
            continue
        if board[i][j] != -1:
            sumv += board[i][j]
print(sumv)