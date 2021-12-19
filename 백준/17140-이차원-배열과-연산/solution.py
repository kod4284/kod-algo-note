from collections import defaultdict
readline = lambda: list(map(int, input().split()))

r, c, k = readline()
board = []
for _ in range(3):
    board.append(readline())

def do_R():
    for idx, i in enumerate(board):
        dic = defaultdict(int)
        new_list = []
        for j in i:
            if j == 0:
                continue
            dic[j] += 1
        kv = list(sorted(sorted(dic.items()), key= lambda x: x[1]))
        for k, v in kv:
            new_list.append(k)
            new_list.append(v)
        if len(new_list) >= 100:
            new_list = new_list[:100]
        board[idx] = new_list
    maxv = 0
    for i in board:
        maxv = max(len(i), maxv)
    for idx, v in enumerate(board):
        if len(v) < maxv:
            for _ in range(maxv - len(v)):
                board[idx].append(0)


def do_C():
    for i in range(len(board[0])):
        dic = defaultdict(int)
        new_list = []
        for j in range(len(board)):
            if board[j][i] == 0:
                continue
            dic[board[j][i]] += 1
        kv = list(sorted(sorted(dic.items()), key= lambda x: x[1]))
        for k, v in kv:
            new_list.append(k)
            new_list.append(v)
        if len(new_list) >= 100:
            new_list = new_list[:100]
        for j, v in enumerate(new_list):
            if j >= len(board):
                new_block = [0] * len(board[0])
                new_block[i] = v
                board.append(new_block)
            else:
                board[j][i] = v
        if len(new_list) < len(board):
            for j in range(len(new_list), len(board)):
                board[j][i] = 0


def check_OOR(r, c):
    return r > len(board) or c > len(board[0])

for t in range(0, 101):
    if not check_OOR(r, c) and board[r - 1][c - 1] == k:
        print(t)
        break
    elif len(board) >= len(board[0]):
        do_R()
    elif len(board) < len(board[0]):
        do_C()
else:
    print(-1)