from itertools import combinations, chain

readline = lambda: list(map(int, input().split()))

N, M, H = readline()
board = [[0] * (N + 2) for _ in range(H + 1)]

cases = []
lines = []
for _ in range(M):
    a, b = readline()
    board[a][b + 1] = 1
    lines.append((a, b))

def go(start, b):
    for i in range(1, H + 1):
        if b[i][start] == 0:
            if b[i][start + 1] == 0:
                continue
            else:
                start += 1
        else:
            start -= 1
    return start

def test(b):
    for i in range(2, N + 1):
        ans = go(i, b)
        if ans != i:
            break
    else:
        return True
    return False

def check_exceptions():
    for r in range(1, H + 1):
        for c in range(2, N + 1):
            if board[r][c] == 1 or board[r][c - 1] == 1 or board[r][c + 1]:
                continue
            cases.append((r, c))

def check_iter(iter):
    minv = int(1e9)
    for i in iter:
        for r, c in i:
            board[r][c] = 1
        if test(board):
            minv = min(minv, len(i))
        for r, c in i:
            board[r][c] = 0
    return minv if minv != int(1e9) else -1

check_exceptions()
three = combinations(cases, 3)
two = combinations(cases, 2)
one = combinations(cases, 1)

if test(board):
    print(0)
else:
    print(check_iter(chain(two, three, one)))
    