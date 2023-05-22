from classes import CriticalPath
from functions import search_analytic, check_limits

path_finder = CriticalPath()


while True:
    try:
        correct_time = int(input())
        if check_limits(path_finder, correct_time):
            continue
        dial = search_analytic(path_finder, correct_time)
        print(correct_time)
        print(dial)
    except EOFError:
        break