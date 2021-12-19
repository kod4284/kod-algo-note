from itertools import permutations

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

def solve():
    N = read()
    l = readline()
    arr = []
    for i in range(0, len(l), 2):
        if i == 0:
            comp = (l[i], l[i + 1])
        elif i == 2:
            home = (l[i], l[i + 1])
        else:
            arr.append((l[i], l[i + 1]))
    cases = permutations(arr, N)
    minv = int(1e9)
    ans = []
    for c in cases:
        sumv = 0
        for i, v in enumerate(c):
            r, c = v
            if i == 0:
                sumv += abs(comp[0] - r) + abs(comp[1] - c)
                pr, pc = r, c
            else:
                sumv += abs(pr - r) + abs(pc - c)
                pr, pc = r, c
        
        sumv += abs(home[0] - pr) + abs(home[1] - pc)
        ans.append(sumv)
    return min(ans)
    

TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))
