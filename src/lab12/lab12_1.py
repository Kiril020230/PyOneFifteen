m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
mat = []
print("Введите элементы:")
for num in range(m):
    list = list(map(int, input().split()))
    mat.append(list)

for num in range(m):
    if num % 2 == 0:
        print(*mat[num])
    else:
        print(*mat[num][::-1])