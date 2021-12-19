from collections import defaultdict
readline = lambda: list(map(int, input().split()))

N, M, K = readline()
A = [[-1]]
board = [-1] + [[-1] + [5] * N for _ in range(N)]
trees = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
tree_cords = set()
dead_trees = []
for _ in range(N):
    A.append([-1] + readline())
for _ in range(M):
    x, y, z = readline()
    trees[x][y].append(z)
    tree_cords.add((x, y))

DIR = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def check_OOR(r, c):
    return r < 1 or c < 1 or r > N or c > N

def print_arr(arr):
    for i in arr:
        print(i)
    print()

for _ in range(K):
    # 봄
    for r, c in tree_cords:
        removal_list = []
        for idx, age in enumerate(trees[r][c]):
            result = board[r][c] - age
            if result < 0:
                dead_trees.append((r, c, age))
                removal_list.append(age)
                continue
            board[r][c] = result
            trees[r][c][idx] += 1
        for age in removal_list:
            trees[r][c].remove(age)
        trees[r][c].sort()
    # 여름
    for r, c, age in dead_trees:
        board[r][c] += (age // 2)
    dead_trees = []
    # 가을
    new_set = set()
    for r, c in tree_cords:
        for age in trees[r][c]:
            if age % 5 == 0:
                for rr, cc in DIR:
                    dr, dc = r - rr, c - cc
                    if check_OOR(dr, dc):
                        continue
                    new_set.add((dr, dc))
                    trees[dr][dc].insert(0, 1)
    tree_cords = tree_cords.union(new_set)
    # 겨울
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            board[i][j] += A[i][j]


ans = 0
for r, c in tree_cords:
    ans += len(trees[r][c])
print(ans)
