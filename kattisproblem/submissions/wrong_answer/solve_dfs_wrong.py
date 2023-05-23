from classes import DfsWrong
from functions import search, check_limits

path_finder = DfsWrong()

while True:
    try:
        correct_time = int(input())
        if check_limits(path_finder, correct_time):
            continue
        
        dial = search(path_finder, correct_time)
        print(dial)
    except EOFError:
        break