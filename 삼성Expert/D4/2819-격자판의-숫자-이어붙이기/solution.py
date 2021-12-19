readline = lambda: list(input().split())

DR = [0, 1, 0, -1]
DC = [1, 0, -1, 0]

global board

def dfs(x, y, n, dir, path, str_set):
    global board
    if n <= 0:
        str_set.add(path)
        return path
    x += DR[dir]
    y += DC[dir]
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return
    path += board[x][y]
    for i in range(4):
        dfs(x, y, n - 1, i, path, str_set)

def solve():
    global board
    board = []
    for _ in range(4):
        board.append(readline())
    str_set = set()
    for i in range(4):
        for j in range(4):
            for k in range(4):
                dfs(i, j, 7, k, "", str_set)
    return len(str_set)

TC = int(input())
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))
