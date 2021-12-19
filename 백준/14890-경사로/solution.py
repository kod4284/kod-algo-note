from copy import deepcopy
readline = lambda: list(map(int, input().split()))

N, L = readline()
board = []

for i in range(N):
    board.append(readline())

pass_cnt = 0

def rotate():
    tmp = deepcopy(board)
    for i in range(N):
        for j in range(N):
            board[i][j] = tmp[j][i]

def go():
    global pass_cnt
    for i in range(N):
        cnt = 1
        jump_to = -1
        prev = board[i][0]
        passable = True
        for j in range(1, N):
            cur = board[i][j]
            if jump_to != -1:
                if j < jump_to:
                    continue
                jump_to = -1
            if prev == cur:
                cnt += 1
                prev = cur
            elif abs(prev - cur) != 1:
                passable = False
                break
            elif prev > cur:
                for k in range(L):
                    if j + k >= N or prev - 1 != board[i][j + k]:
                        passable = False
                        break
                else:
                    j += L
                    jump_to = j
                    cnt = 0
                    if j >= N:
                        break
                    prev = board[i][j - 1]
            elif prev < cur:
                if cnt >= L:
                    cnt = 1
                    prev = cur
                else:
                    passable = False
                    break
        if passable:
            pass_cnt += 1
go()
rotate()
go()
print(pass_cnt)


