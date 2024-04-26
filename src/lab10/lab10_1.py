in1 = set(map(int, input("Введите элементы первого множества через пробел: ").split()))
in2 = set(map(int, input("Введите элементы второго множества через пробел: ").split()))

union = in1.union(in2)
sort = sorted(in1.intersection(in2))

print("Числа в двух множествах(не повтор.):", union)
print("Числа, входящие в оба множества (в порядке возрастания):", sort)