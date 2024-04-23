def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def fun(n, m):
    result = fact(n) / (fact(m) * fact(n - m))
    return result


n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))


с = fun(n, m)
print("Значение выражения:", с)