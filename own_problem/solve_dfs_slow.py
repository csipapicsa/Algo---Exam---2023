import sys
sys.path.insert(0, '..')

from objs import DfsSlow, BinarySearch

if __name__ == "__main__":
    path_finder = DfsSlow()


    while True:
        try:
            correct_time = int(input())

            path_finder.turn_dial(1000)
            time = path_finder.search()

            if correct_time > time:
                print(1000)
                continue

            path_finder.turn_dial(0)
            time = path_finder.search()

            if correct_time < time:
                print("Impossible")
                continue

            bs = BinarySearch(1000)

            time = path_finder.search()
            prev_path = None

            while abs(correct_time - time) > (correct_time / 10000):
                dial = bs.step(correct_time - time > 0)
                path_finder.turn_dial(dial)
                time = path_finder.search()


            
            #path_finder.turn_dial(dial)
            print(dial)
        except EOFError:
            break