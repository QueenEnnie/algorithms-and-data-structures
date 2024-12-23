import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import read_from_file, write_in_file

PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def sort_land(numbers):
    for i in range(len(numbers)):
        numbers[i] = [i + 1, numbers[i]]

    for i in range(1, len(numbers)):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp[1] < numbers[j][1]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = temp

    return numbers[0][0], numbers[len(numbers) // 2][0], numbers[-1][0]


def task7():
    print("Задание №7")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = list(map(float, read_from_file(PATH_INPUT)[1].split()))
    result = " ".join(map(str, sort_land(data)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)

if __name__ == "__main__":
    task7()
