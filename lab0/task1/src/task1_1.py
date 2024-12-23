import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


def addition(a, b):
    return a + b


def task1_1():
    print("Задание №1.1")
    a, b = map(int, input("Введите два целых числа a и b: ").split())
    print("Входные данные:")
    print(f"{a} {b}")
    result = str(addition(a, b))
    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1_1()
