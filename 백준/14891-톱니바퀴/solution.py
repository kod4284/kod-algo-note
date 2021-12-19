from collections import deque
readline = lambda: list(map(int, input().split()))

board = [[] for _ in range(4)]
for i in range(4):
    st = input()
    for j in st:
        board[i].append(int(j))

order = []
K = int(input())
for i in range(K):
    num, di = readline()
    order.append((num, di))

def check_left_gear(idx, di):
    q =  deque()
    while idx > 0:
        if board[idx][6] != board[idx - 1][2]:
            di = -di
            q.append((idx - 1, di))
            idx -= 1
        else:
            break
    while q:
        i, d = q.popleft()
        rotate(board[i], d)

def check_right_gear(idx, di):
    q =  deque()
    while idx < 3:
        if board[idx][2] != board[idx + 1][6]:
            di = -di
            q.append((idx + 1, di))
            idx += 1
        else:
            break
    while q:
        i, d = q.popleft()
        rotate(board[i], d)

def rotate(gear, di):
    if di == 1:
        tmp = gear[len(gear) - 1]
        for i in range(len(gear) - 1, 0, -1):
            gear[i] = gear[i - 1]
        gear[0] = tmp
    else:
        tmp = gear[0]
        for i in range(len(gear) - 1):
            gear[i] = gear[i + 1]
        gear[len(gear) - 1] = tmp
        
def get_score():
    score = 0
    cnt = 1
    for i in range(4):
        if board[i][0] == 1:
            score += cnt
        cnt *= 2
    return score

def print_board():
    for i in board:
        print(i)
    print()

for g, di in order:
    check_left_gear(g - 1, di)
    check_right_gear(g - 1, di)
    rotate(board[g - 1], di)

print(get_score())