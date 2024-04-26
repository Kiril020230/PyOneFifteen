n = 5
m = sum(num**2 - 2*num2 for num in range(n+1) for num2 in range(n+1))

print("Результат:", m)