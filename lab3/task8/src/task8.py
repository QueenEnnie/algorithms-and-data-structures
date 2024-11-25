from lab3.utils import *
from math import sqrt
from random import randint

def three_way_partition(array, left_index, right_index):
    pivot = array[left_index][0]
    less_than = left_index
    greater_than = right_index
    indicator = left_index

    while indicator <= greater_than:
        if array[indicator][0] < pivot:
            array[less_than], array[indicator] = array[indicator], array[less_than]
            less_than += 1
            indicator += 1
        elif array[indicator][0] > pivot:
            array[indicator], array[greater_than] = array[greater_than], array[indicator]
            greater_than -= 1
        else:
            indicator += 1
    return less_than, greater_than

def randomized_quick_sort(array, left_index, right_index):
    if left_index < right_index:
        index = randint(left_index, right_index)
        array[left_index], array[index] = array[index], array[left_index]
        less_than, greater_than = three_way_partition(array, left_index, right_index)
        randomized_quick_sort(array, left_index, less_than - 1)
        randomized_quick_sort(array, greater_than + 1, right_index)

def task8():
    data = read_from_file()
    number_out = int(data[0].split()[1])
    coordinates = [(int(elem.split()[0]), int(elem.split()[1])) for elem in data[1:]]
    distance_coordinates = [[sqrt(x ** 2 + y ** 2), (x, y)] for x, y in coordinates]
    randomized_quick_sort(distance_coordinates, 0, len(distance_coordinates) - 1)
    out = [f"[{elem[1][0]},{elem[1][1]}]" for elem in distance_coordinates[:number_out]]
    write_in_file(",".join(out))

if __name__ == "__main__":
    task8()
