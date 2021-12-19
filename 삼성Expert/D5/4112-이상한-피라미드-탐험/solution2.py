read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

depth = [0 for i in range(1, 12000)]
cnt = 0
for i in range(1, 150):
    for _ in range(0, i):
        cnt += 1
        depth[cnt] = i

def solve(a, b):
    if a > b:
        a, b = b, a
    d = depth[a]
    dl, dr = a, a
    for _ in range(142):
        dl += d
        dr += (d + 1)
        if dl <= b and b <= dr:
            return depth[b] - depth[a]
        if dl > b and depth[dl] - depth[b] == 1:
            break
        d += 1
    dl -= d
    dr -= (d + 1)
    if b <= dl:
        return (dl - b) + depth[b] - depth[a]
    else:
        return (b - dr) + depth[b] - depth[a]

TC = read()
for i in range(1, TC + 1):
    a, b = readline()
    print("#{} {}".format(i, solve(a, b)))
