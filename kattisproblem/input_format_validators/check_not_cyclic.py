#! /usr/env/python3

from collections import defaultdict
import sys

class Node:
    def __init__(self):
        self.neighbors = []
        self.dependencies = []
        self.from_ = None
    def __repr__(self):
        return self.name
    

class Graph:

    def __init__(self, strings=False):
        self.nodes = defaultdict(Node)
        self.no_dependencies = []
        if strings:
            self.from_strings(strings)
        else:
            self.load_data()

    def is_cyclic(self):
        visited = set()
        recursion_stack = set()

        def dfs(node):
            visited.add(node.name)
            recursion_stack.add(node.name)

            for neighbor_ in node.neighbors:
                neighbor = neighbor_.name
                if neighbor in recursion_stack:
                    return True
                if neighbor not in visited:
                    if dfs(neighbor_):
                        return True
            recursion_stack.remove(node.name)
            return False

        for node_name, node in list(self.nodes.items()):
            if node_name not in visited:
                if dfs(node):
                    return True
        return False

    def load_data(self):

        n = int(input())

        for _ in range(n):
            info = input().split(':')

            name = int(info[0].strip())
            time = int(info[1].strip())
            variability = info[2].strip()
            dependencies_str = info[3].strip()

            node = self.nodes[name]
            node.name = str(name)
            node.original_time = time
            node.time = time
            node.variability = variability
        
            if dependencies_str:
                node.dependencies = [self.nodes[int(dep)] for dep in dependencies_str.split(' ')]
            else:
                self.no_dependencies.append(node)

            node.unaccounted_deps = len(node.dependencies)

            for dependency in node.dependencies:
                dependency.neighbors.append(node) 

graph = Graph()

assert not graph.is_cyclic()

sys.exit(42)