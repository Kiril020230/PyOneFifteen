inp = input("Введите строку: ")
maxi = max(inp.lower().count(char) for char in inp.lower() if char.isalpha())

print("Максимальное количество встречающихся букв:", maxi)