a = [int(input(f"Введите элемент {i + 1}: ")) for i in range(20)]
sum_l = sum(1 for x in a if x < 0)

print("Количество отрицательных элементов в списке:", sum_l)