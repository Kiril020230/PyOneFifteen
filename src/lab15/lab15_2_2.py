def funm(string):
    space_count = string.count(' ')
    if space_count % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")

string = input("Введите строку: ")
funm(string)