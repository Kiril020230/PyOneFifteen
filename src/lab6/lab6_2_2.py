n = 15
sum = 0
numb = 1

for num in range(n):
    number = float(input(f"Введите число {num + 1}: "))
    sum += number
    numb *= number

print("Сумма введенных чисел:", sum)
print("Произведение введенных чисел:", numb)