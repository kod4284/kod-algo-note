read = lambda: int(input())
readline = lambda: input()

def solve():
    K = read()
    st = readline()
    arr = []
    for i in range(len(st)):
        arr.append(st[i:])
    return sorted(arr)[K - 1]

TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))