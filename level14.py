# Python Challenge level 14
# Italy
#
# 100x100 = (100 + 99 + 99 + 98) + (...

from PIL import Image

IMG_URL = "http://www.pythonchallenge.com/pc/return/wire.png"

vectors = ((1, 0, -1), (0, 1, 0), (-1, 0, -1), (0,-1, 0))
x ,y = 0, 0 
strip_pixel_number = 0
steps = 100
i = 0
with Image.open('wire.png') as img:
    # pixels = img.load()
    out = Image.new("RGB", (100,100))
    # img.show()
    while steps>0:
        for vector in vectors:         
            for _ in range(steps):
                x += vector[0]
                y += vector[1]
                out.putpixel((x,y), img.getpixel((strip_pixel_number, 0)))
                strip_pixel_number += 1               
            steps += vector[2]
            i += 1
    out.show()
    