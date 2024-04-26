b = [int(input(f"Введите элемент {i+1}: ")) for i in range(20)]
sum_l = sum(num for num in b if num > 0)

print("Сумма положительных элементов в списке B:", sum_l)