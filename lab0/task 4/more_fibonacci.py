import time


def fib(n):
    previous_last, last = 0, 1
    for _ in range(n):
        previous_last, last = last % 10, (last + previous_last) % 10
    return previous_last

start_time = time.perf_counter()

with open("input.txt") as file:
    number = int(file.read())
if 0 <= number <= 10 ** 7:
    with open("output.txt", "w") as file:
        file.write(str(fib(number)))
else:
    print("Данные не соответствуют условию задачи. "
          "Пожалуйста, занесите в файл корректные данные.")

print(f"Время работы: {time.perf_counter() - start_time}")