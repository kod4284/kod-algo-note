readline = lambda: list(map(int, input().split()))

# -> 화살표 찍힌 방향 역으로 올라가서 의존성 없는 V 삭제 및 출력
def dfs(v, graph, deleted, vs):
    if deleted[v]:
        return
    for i, arr in enumerate(graph):
        if i == 0 or deleted[i]:
            continue
        if v in arr and not deleted[v]:
            return dfs(i, graph, deleted, vs)
    print(v, end=" ")
    vs.remove(v)
    deleted[v] = True
    return v

def solve():
    V, E = readline()
    graph = [[] for _ in range(V + 1)]
    # 삭제된 V 기록
    deleted = [False] * (V + 1)
    # 남아있는 V 있는지 없는지 계속 체크 위해서 만든 리스트
    vs = [i for i in range(1, V + 1)]

    # 그래프 초기화
    data = readline()
    for i in range(0, len(data), 2):
        graph[data[i]].append(data[i + 1])
    # 전부 삭제 될때까지 dfs 작동시키기
    while vs:
        dfs(vs[0], graph, deleted, vs)

# 출력부
for i in range(1, 11):
    print("#{}".format(i), end=" ")
    solve()
    print()