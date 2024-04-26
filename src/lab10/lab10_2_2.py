inp = input("Введите последовательность символов: ")
ch = set()

for char in inp:
    if char.isalpha():
        if char >= 'A' and char <= 'Z' or char >= '0' and char <= '5':
            ch.add(char)

print("Множество букв и цифр:", ch)