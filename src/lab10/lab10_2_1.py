inp = input("Введите последовательность символов: ")
digit = {char for char in inp if char.isdigit()}

print("Множество цифр, встречающихся в последовательности:", digit)