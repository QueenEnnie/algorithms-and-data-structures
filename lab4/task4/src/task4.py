import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import read_from_file, write_in_file
from lab4.task1.src.task1 import ArrayStack


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def check_brackets(string):
    stack = ArrayStack()
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    for index, char in enumerate(string):
        if char in "([{":
            stack.push((char, index + 1))
        elif char in ")]}":
            if not stack.array:
                return index + 1
            top_elem = stack.pop()
            if top_elem[0] != bracket_pairs[char]:
                return index + 1
    if stack.array:
        return stack.pop()[1]
    return "Success"

def task4():
    print("Задание №4")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)[0]
    result = str(check_brackets(data))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)

if __name__ == "__main__":
    task4()
