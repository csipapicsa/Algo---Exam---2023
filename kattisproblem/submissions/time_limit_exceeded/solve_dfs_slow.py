#! /usr/bin/env python3

import sys
sys.path.insert(0, '..')

#from libs.classes import CriticalPath
#from libs.functions import search_analytic, check_limits

from collections import defaultdict


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

    def from_strings(self, list_of_strings):
        n = list_of_strings[0]

        for inp in list_of_strings[1:]:
            info = inp.split(':')

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


    def turn_dial(self, amount):

        for node in self.nodes.values():
            if node.variability == 'V':
                node.time = node.original_time * (amount / 1000)


    
    

class CriticalPath(Graph):

    def __init__(self, strings=False):
        super().__init__(strings)
        self.find_top_order()

    def find_top_order(self):
        self.top_order = []

        while self.no_dependencies:
            current = self.no_dependencies.pop()
            self.top_order.append(current)

            for neighbor in current.neighbors:
                neighbor.unaccounted_deps -= 1

                if neighbor.unaccounted_deps == 0:
                    self.no_dependencies.append(neighbor)

    def _compute_longest_paths(self):
        '''
        Computes the longest path to each node in self.nodes
            will be stored in nodes as node.sum_time
        '''
        for node in self.top_order:
            node.sum_time = node.time

            for dependency in node.dependencies:
                if dependency.sum_time + node.time > node.sum_time:
                    node.sum_time = dependency.sum_time + node.time
                    node.from_ = dependency

    def _find_max_node(self):
        '''
        finds the node with the maximum sum_time value
        '''
        current = self.top_order[0]
        for node in self.top_order[1:]:
            if node.sum_time > current.sum_time:
                current = node
        return current
    
    def get_time(self):
        self._compute_longest_paths()
        max_node = self._find_max_node()

        return max_node.sum_time

    def get_critical_path(self):
        self._compute_longest_paths()
        max_node = self._find_max_node()

        critical_path = []

        current = max_node      
        while current:
            critical_path.append(current)
            current = current.from_
        return critical_path, max_node.sum_time


class BinarySearch: 

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
    


# WRONG SOLUTIONS
    

class DfsSlow(Graph):

    def _depth_first(self, current, sum_time, all_times):

        sum_time += current.time
        all_times.append(sum_time)

        for neighbor in current.neighbors:
            self._depth_first(neighbor, sum_time, all_times)

    def get_time(self):
        all_times = []
        for node in self.no_dependencies:
            self._depth_first(node, 0, all_times)  

        return max(all_times)
    
class DfsWrong(Graph):

    def _depth_first(self, current, sum_time, visited, all_times):    
        sum_time += current.time
        all_times.append(sum_time)

        visited.add(current)

        for neighbor in current.neighbors:
            if neighbor not in visited:
                self._depth_first(neighbor, sum_time, visited, all_times)

    def get_time(self):
        all_times = []
        visited = set()
        for node in self.no_dependencies:
            self._depth_first(node, 0, visited, all_times)  

        return max(all_times)


def check_limits(path_finder, correct_time):

    path_finder.turn_dial(1000)
    time = path_finder.get_time()

    if correct_time > time:
        print(1000)
        return True

    path_finder.turn_dial(0)
    time = path_finder.get_time()

    if correct_time < time:
        print("Impossible")
        return True
    
    return False


def search_analytic(path_finder, correct_time):

    bs = BinarySearch(1000)
    path, time = path_finder.get_critical_path()
    prev_path = None

    while True:     
        dial = bs.step(correct_time - time > 0)
        path_finder.turn_dial(dial)
        path, time = path_finder.get_critical_path()
        if path == prev_path and (time >= correct_time >= prev_time or time <= correct_time <= prev_time):
            a = (prev_time - time) / (prev_dial - dial)
            dial = ((correct_time - time) / a) + dial
            break
        prev_dial = dial
        prev_path, prev_time = path, time

    return dial


def search(path_finder, correct_time):
    bs = BinarySearch(1000)

    dial = 1000
    time = path_finder.get_time()

    while abs(correct_time - time) > 0.01:
        dial = bs.step(correct_time - time > 0)
        path_finder.turn_dial(dial)
        time = path_finder.get_time()

    return dial


path_finder = DfsSlow()
while True:
    try:
        correct_time = int(input())
        if check_limits(path_finder, correct_time):
            continue
        
        dial = search(path_finder, correct_time)
        print(dial)
    except EOFError:
        break