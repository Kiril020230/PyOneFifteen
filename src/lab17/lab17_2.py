import random

ekz = int(input("Количество экзаменов: "))

obj = input("Введите названия дисциплин через запятую и пробел: ").split(", ")

day = ["понедельник", "вторник", "среда", "четверг", "пятница"]
time = [9.0 + 0.5 * i for i in range(10)]

for i in range(ekz):
    days = random.choice(day)
    times = random.choice(time)
    ran = random.randint(1, 20)
    print(f"Экзамен по дисциплине «{obj[i]}» состоится в {days} время {times:.1f}. Ваш счастливый билет N# {ran}.")