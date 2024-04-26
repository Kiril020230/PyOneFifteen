inp = int(input("количесиво студентов"))
students = {}
for _ in range(inp):
    last_name, specialty, group = input().split()
    if specialty not in students:
        students[specialty] = []
    students[specialty].append(last_name)

query = input()
if query in students:
    print(','.join(students[query]))
else:
    print("Проверьте запрос")