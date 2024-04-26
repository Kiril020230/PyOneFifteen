inp = int(input("Введите количество специальностей: "))
speec = {}
for i in range(inp):
    specialty_info = input().split('-')
    specialty = specialty_info[0]
    groups = specialty_info[1].split(',')
    speec[specialty] = groups

group = input("Введите номер группы: ")
for specialty, groups in speec.items():
    if group in groups:
        print(specialty)
        break
else:
    print()