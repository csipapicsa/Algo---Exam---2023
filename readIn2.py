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

def readIn ():
    n = int(input())
    # node time dictionary 
    execution_times = {}
    earliest_start_times = {}
    # graph dictionary
    graph = {}
    for i in range(n):
        parts = input().split(':')
        node = int(parts[0])
        time = int(parts[1])
        execution_times[node] = time
        earliest_start_times[node] = -float('inf')
        graph[node] = list()
        if len(parts[2]) == 0:
            # do nothing
            continue
        else:
            dependendNodes = [int(e) for e in parts[2].split(',')]
            #dependendNodes
            for i in dependendNodes:
                # build the graphs
                graph[node].append(i)
                #print(f"dependent node {i}")

    """graphConnections = []
    for key, value in graph.items():
        #print(f"key, value {key} {value}")
        for v in value:
            graphConnections.append([int(v), int(key)])
    """        
    # new method
    graphConnectionsSet = set()
    for key, value in graph.items():
        graphConnectionsSet.add(key)
    
    #print(graphConnectionsSet)
    # init dictionary
    graphConnections = {}
    for k in graphConnectionsSet:
        graphConnections[k] = list()
    
    #print(graphConnections)
    for key, value in graph.items():
        #print(f"key, value {key} {value}")
        for v in value:
            graphConnections[int(v)].append(key)
    print(graphConnections)
    print(execution_times)
    # print(critical_path(graphConnections))
    #print(nodeTimeDict)
    return graphConnections, execution_times