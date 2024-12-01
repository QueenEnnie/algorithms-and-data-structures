import os

from lab4.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self.array = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        # self.mini =

    def __len__(self):
        return self.size

    def enqueue(self, elem):
        if self.size == len(self.array):
            self.resize(2 * len(self.array))
        available = (self.front + self.size) % len(self.array)
        self.array[available] = elem
        self.size += 1

    def dequeue(self):
        answer = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % len(self.array)
        self.size -= 1
        return answer

    def resize(self, capacity):
        old = self.array
        self.array = [None] * capacity
        walk = self.front
        for i in range(self.size):
            self.array[i] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0

def task6():
    print("Задание №6")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    result = list()
    # stack = ArrayStack()
    # for operation in read_from_file(PATH_INPUT)[1:]:
    #     if "+" in operation:
    #         stack.push(int(operation.split()[1]))
    #     else:
    #         result.append(stack.pop())
    result = "\n".join(map(str, result))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task6()
