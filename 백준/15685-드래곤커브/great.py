read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

board = [[0] * 101 for _ in range(101)]

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def make_dg_curve_dir(d, g):
    path = [d]
    for _ in range(g):
        for r in reversed(path):
            path.append((r + 1) % 4)
    return path

def write_dg_curve(r, c, path):
    board[r][c] = 1
    for p in path:
        r += dr[p]
        c += dc[p]
        board[r][c] = 1

N = read()
for _ in range(N):
    x, y, d, g = readline()
    path = make_dg_curve_dir(d, g)
    write_dg_curve(y, x, path)

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
            cnt += 1

print(cnt)