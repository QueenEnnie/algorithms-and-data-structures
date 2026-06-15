import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


from lab4.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


class LinkedQueue:
    __slots__ = ("head", "tail", "size")

    class Node:
        __slots__ = ("elem", "next_elem")

        def __init__(self, elem, next_elem):
            self.elem = elem
            self.next_elem = next_elem

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, elem):
        newest = self.Node(elem, None)
        if self.size == 0:
            self.head = newest
        else:
            self.tail.next_elem = newest
        self.tail = newest
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return "queue is empty"
        answer = self.head.elem
        self.head = self.head.next_elem
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return answer


def complete_operations(operations):
    result = list()
    queue = LinkedQueue()
    for operation in operations:
        if "+" in operation:
            queue.enqueue(int(operation.split()[1]))
        else:
            result.append(queue.dequeue())
    return result

def task13_2():
    print("Задание №13.2")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    operations = read_from_file(PATH_INPUT)[1:]
    result = "\n".join(map(str, complete_operations(operations)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)



if __name__ == "__main__":
    task13_2()
