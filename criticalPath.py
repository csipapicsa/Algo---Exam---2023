from collections import deque

def critical_path(graph):
    # Step 1: Compute the earliest start time of each task
    earliest_start = {task: 0 for task in graph}
    queue = deque([task for task in graph if not graph[task]])
    while queue:
        task = queue.popleft()
        for successor in graph[task]:
            earliest_start[successor] = max(earliest_start[successor], earliest_start[task] + graph[task][successor])
            graph[successor].pop(task)
            if not graph[successor]:
                queue.append(successor)

    # Step 2: Compute the latest start time of each task
    latest_start = {task: earliest_start[task] for task in graph}
    queue = deque([task for task in graph if not graph[task]])
    while queue:
        task = queue.popleft()
        for predecessor in graph[task]:
            latest_start[predecessor] = min(latest_start[predecessor], latest_start[task] - graph[predecessor][task])
            graph[predecessor].pop(task)
            if not graph[predecessor]:
                queue.append(predecessor)

    # Step 3: Compute the critical path
    critical_path = []
    for task in earliest_start:
        if earliest_start[task] == latest_start[task]:
            critical_path.append(task)

    return earliest_start, latest_start, critical_path
    
"""
This implementation assumes that the graph is represented as a dictionary of tasks and their dependencies. The dependencies are themselves represented as a dictionary of successor tasks and their weights.

The algorithm works in three steps:

Compute the earliest start time of each task by iteratively traversing the graph in topological order and computing the earliest start time of each successor task as the maximum of the earliest start time of its predecessors plus the weight of the edge connecting them.

Compute the latest start time of each task by iteratively traversing the graph in reverse topological order and computing the latest start time of each predecessor task as the minimum of the latest start time of its successors minus the weight of the edge connecting them.

Compute the critical path by iterating over all tasks and checking if their earliest and latest start times are equal. If they are, the task is on the critical path.

The function returns a tuple containing the earliest start time and latest start time of each task, as well as the list of tasks on the critical path.
"""

n = int(input())
# node time dictionary 
nodeTimeDict = {}
# graph dictionary
graph = {}
for i in range(n):
    line = input().split()
    node, time = line[0], line[1]
    # print(f"node and time {node}, {time}")
    # append weight
    nodeTimeDict[node] = time
    graph[node] = list()
    if len(line) < 3:
        # do nothing
        continue
    else:
        #length = len(line[2:])
        dependendNodes = line[2:]
        #print(f"len of dependent nodes {length}")
        #graph[node] = 
        for i in dependendNodes:
            # build the graphs
            graph[node].append(i)
            #adj[0].append([node, 5])
            #print(f"dependent node {i}")

#print(graph)
graphConnections = []
for key, value in graph.items():
    #print(f"key, value {key} {value}")
    for v in value:
        graphConnections.append([int(v), int(key)])
print(graphConnections)
print(critical_path(graphConnections))
#print(nodeTimeDict)