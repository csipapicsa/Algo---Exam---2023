class Node:
    def __init__(self):
        self.links = []

class Link:
    def __init__(self, source, destination, weight):
        self.source = source 
        self.destination = destination
        self.weight = weight


nodes = dict()
#n = int(input())
n = 10
#links = []

for _ in range(n):
    name, weight, depends = input().split(':')

    name = int(name.strip())
    weight = int(weight.strip())
    depends = [int(node.strip()) for node in depends.split(',') if depends.strip()]

    first_node = Node()
    second_node = Node()

    first_node.links.append(Link(first_node, second_node, weight))
    nodes[name] = (first_node, second_node)
    links.append((name, depends))

for link in links:
    for depend in link[1]:
        nodes[depend][1].links.append(Link(nodes[depend], nodes[link[0]], 0))








        