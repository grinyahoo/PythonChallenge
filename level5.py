# Python challenge level 5
# Peak hell => 'pickle'


import pickle
from urllib.request import urlopen

src = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(src)
src.close()

for item in data:
    print("".join([chr * qty for chr, qty in item]))
