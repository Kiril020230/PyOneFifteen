arr = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
start, end = map(int, input("Введите начальный и конечный номера интервала (через пробел): ").split())
suma = sum(arr[start:end+1])

print("Сумма чисел в интервале:", suma)