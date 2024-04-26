inp = input("Введите строку с несколькими словами: ")
sh  = '-'.join(word.upper() for word in inp.split())

print("Преобразованная строка:", sh)