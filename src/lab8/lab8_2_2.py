inp = input("Введите текст на английском: ")
sp = inp.split()
f_n = 0

for num in sp:
    if num.startswith('b') or num.startswith('B'):
        f_n += 1

print("Количество слов, начинающихся с 'b':", f_n)