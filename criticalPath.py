n = int(input())
# node time dictionary 
taskTimeDict = {}
# graph dictionary
graph = {}
for i in range(n):
    line = input().split()
    node, time = line[0], line[1]
    # append weight of the node
    taskTimeDict[node] = time
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
print(taskTimeDict)
# print(critical_path(graphConnections))
#print(nodeTimeDict)