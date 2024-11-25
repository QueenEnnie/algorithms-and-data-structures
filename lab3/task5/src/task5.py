from lab3.utils import read_from_file, write_in_file
from lab3.task1.src.task1 import randomized_quick_sort


def find_h_index(array):
    randomized_quick_sort(array, 0, len(array) - 1)
    h_index = 0
    for index, number in enumerate(array[::-1]):
        if number >= index + 1:
            h_index = index + 1
        else:
            break
    return h_index


def task5():
    data = list(map(int, read_from_file()[0].split(",")))
    write_in_file(str(find_h_index(data)))


if __name__ == "__main__":
    task5()
