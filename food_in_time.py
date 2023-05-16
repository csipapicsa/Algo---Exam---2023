from collections import defaultdict

nodes = defaultdict(dict)

n = int(input())

no_deps = []

for _ in range(n):
    info = input().split(':')

    name = int(info[0].strip())
    time = int(info[1].strip())
    nodes[name]['time'] = time
    type_ = info[2].strip()
    nodes[name]['type'] = type_


    has_deps = info[3].strip()
    if has_deps:
        depends = [int(node) for node in has_deps.split(' ')]
        nodes[name]['depends'] = [nodes[node] for node in depends]
    else:
        nodes[name]['depends'] = []
        no_deps.append(nodes[name])

    nodes[name]['unaccounted_deps'] = len(nodes[name]['depends'])

    for dep in nodes[name]['depends']:
        if 'neighbors' not in dep:
            dep['neighbors'] = []
        nodes[name]['neighbors'].append(nodes[name])


top_order = []

while no_deps:
    current = no_deps.pop()
    top_order.append(current)

    for neighbor in current['neighbors']:
        neighbor['unaccounted_deps'] -= 1

        if neighbor['unaccounted_deps'] == 0:
            no_deps.append(neighbor)


print(top_order)




        
    


print(no_deps)