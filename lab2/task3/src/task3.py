from lab2.utils import *


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers, 0

    middle = len(numbers) // 2
    left_half, left_inversions = merge_sort(numbers[:middle])
    right_half, right_inversions = merge_sort(numbers[middle:])
    merged, inversions = merge_and_count_inversions(left_half, right_half)
    return merged, (left_inversions + right_inversions + inversions)


def merge_and_count_inversions(left, right):
    new = [0 for _ in range(len(right) + len(left))]
    left_index, right_index, new_index = 0, 0, 0
    inversions = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            new[new_index] = left[left_index]
            left_index += 1
        else:
            new[new_index] = right[right_index]
            inversions += len(left) - left_index
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
    return new, inversions


def task3():
    data = list(map(int, read_from_file()[1].split()))
    write_in_file(str(merge_sort(data)[1]))


if __name__ == "__main__":
    task3()
