import math

def dfs(a, b):
    P[b][0] = a
    depth[b] = depth[a] + 1
    for c in G[b]:
        if a != c:
            dfs(b, c)

def lca(a, b):
    d = depth[b] - depth[a]
    if d < 0:
        a, b = b, a
        d *= -1
    for i in range(MAX_DEPTH, -1, -1):
        if d & (1 << i):
            b = P[b][i]
    for i in range(MAX_DEPTH, -1, -1):
        if P[a][i] != P[b][i]:
            a = P[a][i]
            b = P[b][i]
    if a == b:
        return a
    return P[a][0]

def path_length(a, b):
    c = lca(a, b)
    return depth[a] - depth[c] + depth[b] - depth[c] + 1

n = int(input())
MAX_NODE = n
MAX_DEPTH = math.ceil(math.log(MAX_NODE) / math.log(2))
G = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)
P = [[0] * MAX_DEPTH for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dfs(1, 1)
for j in range(1, MAX_DEPTH):
    for i in range(1, n + 1):
        P[i][j] = P[P[i][j - 1]][j - 1]

res = 0
for i in range(1, n + 1):
    for j in range(2 * i, n + 1, i):
        res += path_length(i, j)

print(res)