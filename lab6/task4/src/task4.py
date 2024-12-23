import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


class AssociativeMap:
    def __init__(self):
        self.data = {}
        self.order = []

    def get(self, x):
        return self.data.get(x, None)

    def previous(self, x):
        if x in self.data:
            if self.order.index(x) != 0:
                return self.data[self.order[self.order.index(x) - 1]]
        return None

    def next(self, x):
        if x in self.data:
            if self.order.index(x) + 1 < len(self.data):
                return self.data[self.order[self.order.index(x) + 1]]
        return None

    def put(self, x, y):
        if x in self.data:
            self.data[x] = y
        else:
            self.data[x] = y
            self.order.append(x)

    def delete(self, x):
        if x in self.data:
            del self.data[x]
            self.order.remove(x)

def complete_operations(operations):
    result = []
    associative_map = AssociativeMap()
    for elem in operations:
        if "get" in elem:
            value = associative_map.get(elem.split()[1])
            result.append(value if value else "<none>")
        elif "prev" in elem:
            value = associative_map.previous(elem.split()[1])
            result.append(value if value else "<none>")
        elif "next" in elem:
            value = associative_map.next(elem.split()[1])
            result.append(value if value else "<none>")
        elif "put" in elem:
            associative_map.put(elem.split()[1], elem.split()[2])
        elif "delete" in elem:
            associative_map.delete(elem.split()[1])
    return result


def task4():
    print("Задание №4")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    operations = [elem.strip() for elem in read_from_file(PATH_INPUT)[1:]]
    result = "\n".join(map(str, complete_operations(operations)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task4()
