# Python Challenge level 12
# dealing evil
#
# http://www.pythonchallenge.com/pc/return/evil.html
#
# 5 stack for 5 cards 
#

with open('evil2.gfx','rb') as f:
    data = f.read()
    for i in range(5):
        open('LVL12_OUT_%d.jpg' % i ,'wb').write(data[i::5])