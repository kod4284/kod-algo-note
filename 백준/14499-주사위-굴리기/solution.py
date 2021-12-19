readline = lambda: list(map(int, input().split()))

N, M, r, c, K = readline()
board = []
for i in range(N):
    board.append(readline())
dice = [[0] * 3 for _ in range(4)]
DIR = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

def check_OOR(r, c):
    return r < 0 or c < 0 or r >= N or c >= M

def move_dice(d):
    global r, c
    if d == 1:
        c += 1
        tmp = dice[1][0]
        for i in range(2):
            dice[1][i] = dice[1][i + 1]
        dice[1][2] = dice[3][1]
        dice[3][1] = tmp
    elif d == 2:
        c += -1
        tmp = dice[1][2]
        for i in range(1, -1, -1):
            dice[1][i + 1] = dice[1][i]
        dice[1][0] = dice[3][1]
        dice[3][1] = tmp
    elif d == 3:
        r += -1
        tmp = dice[3][1]
        for i in range(2, -1, -1):
            dice[i + 1][1] = dice[i][1]
        dice[0][1] = tmp
    elif d == 4:
        r += 1
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i + 1][1]
        dice[3][1] = tmp

def copy_number():
    if board[r][c] == 0:
        board[r][c] = dice[1][1]
    else:
        dice[1][1] = board[r][c]
        board[r][c] = 0

copy_number()
for i in readline():
    fr, fc = DIR[i]
    if check_OOR(r + fr, c + fc):
        continue
    move_dice(i)
    copy_number()
    print(dice[3][1])