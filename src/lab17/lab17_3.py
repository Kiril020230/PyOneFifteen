import datetime

day = int(input("Количество дней до экзамена: "))
date = datetime.datetime.now() + datetime.timedelta(days=day)

print("Дата экзамена:", date.strftime("%d.%m"))