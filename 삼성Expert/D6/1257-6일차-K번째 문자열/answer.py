read = lambda: int(input())
readline = lambda: input().rstrip()

def make_all_cases(str):
    result_set = set()
    last = len(str) + 1
    for i in range(1, last):
        for j in range(last - i):
            temp = ""
            for k in range(i):
                temp += str[j + k]
            result_set.add(temp)
    return list(result_set)

def solve():
    K = read()
    str = readline()
    all_cases = make_all_cases(str)
    all_cases.sort()
    return all_cases[K - 1]
    
# 출력부
TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))