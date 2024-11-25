import time
import memory_profiler
from random import randint

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def read_from_file():
    with open(PATH_INPUT, "r", encoding="utf-8") as file:
        data = file.readlines()
    return data


def write_in_file(data):
    with open(PATH_OUTPUT, "w", encoding="utf-8") as file:
        file.write(data)


def start_time_memory():
    start_time = time.perf_counter()
    start_memory = memory_profiler.memory_usage()[0]
    return start_time, start_memory


def print_time_memory(name, start_time, start_memory):
    print(f"Название теста: {name}")
    print(f"Время работы: {time.perf_counter() - start_time} с")
    print(f"Память: {memory_profiler.memory_usage()[0] - start_memory} Мб", "\n")


def quicksort_with_key(array, begin, end, k=0):
    if begin >= end:
        return
    pivot = array[end]
    left_i, right_i = begin, end - 1
    while left_i <= right_i:
        while left_i <= right_i and array[left_i][k] < pivot[k]:
            left_i += 1
        while left_i <= right_i and pivot[k] < array[right_i][k]:
            right_i -= 1
        if left_i <= right_i:
            array[left_i], array[right_i] = array[right_i], array[left_i]
            left_i, right_i = left_i + 1, right_i - 1
    array[left_i], array[end] = array[end], array[left_i]
    quicksort_with_key(array, begin, left_i - 1, k)
    quicksort_with_key(array, left_i + 1, end, k)

