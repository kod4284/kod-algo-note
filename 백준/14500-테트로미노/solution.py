from copy import deepcopy

readline = lambda: list(map(int, input().split()))

N, M = readline()
board = []
initial_tetros = [
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [1, 0], [1, 1], [0, 1]],
    [[0, 1], [1, 1], [2, 1], [2, 0]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [1, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 1]]
]

all_tetros = []
max_value = 0

for i in range(N):
    board.append(readline())    

def rotate(arr):
    max_value = max(arr, key=lambda x: x[0])[0]
    tmp = []
    for r, c in arr:
        tmp.append([c, max_value - r])
    return tmp

def check_OOR(r, c):
    return r < 0 or c < 0 or r >= N or c >= M

def move_right(tetro):
    global max_value
    sum_value = 0
    move = True
    for i, value in enumerate(tetro):
        r, c = value
        sum_value += board[r][c]
        if check_OOR(r, c + 1):
            move = False
            continue
        tetro[i][0], tetro[i][1] = r, c + 1
    max_value = max(max_value, sum_value)
    return move

def move_down(tetro):
    global max_value
    sum_value = 0
    move = True
    for i, value in enumerate(tetro):
        r, c = value
        sum_value += board[r][c]
        if check_OOR(r + 1, c):
            move = False
            continue
        tetro[i][0], tetro[i][1] = r + 1, c
    max_value = max(max_value, sum_value)
    return move

for i in initial_tetros:
    all_tetros.append(deepcopy(i))
    for _ in range(3):
        all_tetros.append(rotate(all_tetros[len(all_tetros) - 1])) 

for i in range(len(all_tetros)):
    for _ in range(N):
        tmp = deepcopy(all_tetros[i])
        for _ in range(M):
            if not move_right(all_tetros[i]):
                break
        all_tetros[i] = tmp
        if not move_down(all_tetros[i]):
            break

print(max_value)