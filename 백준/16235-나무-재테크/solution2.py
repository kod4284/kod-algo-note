from collections import defaultdict

readline = lambda: list(map(int, input().split()))

N, M, K = readline()
A = [[-1]]
board = [-1] + [[-1] + [5] * N for _ in range(N)]
trees = [[defaultdict(int) for _ in range(N + 1)] for _ in range(N + 1)]
tree_cords = set()
for _ in range(N):
    A.append([-1] + readline())
for _ in range(M):
    x, y, z = readline()
    trees[x][y][z] += 1
    tree_cords.add((x, y))
DIR = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def check_OOR(r, c):
    return r < 1 or c < 1 or r > N or c > N

def print_arr(arr):
    for i in arr:
        print(i)
    print()

for _ in range(K):
    # 봄, 여름
    for r, c in tree_cords:
        tmp = defaultdict(int)
        die = 0
        for age in sorted(trees[r][c].keys()):
            if age * trees[r][c][age] <= board[r][c]:
                tmp[age + 1] += trees[r][c][age]
                board[r][c] -= age * trees[r][c][age]
            else:
                cnt = board[r][c] // age
                if cnt:
                    tmp[age + 1] += cnt
                die += (age // 2) * (trees[r][c][age] - cnt)
                board[r][c] -= (age * cnt)
        trees[r][c] = tmp
        board[r][c] += die

    # 가을
    new_set = set()
    for r, c in tree_cords:
        for age in sorted(trees[r][c].keys()):
            if age % 5 == 0:
                for _ in range(trees[r][c][age]):
                    for rr, cc in DIR:
                        dr, dc = r - rr, c - cc
                        if check_OOR(dr, dc):
                            continue
                        new_set.add((dr, dc))
                        trees[dr][dc][1] += 1
    tree_cords = tree_cords.union(new_set)
    # 겨울
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            board[i][j] += A[i][j]
ans = 0
for r, c in tree_cords:
    for age in trees[r][c].keys():
        ans += trees[r][c][age]
print(ans)
