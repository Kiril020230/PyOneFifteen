inp = input("Введите строку, заканчивающуюся точкой: ")

if inp.endswith("."):
    inp = inp[:-1]

sp = inp.split()
len_sp = len(sp)

print("Количество слов в строке:", len_sp)