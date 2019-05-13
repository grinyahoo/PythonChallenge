from PIL import Image
from urllib.request import urlopen
import re

def main():

	# Using urllib open image file:
	with urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png") as html:

		# Using Pillow(PIL) fetch (1px x 608px) strip from image (originaly strip on image is 9 pixels, you need just first. Others are sthe same as first one.)
		with Image.open(html) as img:
			strip = [img.getpixel((j,43)) for j in range(0, 608)]

			# # Uncomment to see the sequence of pixel interpretation
			# print('Here is pixel sequence:\n',strip,end="\n")

			# Each pixel is tuple(R, G, B, opacity). I our case R=G=B, and all data have 255 opacity. So the only information in strip is RGB value.
			# Assume this contain an ordinants of ASCII charset

			s = ""
			for pixel in strip:
				s += chr(pixel[0])

			# # Uncomment to see the string
			# print('Char decoded: %s'%s)

			# It is a string. But first symbol repeats 5 times and others 7 times. Its ok we'll start from index=4, and take a step=7

			fixed_s = ""
			for i in range(4,len(s),7):
				fixed_s += s[i]

			# print('Fixed string: %s'%fixed_s)
			# # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

			# Looks like ASCII charset again, lets fetch them with regEx

			next_level_list = re.findall(r'\d+', fixed_s)
			result = ''.join([chr(int(x)) for x in next_level_list])
			print('Next level is: %s'%result)

main()
