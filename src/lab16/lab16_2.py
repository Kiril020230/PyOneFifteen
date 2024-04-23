def fact(n):
    if n == 0:  return 1
    else:       return n * fact(n - 1)

def calculate_expression(n, m):
    result = fact(n) / (fact(m) * fact(n - m))
    return result

n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))

c = calculate_expression(n, m)

print("Значение выражения:", c)