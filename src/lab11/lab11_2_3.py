inp = [int(input(f"Введите элемент {i+1}: ")) for i in range(16)]
nums = [inp[i] for i in range(0, len(inp), 2)]

print("Список из значений под четными номерами:", nums)