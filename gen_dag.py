import random

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

for i in graph:
    print(f'{i}: {graph[i]}')