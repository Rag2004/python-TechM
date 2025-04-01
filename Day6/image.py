from PIL import Image
import PIL.ImageOps  
img = Image.open("./img.jpg")

inverted_img =  PIL.ImageOps.invert(img)
inverted_img.save("inverted_image.jpg")

