from lab2.utils import *

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def task4():
    data = read_from_file()
    array = list(map(int, data[1].split()))
    find_array = list(map(int, data[3].split()))
    result = [binary_search(array, elem) for elem in find_array]
    write_in_file(" ".join(map(str, result)))


if __name__ == "__main__":
    task4()
