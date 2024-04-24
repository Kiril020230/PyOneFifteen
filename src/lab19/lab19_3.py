from PIL import Image

image = Image.open("src\lab19\image5.jpg")
width, height = image.size
new_image = Image.new("RGB", (width, height))

for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        red, green, blue = pixel

        min_value = min(red, green, blue)
        max_value = max(red, green, blue)

        new_red = min_value
        new_green = green
        new_blue = max_value

        new_image.putpixel((x, height - y - 1), (new_red, new_green, new_blue))


new_image = new_image.transpose(Image.ROTATE_180)
new_image.save("src\lab19\image6.jpg")
new_image.show()