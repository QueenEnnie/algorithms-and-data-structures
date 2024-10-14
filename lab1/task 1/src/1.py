import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

with open("input.txt") as file:
    numbers = list(map(int, file.readlines()[1].split()))

for i in range(1, len(numbers)):
    temp = numbers[i]
    j = i - 1
    while j >= 0 and temp < numbers[j]:
        numbers[j + 1] = numbers[j]
        j = j - 1
    numbers[j + 1] = temp

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, numbers)))

print(f"Время работы: {time.perf_counter() - start_time} с")
print(f"Память: {tracemalloc.get_traced_memory()[1] / 2 ** 20} Мб")
