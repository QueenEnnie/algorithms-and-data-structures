import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


from lab4.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


class LinkedStack:
    class Node:
        def __init__(self, elem, next_elem):
            self.elem = elem
            self.next_elem = next_elem

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, elem):
        self.head = self.Node(elem, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return "stack is empty" # ????!!!!
        answer = self.head.elem
        self.head = self.head.next_elem
        self.size -= 1
        return answer


def complete_operations(operations):
    result = list()
    stack = LinkedStack()
    for operation in operations:
        if "+" in operation:
            stack.push(int(operation.split()[1]))
        else:
            result.append(stack.pop())
    return result

def task13_1():
    print("Задание №13.1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    operations = read_from_file(PATH_INPUT)[1:]
    result = "\n".join(map(str, complete_operations(operations)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)



if __name__ == "__main__":
    task13_1()
