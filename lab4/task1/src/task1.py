import os

from lab4.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


class ArrayStack:
    def __init__(self):
        self.array = []

    def push(self, elem):
        self.array.append(elem)

    def pop(self):
        return self.array.pop()

def task1():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    result = list()
    stack = ArrayStack()
    for operation in read_from_file(PATH_INPUT)[1:]:
        if "+" in operation:
            stack.push(int(operation.split()[1]))
        else:
            result.append(stack.pop())
    result = "\n".join(map(str, result))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1()
