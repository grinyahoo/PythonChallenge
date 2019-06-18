# Python Challenge level 11
# Odd even
#
# http://www.pythonchallenge.com/pc/return/5808.html
#
# Appears as image. Its easy to notice
# that image is composed from 2 layers.
# Title of challenge is "odd even".
# So we will try to split original image
# in two layers by odd-even pixels.

from PIL import Image
import urllib
from urllib.request import urlopen


# http://www.pythonchallenge.com/pc/return/cave.jpg

URL = 'http://www.pythonchallenge.com/pc/return/'
IMG_URL = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
USERNAME = 'huge'
PASSWORD = 'file'

# Authorization to source

pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwd_manager.add_password(None, URL, USERNAME, PASSWORD)
handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)
opener = urllib.request.build_opener(handler)
opener.open(IMG_URL)
urllib.request.install_opener(opener)

with urlopen(IMG_URL) as src:
    with Image.open(src) as orig_image:
        layer1 = orig_image.copy()

        # Paint black all odd rows and columns

        for i in range(640):
            for j in range(480):
                if i % 2 > 0 or j % 2 > 0:
                    layer1.putpixel((i,j),(0,0,0))

        # orig_image.show()
        layer1.show()
