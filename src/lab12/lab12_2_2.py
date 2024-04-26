n = int(input("Введите размерность квадратной матрицы: "))
mat = [[int(input(f"Элемент [{i+1}][{j+1}]: ")) for j in range(n)] for i in range(n)]

suma = [sum(mat[i]) for i in range(n)]
print("Исходная матрица:")
for row in mat:
    print(row)
print("Суммы элементов каждой строки:", suma)