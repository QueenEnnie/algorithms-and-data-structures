from lab2.utils import *


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    middle = len(numbers) // 2
    left_half = merge_sort(numbers[:middle])
    right_half = merge_sort(numbers[middle:])
    return merge(left_half, right_half)


def merge(left, right):
    new = [0 for _ in range(len(right) + len(left))]
    left_index, right_index, new_index = 0, 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            new[new_index] = left[left_index]
            left_index += 1
        else:
            new[new_index] = right[right_index]
            right_index += 1
        new_index += 1

    while left_index < len(left):
        new[new_index] = left[left_index]
        left_index += 1
        new_index += 1

    while right_index < len(right):
        new[new_index] = right[right_index]
        right_index += 1
        new_index += 1
    return new


def task1():
    data = list(map(int, read_from_file()[1].split()))
    write_in_file(" ".join(map(str, merge_sort(data))))


if __name__ == "__main__":
    task1()
