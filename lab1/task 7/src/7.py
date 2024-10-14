import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

with open("input.txt") as file:
    numbers = list(map(float, file.readlines()[1].split()))

for i in range(len(numbers)):
    numbers[i] = [i + 1, numbers[i]]

for i in range(1, len(numbers)):
    temp = numbers[i]
    j = i - 1
    while j >= 0 and temp[1] < numbers[j][1]:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = temp

the_poorest = numbers[0][0]
average = numbers[len(numbers) // 2][0]
the_richest = numbers[-1][0]

with open("output.txt", "w") as file:
    file.write(" ".join([str(the_poorest), str(average), str(the_richest)]))

print(f"Время работы: {time.perf_counter() - start_time} с")
print(f"Память: {tracemalloc.get_traced_memory()[1] / 2 ** 20} Мб")
