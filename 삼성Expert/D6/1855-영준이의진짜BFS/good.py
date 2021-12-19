from collections import deque
import math
 
# 그래프, 족보, 깊이표, 두 노드가 주어졌을 때 공통 조상 반환하는 함수
def getAncester(graph, jokbo, depth, n1, n2):
    # 깊이가 깊은 노드를 n2에 두기
    if depth[n1] > depth[n2]:
        n1, n2 = n2, n1
 
    # 같은 깊이로 맞추기
    limit = len(jokbo[-1])
    while depth[n1] != depth[n2]:
        diff = depth[n2]-depth[n1]
 
        for j in range(limit-1, -1, -1):
            if 2**j <= diff:
                n2 = jokbo[n2][j]
                break
 
    # 조상 찾기
    if n1 == n2:
        return n2
 
    for j in range(limit-1, -1, -1):
        if jokbo[n1][j] != jokbo[n2][j]:
            n1 = jokbo[n1][j]
            n2 = jokbo[n2][j]
 
    return jokbo[n2][0]
 
 
for test_case in range(1, int(input()) + 1):
    N = int(input()) # 정점 개수
    limit = int(math.log2(N))+1 # 최대 2xk 한계
    jokbo = [[0]*limit for _ in range(N+1)] # 족보  노드 i의 2xj번째 조상
 
    # 그래프 만들기
    temp = [ int(node) for node in input().split() ]
    temp = [0, 0] + temp
 
    # 각 노드에서 연결된 다른 노드들을 모두 보여주는 그래프로 만들어보기
    graph = [[] for _ in range(N+1)]
    for i in range(2, len(temp)):
        graph[i].append(temp[i])
        graph[temp[i]].append(i)
 
    # BFS 각 깊이 (1부터 시작), 족보에서 부모, 방문 경로 구하기
    depth = [0]*(N+1)
    isVisited = [False]*(N+1)
    visited_path = []
 
    # 스타팅 포인트 1부터 시작
    need_visit = deque([1])
    visited_path.append(1)
    isVisited[1] = True
    depth[1] = 1
 
    while need_visit:
        node = need_visit.popleft()
        next_nodes = graph[node]
 
        for next in next_nodes:
            if not isVisited[next]:
                need_visit.append(next)
                visited_path.append(next)
                depth[next], jokbo[next][0], isVisited[next] = depth[node]+1, node, True
 
    # 족보 다 채우기
    for j in range(limit-1): # 노드 i의 2xj번째 조상
        for i in range(1, N+1): # 1을 제외한 모든 노드 (1은 최고 조상)
            if jokbo[i][j] != jokbo[i][j+1]:
                jokbo[i][j+1] = jokbo[jokbo[i][j]][j]
 
    # 경로 계산하기
    result = 0
    for k in range(len(visited_path)-1):
        src, dst = visited_path[k], visited_path[k+1]
        ancester = getAncester(graph, jokbo, depth, src, dst)
        result += (depth[src]+depth[dst])-(2*depth[ancester])
 