def fil_arr(numbers):
    filtered_numbers = [num for num in numbers if num > 10 and num % 2 == 0]
    return filtered_numbers

num = list(map(int, input("Введите список чисел через пробел: ").split()))
filtered_numbers = fil_arr(num)
if filtered_numbers:
    print("Отфильтрованный список:", filtered_numbers)
else:
    print("В списке нет четных чисел больше 10.")