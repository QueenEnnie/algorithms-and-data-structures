from lab1.utils import *


def insert_sort(numbers):
    for i in range(1, len(numbers)):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp < numbers[j]:
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j + 1] = temp
    return numbers


def task1():
    data = list(map(int, read_from_file()[1].split()))
    write_in_file(" ".join(map(str, insert_sort(data))))


if __name__ == "__main__":
    task1()