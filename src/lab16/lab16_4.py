numbers = [32, -3, 44, -5, 6, -7, 8, -19]
sum = 0

for number in numbers:
    if number < 0:
        sum += number ** 3

print("Сумма кубов отрицательных чисел:", sum)
