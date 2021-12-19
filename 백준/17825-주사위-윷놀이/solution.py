from collections import defaultdict
readline = lambda: list(map(int, input().split()))

class node:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

def print_arr(arr):
    for i in arr:
        for j in i:
            print(j.value, end=" ")
        print()

def check_OOR(r, c):
    return c >= len(board[r])

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
ans = -int(1e9)

for k in range(4**10 + 1):
    quo = k
    cnt = 0
    pas = False
    mals = [[0, 0] for _ in range(4)]
    for idx in range(10):
        n = quo % 4
        quo //= 4
        jump = seq[idx]
        r = mals[n][0]
        if r == -1:
            pas = True
            break
        dc = mals[n][1] + jump
        if check_OOR(r, dc):
            mals[n][0] = -1
            continue
        for i in filter(lambda x: x != n, range(4)):
            mal_r, mal_c = mals[i][0], mals[i][1]
            if mal_r >= 0 and board[mal_r][mal_c] == board[r][dc]:
                pas = True
                break
        if pas:
            break
        
        point = board[r][dc].get_value()
        mals[n][1] = dc
        if r == 0 and point in portal_keys:
            mals[n][0] = portal[point]
            mals[n][1] = 0
        cnt += point
    else:
        ans = max(cnt, ans)
print(ans)