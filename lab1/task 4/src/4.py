import time
import tracemalloc

def linear_search(numbers):
    for i in range(len(numbers)):
        if numbers[i] == x:
            return i + 1
    return -1


start_time = time.perf_counter()
tracemalloc.start()

with open("input.txt") as file:
    data = list(map(int, file.readline().split()))
    x = int(file.readline())

with open("output.txt", "w") as file:
    file.write(str(linear_search(data)))

print(f"Время работы: {time.perf_counter() - start_time} с")
print(f"Память: {tracemalloc.get_traced_memory()[1] / 2 ** 20} Мб")

