import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://wallpaperaccess.com/full/158739.jpg")

print("Status Code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Could not save image.")
