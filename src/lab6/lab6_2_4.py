ou = float(input("Введите размер стипендии: "))
ou2 = float(input("Введите расходы в месяц: "))

full = ou + ou2

for num in range(2, 11):
    ou2 *= 1.03 
    full += ou + ou2

print("Сумма денег, необходимая на 10 месяцев:", full, "руб.")