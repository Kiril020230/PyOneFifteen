inp = int(input("Введите количество записей в словаре: "))
dictionary = {}
for i in range(inp):
    word_info = input().split('-')
    word = word_info[0]
    description = word_info[1]
    dictionary[word] = description

word = input("Введите слово для поиска: ")
if word in dictionary:
    print(dictionary[word])
else:
    print("Нет в словаре")