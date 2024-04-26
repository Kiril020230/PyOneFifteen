inp = int(input("Введите количество номеров телефонов: "))
cont = {}

print("Введите номера телефонов и имена их владельцев:")
for _ in range(inp):
    phone, name = input().split()
    cont[name] = phone

iis = input("Введите имя, чей телефон нужно найти: ")
if iis in cont:
    print(f"Номер телефона {iis}: {cont[iis]}")
else:
    print("Такое имя отсутствует в телефонной книге.")