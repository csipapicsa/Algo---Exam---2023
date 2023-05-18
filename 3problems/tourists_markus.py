from collections import defaultdict


def search(start, node, count, nodes):
    global sum_, visited
    if node in visited:
        return
    visited.add(node)
    if node > start and node % start == 0:
        sum_ += count
    for neighbor in nodes[node]:
        search(start, neighbor, count + 1, nodes)


while True:
    
    try:
        nodes = defaultdict(list)
        n = int(input())
        for _ in range(1, n):
            from_, to_ = map(int, input().strip().split(' ')) 
            nodes[from_].append(to_)
            nodes[to_].append(from_)

        sum_ = 0
        for i in range(1, n):
            visited = set()
            search(i, i, 1, nodes)

        print(sum_)
        

    except EOFError:
        break