def fib(n):
    previous_last, last = 0, 1
    for _ in range(n):
        previous_last, last = last, last + previous_last
    return previous_last


with open("input.txt") as file:
    number = int(file.read())
if 0 <= number <= 45:
    with open("output.txt", "w") as file:
        file.write(str(fib(number)))
else:
    print("Данные не соответствуют условию задачи. "
          "Пожалуйста, занесите в файл корректные данные.")
