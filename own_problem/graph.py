from matplotlib import pyplot as plt

from classes import CriticalPath

path_finder = CriticalPath()

path_lengths = []

for i in range(1001):
    path_finder.turn_dial(i)
    path_lengths.append(path_finder.get_time())

plt.plot(path_lengths)
plt.yticks([0, 5, 10, 15, 20, 25, 30])
plt.ylabel("Time to complete all steps")
plt.xlabel("Dial value")
plt.show()