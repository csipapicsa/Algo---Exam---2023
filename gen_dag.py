import random
from collections import defaultdict

n = 10
max_time = 100
graph = dict()

nodes = list(range(0, n))
random.shuffle(nodes)

graph[nodes[0]] = (random.randint(1, max_time), [])


for ind, node in enumerate(nodes[1:]):
    amount_depend = random.randint(1, ind+1)
    depends = random.sample(graph.keys(), amount_depend)
    graph[node] = (random.randint(1, max_time), depends)

op_graph = dict()
for i in graph:
    op_graph[i] = (graph[i][0], [])


for i in graph:
    for j in graph[i][1]:
        print(i, j)
        op_graph[j][1].append(i)

for i in graph:
    print(f'{i}: {graph[i]}')

print('------------------------')

for i in op_graph:
    print(f'{i}: {op_graph[i]}')