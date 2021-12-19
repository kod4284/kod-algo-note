readline = lambda: list(map(int, input().split()))

max_v = -int(1e9)
min_v = int(1e9)

N = int(input())
A = readline()
a, b, c, d = readline()
s = set()
ops = []

def cal(sum_v, idx, add, sub, mul, div):
    global max_v, min_v
    if idx == N:
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)
        return
    if add:
        cal(sum_v + A[idx], idx + 1, add - 1, sub, mul, div)
    if sub:
        cal(sum_v - A[idx], idx + 1, add, sub - 1, mul, div)
    if mul:
        cal(sum_v * A[idx], idx + 1, add, sub, mul - 1, div)
    if div:
        cal(int(sum_v / A[idx]), idx + 1, add, sub, mul, div - 1)

cal(A[0], 1, a, b, c, d)
print(max_v)
print(min_v)