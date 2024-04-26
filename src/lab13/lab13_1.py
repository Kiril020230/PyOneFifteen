inp1 = input("Введите номера слов через пробел: ").split()
inp2 = input("Введите слова через пробел: ").split()

changes = ' '.join(inp2[int(index) - 1] for index in inp1 if index.isdigit())
changes = changes.capitalize()

print("Новое предложение:", changes)