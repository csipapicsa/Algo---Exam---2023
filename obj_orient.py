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

        self.find_top_order()


    def turn_dial(self, amount):

        for node in self.top_order:
            if node.variability == 'V':
                node.time = node.original_time * amount


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



if __name__ == "__main__":
    path_finder = PathFinder()

    correct_time = int(input())

    bs = binary_search(1)

    path, time = path_finder.get_critical_path()
    prev_path = None

    while abs(correct_time - time) > 0.00001:
        dial = bs.step(correct_time - time > 0)
        print(dial)
        path_finder.turn_dial(dial)
        path, time = path_finder.get_critical_path()
        if path == prev_path and (prev_time > correct_time > time or time > correct_time > prev_time):
            b = prev_time
            a = (time - prev_time) / (dial - prev_dial)
            dial = ((correct_time - b) / a) + prev_dial
            break
        prev_dial = dial
        prev_path, prev_time = path, time

    print(path_finder.get_critical_path(), dial)

    path_finder.turn_dial(dial)

    print(path_finder.get_critical_path(), dial)

    print(path_finder.top_order)