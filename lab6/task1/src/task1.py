import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab6.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


class CustomHashSet:
    def __init__(self, capacity=5 * 10 ** 5):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return key % self.capacity

    def add(self, key):
        hashed_elem = self._hash(key)
        if key not in self.table[hashed_elem]:
            self.table[hashed_elem].append(key)

    def remove(self, key):
        hashed_elem = self._hash(key)
        if key in self.table[hashed_elem]:
            self.table[hashed_elem].remove(key)

    def contains(self, key):
        hashed_elem = self._hash(key)
        return key in self.table[hashed_elem]


def complete_operations(operations):
    result = []
    hash_set = CustomHashSet()
    for i in range(len(operations)):
        if "A" in operations[i]:
            hash_set.add(int(operations[i].split()[1]))
        elif "D" in operations[i]:
            hash_set.remove(int(operations[i].split()[1]))
        elif "?" in operations[i]:
            result.append("Y" if hash_set.contains(int(operations[i].split()[1])) else "N")
    return result



def task1():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    operations = [elem.strip() for elem in read_from_file(PATH_INPUT)[1:]]
    result = "\n".join(map(str, complete_operations(operations)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1()
