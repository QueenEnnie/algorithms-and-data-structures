from lab3.utils import *
from lab3.task1.src.task1 import randomized_quick_sort
from random import randint

def scarecrow_sort(array, step):
    groups = [[] for _ in range(step)]
    for i in range(len(array)):
        groups[i % step].append(array[i])
    sorted_groups = []
    for elem in groups:
        randomized_quick_sort(elem, 0 , len(elem) - 1)
        sorted_groups.append(elem)
    sorted_array = []
    indices = [0] * step
    for i in range(len(array)):
        sorted_array.append(groups[i % step][indices[i % step]])
        indices[i % step] += 1
    for i in range(len(sorted_array) - 1):
        if not sorted_array[i] <= sorted_array[i + 1]:
            return False
    return True

def task1():
    data = read_from_file()
    step = int(data[0].split()[1])
    numbers = list(map(int, data[1].split()))
    result = "ДА" if scarecrow_sort(numbers, step) else "НЕТ"
    write_in_file(result)


if __name__ == "__main__":
    task1()
