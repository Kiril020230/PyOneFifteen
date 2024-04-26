def ff_ma(numbers):
    if not numbers:
        print("0")
    else:
        average = sum(numbers) / len(numbers)
        print("Среднее значение:", average)

numbers = list(map(int, input("Введите список целых чисел, разделенных пробелами: ").split()))
ff_ma(numbers)