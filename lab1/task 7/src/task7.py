from lab1.utils import *


def sort_land(numbers):
    for i in range(len(numbers)):
        numbers[i] = [i + 1, numbers[i]]

    for i in range(1, len(numbers)):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp[1] < numbers[j][1]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = temp

    return numbers[0][0], numbers[len(numbers) // 2][0], numbers[-1][0]


def task7():
    data = list(map(float, read_from_file()[1].split()))
    write_in_file(" ".join(map(str, sort_land(data))))


if __name__ == "__main__":
    task7()
