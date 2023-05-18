import random
from collections import defaultdict

n = 1000
max_time = 100
graph = dict()

nodes = list(range(0, n))
random.shuffle(nodes)

graph[nodes[0]] = (random.randint(1, max_time), [])


for ind, node in enumerate(nodes[1:]):
    amount_depend = random.randint(1, min(ind+1, 5))
    depends = random.sample(graph.keys(), amount_depend)
    graph[node] = (random.randint(1, max_time), depends)

op_graph = dict()
for i in graph:
    op_graph[i] = (graph[i][0], [])


for i in graph:
    for j in graph[i][1]:
        op_graph[j][1].append(i)


op_graph_items = list(op_graph.items())
random.shuffle(op_graph_items)

print(len(op_graph))
for i, val in op_graph_items:
    letter = random.choice(['C', 'V'])
    print(f"{i}:{val[0]}:{letter}:{' '.join(map(str, val[1]))}")

print(1300)