import time
import memory_profiler


def read_from_file(path):
    with open(path, "r", encoding="utf-8") as file:
        data = file.readlines()
    return data


def write_in_file(data,path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)


def start_time_memory():
    start_time = time.perf_counter()
    start_memory = memory_profiler.memory_usage()[0]
    return start_time, start_memory


def print_time_memory(name, start_time, start_memory):
    print(f"Название теста: {name}")
    print(f"Время работы: {time.perf_counter() - start_time} с")
    print(f"Память: {memory_profiler.memory_usage()[0] - start_memory} Мб", "\n")



