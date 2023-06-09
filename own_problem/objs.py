from collections import defaultdict


class Node():
    def __init__(self):
        self.neighbors = []
        self.dependencies = []
        self.from_ = None
    def __repr__(self):
        return self.name
    

class PathFinder():
    def __init__(self):
        self.nodes = defaultdict(Node)
        self.no_dependencies = []

        self.load_data()
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

    def turn_dial(self, amount):

        for node in self.nodes.values():
            if node.variability == 'V':
                node.time = node.original_time * (amount / 1000)


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

class DFS(PathFinder):
    def __init__(self):
        self.nodes = defaultdict(Node)
        self.no_dependencies = []

        self.load_data()

    def depth_first(self, current, sum_time, all_times):
        sum_time += current.time
        all_times.append(sum_time)
        for neighbor in current.neighbors:
            self.depth_first(neighbor, sum_time, all_times)

    def depth_first_no_replace(self, current, sum_time, visited, all_times):    
        sum_time += current.time
        visited.add(current)
        all_times.append(sum_time)
        for neighbor in current.neighbors:
            if neighbor not in visited:
                self.depth_first_no_replace(neighbor, sum_time, visited, all_times)

    def search_wrong(self):
        visited = set()
        all_times = []
        for node in self.no_dependencies:
            self.depth_first_no_replace(node, 0, visited, all_times)  

        return max(all_times)
    
    def search_slow(self):
        all_times = []
        for node in self.no_dependencies:
            self.depth_first(node, 0, all_times)  

        return max(all_times)


    

        
        


