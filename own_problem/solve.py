from objs import PathFinder, BinarySearch
from matplotlib import pyplot as plt 

if __name__ == "__main__":
    path_finder = PathFinder()


    while True:
        try:
            correct_time = int(input())


            path_finder.turn_dial(1000)
            path, time = path_finder.get_critical_path()

            if correct_time > time:
                print(1000)
                continue

            path_finder.turn_dial(0)
            path, time = path_finder.get_critical_path()

            if correct_time < time:
                print("Impossible")
                continue

            bs = BinarySearch(1000)

            path, time = path_finder.get_critical_path()
            prev_path = None

            while abs(correct_time - time) > 0.01:
                dial = bs.step(correct_time - time > 0)
                path_finder.turn_dial(dial)
                path, time = path_finder.get_critical_path()
                if path == prev_path and (time > correct_time > prev_time or time < correct_time < prev_time):
                    a = (prev_time - time) / (prev_dial - dial)
                    dial = ((correct_time - time) / a) + dial
                    break
                prev_dial = dial
                prev_path, prev_time = path, time

            #path_finder.turn_dial(dial)
            #print(path_finder.get_critical_path()[1])
            print(dial)
        except EOFError:
            break