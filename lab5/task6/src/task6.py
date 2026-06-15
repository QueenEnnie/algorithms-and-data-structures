import os, sys
import heapq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab5.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


class HeapPriorityQueue:
    def __init__(self):
        self.array = []
        self.index_map = {}

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * (i + 1) - 1

    def right_child(self, i):
        return 2 * (i + 1)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
        self.index_map[self.array[i].value] = j
        self.index_map[self.array[j].value] = i

    def has_left(self, i):
        return self.left_child(i) < len(self.array)

    def has_right(self, i):
        return self.right_child(i) < len(self.array)

    def up_heap(self, i):
        parent = self.parent(i)
        if i > 0 and self.array[i]  < self.array[parent]:
            self.swap(i, parent)
            self.up_heap(parent)

    def down_heap(self, i):
        if self.has_left(i):
            left = self.left_child(i)
            small_child = left
            if self.has_right(i):
                right = self.right_child(i)
                if self.array[right] < self.array[left]:
                    small_child = right
            if self.array[small_child] < self.array[i]:
                self.swap(i, small_child)
                self.down_heap(small_child)

    def add(self, key, value):
        self.index_map[value] = key
        heapq.heappush(self.array, (key, value))

    def remove_min(self):
        while self.array:
            key, value = heapq.heappop(self.array)
            if self.index_map.get(value) == key:
                self.index_map[value] = None
                return key
        return "*"

    def reduce(self, value, new_key):
        if self.index_map.get(value) is not None:
            self.index_map[value] = new_key
            heapq.heappush(self.array, (new_key, value))



def complete_operations(operations):
    result = []
    priority_queue = HeapPriorityQueue()
    for i in range(len(operations)):
        if "A" in operations[i]:
            priority_queue.add(int(operations[i].split()[1]), i + 1)
        elif "X" in operations[i]:
            result.append(priority_queue.remove_min())
        elif "D" in operations[i]:
            value, new_key = int(operations[i].split()[1]), int(operations[i].split()[2])
            priority_queue.reduce(value, new_key)
    return result


def task6():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))
    operations = [elem.strip() for elem in read_from_file(PATH_INPUT)[1:]]
    result = "\n".join(map(str, complete_operations(operations)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task6()
