import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))




def complete_operations(operations):
    result = []
    phone_book = {}
    for elem in operations:
        if "add" in elem:
            phone_book[elem.split()[1]] = elem.split()[2]
        elif "del" in elem:
            phone_book.pop(elem.split()[1], "")
        else:
            result.append(phone_book[elem.split()[1]]
                          if elem.split()[1] in phone_book else "not found")
    return result



def task2():
    print("Задание №2")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    operations = [elem.strip() for elem in read_from_file(PATH_INPUT)[1:]]
    result = "\n".join(map(str, complete_operations(operations)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task2()
