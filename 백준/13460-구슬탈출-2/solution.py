import heapq

readline = lambda: list(map(int, input().split()))

N, M = readline()
board = []

RED = []
BLUE = []
HOLE = ()

DIR = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]

for i in range(N):
    temp = []
    for j, st in enumerate(input()):
        if st == "R":
            RED = [i, j]
            temp.append(".")
        elif st == "B":
            BLUE = [i, j]
            temp.append(".")
        elif st == "O":
            HOLE = (i, j)
            temp.append(st)
        else:
            temp.append(st)
    board.append(temp)

goal = []

def dfs(cnt):
    global board
    if cnt > 10:
        return
    for r, c in DIR:
        prr, prc = RED[0], RED[1]
        pbr, pbc = BLUE[0], BLUE[1]
        rb = set()
        for _ in range(max(M, N)):
            if board[RED[0] + r][RED[1] + c] == "." and not (RED[0] + r == BLUE[0] and RED[1] + c == BLUE[1]):
                RED[0] += r
                RED[1] += c
            if board[RED[0] + r][RED[1] + c] == "O":
                RED[0], RED[1] = 0, 0
                rb.add((cnt, "R"))
            if board[BLUE[0] + r][BLUE[1] + c] == "." and not (RED[0] == BLUE[0] + r and RED[1] == BLUE[1] + c):
                BLUE[0] += r
                BLUE[1] += c
            if board[BLUE[0] + r][BLUE[1] + c] == "O":
                BLUE[0], BLUE[1] = 0, 0
                rb.add((cnt, "B"))
        if len(rb) == 1 and RED[0] == 0 and RED[1] == 0 and not (BLUE[0] == 0 and BLUE[1] == 0):
            value = rb.pop()
            if value[1] == "R":
                heapq.heappush(goal, value[0])
        dfs(cnt + 1)
        RED[0], RED[1] = prr, prc
        BLUE[0], BLUE[1] = pbr, pbc
    if len(goal) > 0:
        return

dfs(1)
if len(goal) == 0:
    print(-1)
else:
    print(heapq.heappop(goal))