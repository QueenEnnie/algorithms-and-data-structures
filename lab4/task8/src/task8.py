import os, sys, random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import read_from_file, write_in_file
PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def calculate_postfix(math_expression):
    stack = []
    push = stack.append
    pop = stack.pop
    for elem in math_expression:
        if elem.isdigit():
            push(int(elem))
        else:
            second = pop()
            first = pop()
            if elem == '+':
                push(first + second)
            elif elem == '-':
                push(first - second)
            elif elem == '*':
                push(first * second)
    return pop()

def task8():
    print("Задание №8")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)[1].split()
    result = str(calculate_postfix(data))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task8()
