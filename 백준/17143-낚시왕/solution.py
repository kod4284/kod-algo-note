from collections import defaultdict
readline = lambda: list(map(int, input().split()))

DIR = [(-1, 0), (1, 0), (0, 1), (-1, 0)]
R, C, M = readline()
sharks = defaultdict(list)
fisher = 0
for _ in range(M):
    r, c, s, d, z = readline()
    sharks[(r, c)] = [s, d, z]

def move(r, c, s, d):
    global R, C
    TR, TC = R, C
    d -= 1
    if d == 0:
        if s <= r - 1:
            r -= s
            return (r, c, d + 1)
        s -= r - 1
        quo = s // (TR - 1)
        rem = s % (TR - 1)
        if quo % 2 != 0:
            r = TR - rem
        else:
            d = 1
            r = 1 + rem
        return (r, c, d + 1)
    elif d == 1:
        if s <= TR - r:
            r += s
            return (r, c, d + 1)
        s -= TR - r
        quo = s // (TR - 1)
        rem = s % (TR - 1)
        if quo % 2 != 0:
            r = 1 + rem
        else:
            d = 0
            r = TR - rem
        return (r, c, d + 1)
    elif d == 2:
        if s <= TC - c:
            c += s
            return (r, c, d + 1)
        s -= TC - c
        quo = s // (TC - 1)
        rem = s % (TC - 1)
        if quo % 2 != 0:
            c = 1 + rem
        else:
            d = 3
            c = TC - rem
        return (r, c, d + 1)
    elif d == 3:
        if s <= c - 1:
            c -= s
            return (r, c, d + 1)
        s -= c - 1
        quo = s // (TC - 1)
        rem = s % (TC - 1)
        if quo % 2 != 0:
            c = TC - rem
        else:
            d = 2
            c = 1 + rem
        return (r, c, d + 1)
    

sumv = 0
fisher = 0
while fisher <= C:
    fisher += 1
    target = list(filter(lambda x: x[1] == fisher, sorted(sharks.keys())))
    if target:
        _, _, tz = sharks[target[0]]
        sumv += tz
        sharks.pop(target[0]) 
    new_sharks = defaultdict(list)
    for kr, kc in list(sharks.keys()):
        s, d, z = sharks[(kr, kc)]
        mr, mc, md = move(kr, kc, s, d)
        new_sharks[(mr, mc)].append([s, md, z])

    for kr, kc in new_sharks.keys():
        if len(new_sharks[(kr, kc)]) > 1:
            maxv = max(new_sharks[(kr, kc)], key=lambda x: x[2])
            new_sharks[(kr, kc)] = maxv
        else:
            new_sharks[(kr, kc)] = new_sharks[(kr, kc)][0]
    sharks = new_sharks

print(sumv)