from PIL import Image

ris = Image.open("src\lab19\image3.jpg")
sc_image = ris.convert("L")
tra_image = sc_image.transpose(Image.FLIP_LEFT_RIGHT)

h_g = (400, 300)  # новая ширина и высота
new_image = tra_image.resize(h_g)

new_image.save("src\lab19\image4.jpg")
new_image.show()