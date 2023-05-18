from objs import PathFinder, BinarySearch
from matplotlib import pyplot as plt 

if __name__ == "__main__":
    path_finder = PathFinder()

    correct_time = int(input())

    bs = BinarySearch(1000)

    path, time = path_finder.get_critical_path()
    prev_path = None

    while abs(correct_time - time) > 0.01:
        dial = bs.step(correct_time - time > 0)
        print(dial)
        path_finder.turn_dial(dial)
        path, time = path_finder.get_critical_path()
        #if path == prev_path and (time > correct_time > prev_time or time < correct_time < prev_time):
        #    a = (prev_time - time) / (prev_dial - dial)
        #    dial = ((correct_time - time) / a) + dial
        #    break
        prev_dial = dial
        prev_path, prev_time = path, time

    path_finder.turn_dial(dial)
    print(path_finder.get_critical_path(), dial)

    #crit_lens = []
    #for j in range(1000):
    #    path_finder.turn_dial(j)
    #    crit_lens.append(path_finder.get_critical_path()[1])
#
    #plt.plot(crit_lens)
#
    #plt.show()