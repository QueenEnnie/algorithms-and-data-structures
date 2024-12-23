import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        mini = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[mini]:
                mini = j
        numbers[i], numbers[mini] = numbers[mini], numbers[i]
    return numbers


def task5():
    print("Задание №5")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = list(map(int, read_from_file(PATH_INPUT)[1].split()))
    result = " ".join(map(str, selection_sort(data)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task5()
