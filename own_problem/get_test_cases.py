from objs import PathFinder
from sys import argv
import random

def get_range():
    path_finder = PathFinder()
    high = path_finder.get_critical_path()[1]
    path_finder.turn_dial(0.00001)
    low = path_finder.get_critical_path()[1]
    return low, high


low, high = get_range()
print(low, high)
with open(argv[1], 'a') as file:
    for _ in range(1000):
        file.write(str(random.randint(int(low), int(high))))
        file.write('\n')