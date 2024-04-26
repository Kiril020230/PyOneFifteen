k = 3
full = 0

for num in range(1000, 10000):# до 9999
    if num % k == 0:
        full += num

print("Сумма всех 4-значных чисел, кратных", k, ":", full)