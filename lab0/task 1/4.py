with open("input.txt") as file:
    a, b = map(int, file.read().split())
if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
    with open("output.txt", "w") as file:
        file.write(str(a + b ** 2))
else:
    print("Данные числа не соответствуют условию задачи. "
          "Пожалуйста, занесите в файл корректные данные.")

