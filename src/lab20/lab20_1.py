from PIL import Image, ImageFont, ImageDraw  
      
image = Image.new('RGB', (350, 350), 'white')
  
draw = ImageDraw.Draw(image)  
  
# specified font size 
font = ImageFont.truetype(r'src\lab20\arial.ttf', 180)  
  
text = 'Kirill'
  
# drawing text size 
draw.text((5, 5), text, fill ="blue", font = font, align ="right")  
  
image.show() 