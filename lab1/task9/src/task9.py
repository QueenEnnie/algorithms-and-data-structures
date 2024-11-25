from lab2.utils import *

def binary_addition(first, second):
    first = list(map(int, first.zfill(max(len(first), len(second)))))
    second = list(map(int, second.zfill(max(len(first), len(second)))))
    new, save = [], 0
    for i in range(len(first) - 1, -1, -1):
        new += [(first[i] + second[i] + save) % 2]
        save = 1 if (first[i] + second[i] + save) // 2 > 0 else 0
    if save:
        new += [save]
    return new[::-1]

def task9():
    first_number, second_number = read_from_file()[0].split()
    write_in_file("".join(map(str, binary_addition(first_number, second_number))))


if __name__ == "__main__":
    task9()

