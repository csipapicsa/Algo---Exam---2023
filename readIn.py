def critical_path(execution_times, earliest_start_times, graphConnections):
    """# Step 1: Create a dictionary to store execution times
    execution_times = {node: dag.nodes[node]['execution_time'] for node in dag}

    # Step 2: Create a dictionary to store earliest start times
    earliest_start_times = {node: -float('inf') for node in dag}
    earliest_start_times[dag.source()] = 0

    # Step 3: Topological sort
    sorted_nodes = list(nx.topological_sort(dag))
    """

    # Step 4: Calculate earliest start times
    for node in sorted_nodes:
        for predecessor in dag.predecessors(node):
            earliest_start_times[node] = max(
                earliest_start_times[node], earliest_start_times[predecessor] + execution_times[predecessor])

    """# Step 5: Calculate latest completion times
    latest_completion_times = {node: earliest_start_times[dag.sink()] for node in dag}
    for node in reversed(sorted_nodes):
        for successor in dag.successors(node):
            latest_completion_times[node] = min(
                latest_completion_times[node], latest_completion_times[successor] - execution_times[node])
    """
    # Step 6: Calculate critical path duration
    critical_path_duration = latest_completion_times[dag.source()] - earliest_start_times[dag.source()]

    return critical_path_duration

n = int(input())
# node time dictionary 
execution_times = {}
earliest_start_times = {}
# graph dictionary
graph = {}
for i in range(n):
    line = input().split()
    node, time = line[0], line[1]
    # append weight of the node
    execution_times[node] = time
    earliest_start_times[node] = -float('inf')
    graph[node] = list()
    if len(line) < 3:
        # do nothing
        continue
    else:
        dependendNodes = line[2:]
        for i in dependendNodes:
            # build the graphs
            graph[node].append(i)
            #adj[0].append([node, 5])
            #print(f"dependent node {i}")

# generate the graph
# [0, 1] 0 -> 1
# [2, 3] 2 -> 3
graphConnections = []
for key, value in graph.items():
    #print(f"key, value {key} {value}")
    for v in value:
        graphConnections.append([int(v), int(key)])
print(graphConnections)
print(execution_times)
# print(critical_path(graphConnections))
#print(nodeTimeDict)