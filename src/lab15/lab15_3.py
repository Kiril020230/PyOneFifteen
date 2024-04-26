def listArr(numbers, a, b, c):
    fil = [num for num in numbers if a < num < b and num % c == 0]
    suma = sum(num for num in numbers if num not in fil)
    return fil, suma

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
a, b, c = map(int, input("Введите три числа a, b, c через пробел: ").split())

filtered_numbers, other_numbers_sum = listArr(numbers, a, b, c)
print("Элементы, которые одновременно больше {}, меньше {} и делятся на {} без остатка:".format(a, b, c), filtered_numbers)
print("Сумма остальных элементов списка:", other_numbers_sum)