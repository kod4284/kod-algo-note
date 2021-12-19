ops = ['+', '*', '-', '/']

def check_leef(node):
    l, r = node * 2, node * 2 + 1
    return not tree[l] and not tree[r]

def check_valid_leef(node):
    l, r = node * 2, node * 2 + 1
    return not tree[l] and not tree[r] and not tree[node] in ops

def check(node):
    l, r = node * 2, node * 2 + 1
    if not tree[l] or not tree[r]:
        return False
    if not tree[node] in ops:
        return False
    return True

def search(node):
    global ans
    if not check(node) and not check_valid_leef(node):
        ans = 0
    if check_leef(node):
        return
 
    search(node * 2)
    search(node * 2 + 1)

def solve():
    global tree, ans
    N = int(input())
    for i in range(1, N + 1):
        line = input().split()
        n, v = line[0], line[1]
        tree[int(n)] = v
    search(1)
    return ans

for i in range(1, 11):
    tree = [None] * 512
    ans = 1
    print("#{} {}".format(i, solve()))
