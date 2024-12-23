import os
import sys
import heapq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))

def american_election(data):
    presidents = {}
    for string in data:
        if string.split()[0] in presidents:
            presidents[string.split()[0]] += int(string.split()[1])
        else:
            presidents[string.split()[0]] = int(string.split()[1])
    return [[key, value] for key, value
            in sorted(presidents.items(), key=lambda x:x[0])]


def task5():
    print("Задание №5")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    result = "\n".join([" ".join(map(str, elem)) for elem in american_election(read_from_file(PATH_INPUT))])
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task5()
