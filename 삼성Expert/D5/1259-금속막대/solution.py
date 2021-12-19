from itertools import permutations
readline = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    line = readline()
    cases = []
    for i in range(0, 2 * n, 2):
        cases.append([line[i], line[i + 1]])
    while len(cases) != 1:
        stop = False
        for i in range(len(cases)):
            if stop:
                break
            for j in range(len(cases)):
                if cases[i] == cases[j]:
                    continue
                if cases[i][-1] == cases[j][0]:
                    cases[i].extend(cases[j])
                    cases.remove(cases[j])
                    stop = True
                    break
    return " ".join(map(str, cases[0]))

if __name__ == "__main__":
    TC = int(input())
    for i in range(1, 11):
        print("#{} {}".format(i, solve()))