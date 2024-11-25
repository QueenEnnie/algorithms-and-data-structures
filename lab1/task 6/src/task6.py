from lab1.utils import *

def bubble_sort(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i + 1] < numbers[i]:
                numbers[i + 1], numbers[i] = numbers[i], numbers[i + 1]
                swapped = True
    return numbers

def task6():
    data = list(map(int, read_from_file()[1].split()))
    write_in_file(" ".join(map(str, bubble_sort(data))))


if __name__ == "__main__":
    task6()