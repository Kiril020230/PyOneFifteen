m = int(input("Введите количество строк матрицы: "))
n = int(input("Введите количество столбцов матрицы: "))
mat = []
print("Введите элементы матрицы:")
for num in range(m):
    list = list(map(int, input().split()))
    mat.append(list)

suma = [sum(row[j] for row in mat) for j in range(n)]
print("Суммы элементов каждого столбца матрицы:")
for num2 in range(n):
    print(f"Сумма элементов столбца {num2 + 1}: {suma[num2]}")