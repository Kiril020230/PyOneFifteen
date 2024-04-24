from PIL import Image

# Открытие изображения
image = Image.open("src\lab19\image.jpg")

# Получение размеров изображения
width, height = image.size

# Получение значений цветов пикселей
pixels = list(image.getdata())

# Вычисление средних значений для каждой составляющей цвета
avg_red = sum([pixel[0] for pixel in pixels]) // len(pixels)
avg_green = sum([pixel[1] for pixel in pixels]) // len(pixels)
avg_blue = sum([pixel[2] for pixel in pixels]) // len(pixels)

print("Средние значения R, G, B:", avg_red, avg_green, avg_blue)

# Создание изображения с усредненным цветом
avg_image = Image.new("RGB", (width, height), (avg_red, avg_green, avg_blue))
avg_image.save("src\lab19\image2.jpg")

# Показ изображения
avg_image.show()