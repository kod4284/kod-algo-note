import bisect
readline = lambda: list(map(int, input().split()))

n, m = readline()
a = readline()
set_a = set()
q = []
for _ in range(m):
    i, j, k = readline()
    q.append((i, j, k))

a.sort()
for i in a:
    set_a.add(i)

list_a = list(set_a)
print(bisect.bisect_left(list_a, 5))