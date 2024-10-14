import time
import tracemalloc

def bubble_sort(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i + 1] < numbers[i]:
                numbers[i + 1], numbers[i] = numbers[i], numbers[i + 1]
                swapped = True
    return numbers


start_time = time.perf_counter()
tracemalloc.start()

with open("input.txt") as file:
    data = list(map(int, file.readlines()[1].split()))

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, bubble_sort(data))))

print(f"Время работы: {time.perf_counter() - start_time} с")
print(f"Память: {tracemalloc.get_traced_memory()[1] / 2 ** 20} Мб")
