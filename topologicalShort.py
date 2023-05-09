import readIn2 as r

def topological_sort(graph):
    """
    Perform a topological sort on a directed acyclic graph (DAG).

    Args:
        graph: A dictionary representing a DAG, where each key is a node and
               the corresponding value is a list of its adjacent nodes.

    Returns:
        A list of nodes in topological order.

    Raises:
        ValueError: If the graph contains a cycle.
    """
    #for node[0] in graph: print(node[0])
    # Create a dictionary to keep track of the in-degree of each node
    in_degree = {node[0]: 0 for node in graph}
    print(f"indegree {in_degree}")

    # Calculate the in-degree of each node
    for node in graph:
        for adj_node in graph[node]:
            in_degree[adj_node] += 1

    # Create a queue to store nodes with zero in-degree
    zero_in_degree = [node for node in in_degree if in_degree[node] == 0]

    # Create a list to store the topological order of nodes
    topo_order = []

    # Process each node with zero in-degree
    while zero_in_degree:
        node = zero_in_degree.pop(0)
        topo_order.append(node)

        # Decrease the in-degree of each adjacent node
        for adj_node in graph[node]:
            in_degree[adj_node] -= 1

            # Add the adjacent node to the queue if its in-degree becomes zero
            if in_degree[adj_node] == 0:
                zero_in_degree.append(adj_node)

    # Check if there is a cycle in the graph
    if len(topo_order) != len(graph):
        raise ValueError("The graph contains a cycle")

    return topo_order

graph, execution_times = r.readIn()
#print(graph)

topological_sort(graph)