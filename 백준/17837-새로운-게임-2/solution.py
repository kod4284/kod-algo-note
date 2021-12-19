from collections import defaultdict
readline = lambda: list(map(int, input().split()))

N, K = readline()
board = []
mals = defaultdict(list)
cords_stack = defaultdict(list)
DIR = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]
op_dir = { 1:2, 2:1, 3:4, 4:3 }
for _ in range(N):
    board.append(readline())

for i in range(1, K + 1):
    r, c, d = readline()
    mals[i] = [r - 1, c - 1, d]
    cords_stack[(r - 1, c - 1)].append(i)

def check_OOR(r, c):
    return r < 0 or c < 0 or r >= N or c >= N

def move_mal(r, c, dr, dc, stacks):
    for i in stacks:
        mals[i][0], mals[i][1] = dr, dc
        cords_stack[(dr, dc)].append(i)
        cords_stack[(r, c)].remove(i)

def check_all_in_one():
    return True if list(filter(lambda x: len(x) >= 4, cords_stack.values())) else False

if check_all_in_one():
    print(1)
else:
    stop = False
    for i in range(1, 1001):
        if stop:
            break
        for j in range(1, K + 1):
            r, c, d = mals[j]
            stacks = cords_stack[(r, c)][cords_stack[(r, c)].index(j):]
            dr, dc = DIR[d][0] + r, DIR[d][1] + c
            if check_OOR(dr, dc) or board[dr][dc] == 2:
                d = op_dir[d]
                mals[j][2] = d
                dr, dc = DIR[d][0] + r, DIR[d][1] + c
                if check_OOR(dr, dc) or board[dr][dc] == 2:
                    continue
            if board[dr][dc] == 0:
                move_mal(r, c, dr, dc, stacks)
            elif board[dr][dc] == 1:
                move_mal(r, c, dr, dc, reversed(stacks))
            if check_all_in_one():
                print(i)
                stop = True
                break
    else:
        print(-1)