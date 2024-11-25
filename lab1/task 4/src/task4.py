from lab1.utils import *
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i + 1
    return -1


def task4():
    data = read_from_file()
    array = list(map(int, data[0].split()))
    target = int(data[1])
    write_in_file(str(linear_search(array, target)))


if __name__ == "__main__":
    task4()
