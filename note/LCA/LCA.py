import sys
from collections import deque
sys.setrecursionlimit(int(1e5))
n = int(input())

# 먼저 선언할 것
parent = [0] * (n + 1) # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프의 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이 구했으면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

# bfs 로 구현
def bfs(x, depth):
    queue = deque([x])
    c[x] = True
    d[x] = depth
    while queue:
        v = queue.popleft()
        for y in graph[v]:
            if c[y]: # 이미 깊이 구했으면 넘기기
                continue
            parent[y] = v
            d[y] = d[v] + 1
            queue.append(y)
            c[y] = True


# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

bfs(1, 0)

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))