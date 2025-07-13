import qrcode
from PIL import Image
url = input("Enter the url: ")
page = input("make the file name: ")
img = qrcode.make(url)
type(img) 
img.save(f"images/{page}.png")