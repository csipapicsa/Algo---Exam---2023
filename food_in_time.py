from collections import defaultdict
from matplotlib import pyplot as plt

class Node():
    def __init__(self):
        self.neighbors = []
        self.depends = []
        self.from_ = None
    def __repr__(self):
        return self.name

nodes = defaultdict(Node)

n = int(input())

no_deps = []

for _ in range(n):
    info = input().split(':')

    name = int(info[0].strip())
    time = int(info[1].strip())
    type_ = info[2].strip()
    has_deps = info[3].strip()

    node = nodes[name]
    node.name = str(name)
    node.org_time = time
    node.time = time
    node.type = type_
  
    if has_deps:
        depends = [int(dep) for dep in has_deps.split(' ')]
        node.depends = [nodes[dep] for dep in depends]
    else:
        no_deps.append(node)

    node.unaccounted_deps = len(node.depends)

    for dep in node.depends:
        dep.neighbors.append(node)


def find_top_oder(no_deps):
    top_order = []

    while no_deps:
        current = no_deps.pop()
        top_order.append(current)

        for neighbor in current.neighbors:
            neighbor.unaccounted_deps -= 1

            if neighbor.unaccounted_deps == 0:
                no_deps.append(neighbor)
    return top_order


def turn_up_dial(top_order, amount):
    for node in top_order:
        if node.type == 'V':
            node.time = node.org_time * amount


def compute_crit_path(top_order):
    for node in top_order:
        node.sum_time = node.time

        for dep in node.depends:
            if dep.sum_time + node.time > node.sum_time:
                node.sum_time = dep.sum_time + node.time
                node.from_ = dep

 
def find_max_node(top_order):
    current = top_order[0]
    for node in top_order[1:]:
        if node.sum_time > current.sum_time:
            current = node
    return current


def find_crit_path(current):
    crit_path = []
    while current:
        crit_path.append(current)
        current = current.from_
    return crit_path

def get_crit_len(top_order, dial):
    turn_up_dial(top_order, dial)
    compute_crit_path(top_order)
    max_node = find_max_node(top_order)

    return max_node.sum_time



class binary_search: 
    def __init__(self, topspeed):
        self.topspeed = topspeed
        self.visited = []
        self.nextDistance = self.topspeed / 2
        
    def step(self, searchHigher):
        if not self.visited: self.visited.append(self.nextDistance)
        elif searchHigher: self.visited.append(self.visited[-1] + self.nextDistance)
        else: self.visited.append(self.visited[-1] - self.nextDistance)
        self.nextDistance /= 2
        return self.visited[-1]
    
bs = binary_search(100)

print(bs.step(False))
print(bs.step(True))
print(bs.step(False))
print(bs.step(True))
print(bs.step(False))



top_order = find_top_oder(no_deps)

crit_lens = []

for j in range(100, 0, -1):
    i = j / 100
    crit_lens.append(get_crit_len(top_order, i))