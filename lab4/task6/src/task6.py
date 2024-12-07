import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


from lab4.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.array = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        self.min_elem = float("inf")

    def __len__(self):
        return self.size

    def enqueue(self, elem):
        if self.size == len(self.array):
            self.resize(2 * len(self.array))
        available = (self.front + self.size) % len(self.array)
        self.array[available] = elem
        self.size += 1

        if self.min_elem > elem:
            self.min_elem = elem

    def dequeue(self):
        answer = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % len(self.array)
        self.size -= 1

        if self.min_elem == answer:
            self.min_elem = None
            if self.size > 0:
                self.min_elem = self.calculate_min()
        return answer

    def calculate_min(self):
        self.min_elem = float("inf")
        for elem in self.array:
            if elem is not None and elem < self.min_elem:
                self.min_elem = elem
        return self.min_elem

    def get_min(self):
        return self.min_elem

    def resize(self, capacity):
        old_array = self.array
        self.array = [None] * capacity
        walk = self.front
        for i in range(self.size):
            self.array[i] = old_array[walk]
            walk = (walk + 1) % len(old_array)
        self.front = 0

def complete_operations(operations):
    result = list()
    queue = ArrayQueue()
    for operation in operations:
        if "+" in operation:
            queue.enqueue(int(operation.split()[1]))
        elif "-" in operation:
            queue.dequeue()
        else:
            result.append(queue.get_min())
    return result

def task6():
    print("Задание №6")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    result = "\n".join(map(str, complete_operations(read_from_file(PATH_INPUT)[1:])))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task6()
