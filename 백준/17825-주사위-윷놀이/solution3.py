from copy import deepcopy
from collections import defaultdict
readline = lambda: list(map(int, input().split()))

class node:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

def check_OOR(r, c):
    return c >= len(board[r])

def dfs(i, cnt):
    global mals, ans
    if i >= 10:
        ans = max(ans, cnt)
        return
    m = deepcopy(mals)
    for n in range(4):
        r = mals[n][0]
        dc = mals[n][1] + seq[i]
        if r == -1:
            continue
        if check_OOR(r, dc):
            mals[n][0] = -1
            dfs(i + 1, cnt)
            mals = deepcopy(m)
            continue

        conti = False
        for j in filter(lambda x: x != n, range(4)):
            mal_r, mal_c = mals[j][0], mals[j][1]
            if mal_r >= 0 and board[mal_r][mal_c] == board[r][dc]:
                conti = True
                break
        if conti:
            conti = False
            continue
    
        point = board[r][dc].get_value()
        mals[n][1] = dc
        if r == 0 and point in portal_keys:
            mals[n][0] = portal[point]
            mals[n][1] = 0
        dfs(i + 1, cnt + point)
        mals = deepcopy(m)

if __name__ == "__main__":
    first = [node(0)] + [node(i) for i in range(2, 41, 2)]
    last = [node(i) for i in range(25, 41, 5)]
    last[-1] = first[-1]

    right = [node(i) for i in range(10, 20, 3)] + last
    right[0] = first[5]

    up = [node(i) for i in range(20, 25, 2)] + last
    up[0] = first[10]

    left = [node(30)] + [node(i) for i in range(28, 25, -1)] + last
    left[0] = first[15]
    board = [first, right, up, left]

    portal = defaultdict(int)
    portal[10] = 1
    portal[20] = 2
    portal[30] = 3
    portal_keys = portal.keys()

    seq = readline()
    ans = 0
    mals = [[0, 0] for _ in range(4)]
    dfs(0, 0)
    print(ans)