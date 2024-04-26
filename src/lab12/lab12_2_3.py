n = int(input("Введите размерность квадратной матрицы: "))
mat = [[int(input(f"Элемент [{i+1}][{j+1}]: ")) for j in range(n)] for i in range(n)]
sum_a_dia = sum(mat[i][j] for i in range(n) for j in range(n) if i >= j and mat[i][j] > 0)

print("Исходная матрица:")
for row in mat:
    print(row)
print("Сумма положительных элементов под главной диагональю и на ней:", sum_a_dia)