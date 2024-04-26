inp = input("Введите последовательность символов: ")
ch = set()

for char in inp:
    if char.isdigit():
        if char >= '5' and char <= '9':
            ch.add(char)
    elif char in ['+', '-', '*', '/']:
        ch.add(char)

print("Множество цифр и знаков арифметических операций:", ch)