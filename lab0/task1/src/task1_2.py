import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


def new_addition(a, b):
    return a + b ** 2


def task1_2():
    print("Задание №1.2")
    a, b = map(int, input("Введите два целых числа a и b: ").split())
    print("Входные данные:")
    print(f"{a} {b}")
    result = str(new_addition(a, b))
    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1_2()
