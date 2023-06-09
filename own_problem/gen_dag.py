import random
from collections import defaultdict
from classes import CriticalPath
from sys import argv, stdin

n = int(argv[1])
max_time = int(argv[2])
num_test_cases = int(argv[3])
max_connections = int(argv[4])

graph = dict()

nodes = list(range(0, n))
random.shuffle(nodes)

graph[nodes[0]] = (random.randint(1, max_time), [])


for ind, node in enumerate(nodes[1:]):
    amount_depend = random.randint(1, min(ind+1, max_connections))
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

strings = []

strings.append(str(len(op_graph)))

for i, val in op_graph_items:
    letter = random.choice(['C', 'V'])
    strings.append(f"{i}:{val[0]}:{letter}:{' '.join(map(str, val[1]))}")


def get_range():
    path_finder = CriticalPath(strings)
    high = path_finder.get_critical_path()[1]
    path_finder.turn_dial(0.00001)
    low = path_finder.get_critical_path()[1]
    return low, high


low, high = get_range()
for _ in range(num_test_cases):
    strings.append(str(random.randint(int(low), int(high))))


for string in strings:
    print(string)


