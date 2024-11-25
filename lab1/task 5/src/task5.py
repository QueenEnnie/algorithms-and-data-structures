from lab1.utils import *



def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        mini = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[mini]:
                mini = j
        numbers[i], numbers[mini] = numbers[mini], numbers[i]
    return numbers


def task5():
    data = list(map(int, read_from_file()[1].split()))
    write_in_file(" ".join(map(str, selection_sort(data))))


if __name__ == "__main__":
    task5()
