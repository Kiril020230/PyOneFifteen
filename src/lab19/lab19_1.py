from PIL import Image

ris = Image.open("src\lab19\image.jpg")

# Получение размеров изображения
width, height = ris.size

# Получение значений цветов пикселей
pixels = list(ris.getdata())

# Вычисление средних значений для каждой составляющей цвета
red = sum([pixel[0] for pixel in pixels]) // len(pixels)
green = sum([pixel[1] for pixel in pixels]) // len(pixels)
blue = sum([pixel[2] for pixel in pixels]) // len(pixels)

print("Средние значения R, G, B:", red, green, blue)

# Создание изображения с усредненным цветом
n_image = Image.new("RGB", (width, height), (red, green, blue))
n_image.save("src\lab19\image2.jpg")

# Показ изображения
n_image.show()