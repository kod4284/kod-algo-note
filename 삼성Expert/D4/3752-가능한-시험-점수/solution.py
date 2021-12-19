read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

def solve():
    N = read()
    scores = readline()
    dp = [True] + [False for _ in range(sum(scores) + 1)]
    result = [0]
    for i in scores:
        for j in range(len(result)):
            s = i + result[j]
            if dp[s]:
                continue
            result.append(s)
            dp[s] = True
    return len(result)

TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))