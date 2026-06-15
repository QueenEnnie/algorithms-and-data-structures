import time
import random

try:
    import memory_profiler
except ImportError:
    memory_profiler = None


def _memory_usage():
    if memory_profiler is None:
        return 0
    return memory_profiler.memory_usage()[0]


def generate_segments(n, min_value=-10 ** 8, max_value=10 ** 8):
    segments = []
    for _ in range(n):
        a = random.randint(min_value, max_value)
        b = random.randint(a, max_value)
        segments.append((a, b))
    return segments


def read_from_file(path):
    with open(path, "r", encoding="utf-8") as file:
        data = file.readlines()
    return data


def write_in_file(data,path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)


def start_time_memory():
    start_time = time.perf_counter()
    start_memory = _memory_usage()
    return start_time, start_memory


def end_time_memory(start_time, start_memory):
    end_time = time.perf_counter() - start_time
    end_memory = _memory_usage() - start_memory
    return end_time, end_memory

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

