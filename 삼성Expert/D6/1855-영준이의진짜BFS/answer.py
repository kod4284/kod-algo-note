from collections import deque
import math

read = lambda: int(input())
readline = lambda: list(map(int, input().split()))

def init(graph):
    nodes = readline()
    arr = []
    for idx, i in enumerate(nodes):
        # 1번 노드랑 연결된 노드일때
        graph.append([i])
        graph[i].append(idx + 2)

# 부모 테이블 초기화
def set_parent(LIMIT, N, parent):
    for i in range(1, LIMIT):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

def bfs(graph, start, visited, path, depth, parent, LIMIT):
    queue = deque([start])
    visited[start] = True
    depth[start] = 0
    while queue:
        v = queue.popleft()
        path.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                # depth 계산
                depth[i] = depth[v] + 1
                # 부모 테이블 첫번째만 초기화
                parent[i][0] = v

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b, depth, parent, LIMIT):
    # b가 더 깊도록 설정
    if depth[a] > depth[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LIMIT - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지게
    if a == b:
        return a
    for i in range(LIMIT - 1, - 1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

def calculate_path(path, depth, parent, LIMIT):
    sum = 0
    for i in range(0, len(path) - 1):
        first = path[i]
        second = path[i + 1]
        # 공통 조상 찾기
        ca = lca(first, second, depth, parent, LIMIT)
        # 거리 계산하기 (a의 깊이 + b의 깊이 2 * 공통조상의 깊이)
        sum += (depth[first] + depth[second] - (2 * depth[ca]))
    return sum

def solve():
    N = read()
    graph = [[], []]
    visited = [False] * (N + 1)

    LIMIT = int(math.log2(N)) + 1 # 부모 노드 정보 기록 제한
    parent = [[0] * LIMIT for _ in range(N + 1)] # 부모 노드 정보
    depth = [0] * (N + 1) # 각 노드까지의 깊이
    path = []
    
    # 에레이 초기화
    init(graph)
    bfs(graph, 1, visited, path, depth, parent, LIMIT)
    set_parent(LIMIT, N, parent)

    return calculate_path(path, depth, parent, LIMIT)
    
# 출력부
TC = read()

for num in range(1, TC + 1):
    print("#{} {}".format(num, solve()))