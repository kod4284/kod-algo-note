import copy

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

def solve():
    N, K = readline()
    cash_map = {}
    count_map = {}
    cash_type = []
    for _ in range(N):
        value, count = readline()
        cash_map.update({value: count})
        cash_type.append(value)
    cash_type.reverse()

    for i in range(1, K):
        change = K - i
        temp_cash_map = copy.deepcopy(cash_map)
        count = 0
        for j in cash_type:
            if j > change:
                continue
            # 새로운 돈이면 카운트
            if temp_cash_map[j] == 0:
                count += 1
            # 동전 몇개인지 계산
            div = change // j
            # 동전 지갑 업데이트 
            temp_cash_map[j] += div
            change %= j
        count_map.update({i:count})

    map_key_list = count_map.keys()
    tuple_list = []
    for key in map_key_list:
        tuple_list.append((key, count_map[key]))
    tuple_list.sort(key=lambda x:-x[1])
    return "{} {}".format(tuple_list[0][1], tuple_list[0][0])
    
# 출력부
TC = read()
for i in range(1, TC + 1):
    print("#{} {}".format(i, solve()))