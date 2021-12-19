from collections import deque, defaultdict
def bfs():
    visited = []
    q = deque()
    q.append(1)
    while q:
        s = q.popleft()
        visited.append(s)
        if s in graph:
            for i in graph[s]:
                q.append(i)
                depth_list[i] = depth_list[s] +1
    return visited
  
def lca(a, b):
    if depth_list[a] < depth_list[b]:
        a, b = b, a     
    for j in range(max_log_depth,-1,-1):
        if 1<<j <= depth_list[a]-depth_list[b]:
            a = dp[j][a]
    if a == b :
        return a
      
    for j in range(max_log_depth-1,-1,-1):
        if dp[j][a] != dp[j][b]:
            a = dp[j][a]
            b = dp[j][b]
    return dp[0][a]
      
def dist(a,b):
    com_anc = lca(a,b)
    result = -2*depth_list[com_anc] + depth_list[a] + depth_list[b]
    return result
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0, 0] + list(map(int, input().split()))
    graph = defaultdict(list)
    for i, parent in enumerate(tree):
        graph[parent].append(i)
    depth_list = [0] * (N+1)
    dp = [[0]* (N+1) for _ in range(20)]
    max_log_depth = 20
    for k in range(max_log_depth):
        for i in range(N+1):
            if k == 0:
                dp[k][i] = tree[i]
            else:
                dp[k][i] = dp[k-1][dp[k-1][i]]
    visited = bfs()
    dis = 0
    for i in range(len(visited)-1):
        dis += dist(visited[i],visited[i+1])
    print('#%i %i'%(test_case,dis))