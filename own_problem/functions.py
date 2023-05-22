from classes import BinarySearch

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