nun = int(input("Введите количество оценок: "))
arr = []

print("Введите оценки:")
for i in range(nun):
    grade = float(input())
    arr.append(grade)

print("Введенные оценки:")
for grade in arr:
    print(grade)

# Вычисление средней оценки
average_grade = sum(arr) / nun
print("Средняя оценка за урок:", average_grade)