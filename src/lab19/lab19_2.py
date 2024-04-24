from PIL import Image

image = Image.open("src\lab19\image3.jpg")
bw_image = image.convert("L")
mirrored_image = bw_image.transpose(Image.FLIP_LEFT_RIGHT)

new_size = (400, 300)  # новая ширина и высота
resized_image = mirrored_image.resize(new_size)

resized_image.save("src\lab19\image4.jpg")
resized_image.show()