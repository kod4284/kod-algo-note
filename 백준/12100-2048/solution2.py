from copy import deepcopy

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

global N
N = read()

board = []
global board2
board2 = [[0] * N for _ in range(N)]

for _ in range(N):
    board.append(readline())

def rotate():
    global N, board2
    temp = deepcopy(board2)
    for i in range(N):
        for j in range(N):
            board2[i][j] = temp[N - 1 - j][i]

def tilt(dir):
    global N, board2
    for _ in range(dir):
        rotate()
    for i in range(N):
        merged = [0 for _ in range(N)]
        idx = 0
        for j in range(N):
            if board2[i][j] == 0:
                continue
            elif merged[idx] == 0:
                merged[idx] = board2[i][j]
            elif merged[idx] == board2[i][j]:
                merged[idx] *= 2
                idx += 1
            else:
                idx += 1
                merged[idx] = board2[i][j]
        for j in range(N):
            board2[i][j] = merged[j]

max_value = 0
for i in range(1<<(2 * 5)):
    brute = i
    board2 = deepcopy(board)
    for _ in range(5):
        remain = brute % 4
        brute //= 4
        tilt(remain)
    for r in board2:
        max_value = max(max(r), max_value)

print(max_value)
