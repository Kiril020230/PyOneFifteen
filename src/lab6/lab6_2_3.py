m = 10
full = m

for km in range(2, 8):
    m *= 1.1
    full += m

print("Суммарный путь спортсмена за неделю:", full, "километров")