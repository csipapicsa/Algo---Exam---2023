from objs import BinarySearch, PathFinder

if __name__ == "__main__":
    path_finder = PathFinder()
    print(path_finder.get_critical_path())
    path_finder.turn_dial(0.00001)
    print(path_finder.get_critical_path())