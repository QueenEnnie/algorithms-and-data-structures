from utils import *

def majority(array):
    candidate, count = None, 0
    for elem in array:
        if count == 0:
            candidate = elem
        count += (1 if elem == candidate else -1)

    if len([1 for elem in array if elem == candidate]) > len(array) // 2:
        return 1
    return 0


def task5():
    data = list(map(int, read_from_file()[1].split()))
    write_in_file(str(majority(data)))


if __name__ == "__main__":
    task5()
