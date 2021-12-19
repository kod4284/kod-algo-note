from collections import defaultdict, deque

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

APPLE = 1
rotates = defaultdict(str)

N = read()
K = read()
board = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = readline()
    board[r][c] = APPLE
L = read()
for _ in range(L):
    r, c = input().split()
    r = int(r)
    rotates[r] = c

python = deque([(1, 1)])
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def check_hit_wall(r, c):
    return r < 1 or c < 1 or r > N or c > N

def solution():
    cur_dir = 0
    time = 0
    while True:
        dr, dc = python[0][0] + DIR[cur_dir][0], python[0][1] + DIR[cur_dir][1]
        if check_hit_wall(dr, dc) or (len(python) > 1 and (dr, dc) in list(python)[1:]):
            return time + 1
        if not check_hit_wall(dr, dc) and board[dr][dc] == APPLE:
            python.appendleft((dr, dc))
            board[dr][dc] = 0
        else:
            v = python.pop()
            python.appendleft((dr, dc))
        time += 1
        if rotates[time] == "D":
            cur_dir = (cur_dir + 1) % 4
        elif rotates[time] == "L":
            cur_dir = (cur_dir - 1) % 4

print(solution())