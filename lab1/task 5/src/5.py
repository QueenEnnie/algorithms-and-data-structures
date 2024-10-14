import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

with open("input.txt") as file:
    numbers = list(map(int, file.readlines()[1].split()))

for i in range(len(numbers) - 1):
    mini = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[mini]:
            mini = j
    numbers[i], numbers[mini] = numbers[mini], numbers[i]


with open("output.txt", "w") as file:
    file.write(" ".join(map(str, numbers)))

print(f"Время работы: {time.perf_counter() - start_time} с")
print(f"Память: {tracemalloc.get_traced_memory()[1] / 2 ** 20} Мб")
