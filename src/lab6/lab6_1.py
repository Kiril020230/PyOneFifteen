import math
k = int(input("Введите число k: "))

for num in range(k+1):
    sqrt_n = math.sqrt(num)
    row = num ** 3
    print(f"Корень числа {num} равен {sqrt_n}, а куб равен {row}")