import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from collections import deque
from lab4.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))

def calculating_max(array, window_size):
    dequeue_indexes = deque()
    result = []
    for i in range(len(array)):
        if dequeue_indexes and dequeue_indexes[0] < i - window_size + 1:
            dequeue_indexes.popleft()
        while dequeue_indexes and array[dequeue_indexes[-1]] < array[i]:
            dequeue_indexes.pop()
        dequeue_indexes.append(i)
        if i >= window_size - 1:
            result.append(array[dequeue_indexes[0]])
    return result


def task7():
    print("Задание №7")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    sequence_ = list(map(int, data[1].split()))
    window_size = int(data[2])
    result = " ".join(map(str, calculating_max(sequence_, window_size)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task7()

