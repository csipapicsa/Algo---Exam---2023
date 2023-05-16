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