readline = lambda: list(map(int, input().split()))

N, M = readline()
r, c, d = readline()
board = []
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0

for _ in range(N):
    board.append(readline())

def dfs():
    global d, cnt, r, c
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1

    for i in range(4):
        ttr, ttc = DIR[i]
        if board[r + ttr][c + ttc] == 0:
            break
    else:
        back = DIR[(d + 2) % 4]
        if board[r + back[0]][c + back[1]] == 1:
            return
        else:
            r += back[0]
            c += back[1]
            return dfs()
    left = (d - 1) % 4
    tr, tc = DIR[left]
    dr, dc = r + tr, c + tc

    if board[dr][dc] == 0:
        d = left
        r, c = dr, dc
    elif board[dr][dc] != 0:
        d = left
    dfs()

dfs()
print(cnt)
