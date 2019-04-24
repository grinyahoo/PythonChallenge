# Python Challenge level 3
# Hint: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
# Data found in source of web-page, put in level3.txt

# Problem similar to level2

import re

def main():
    #load file to string
    file = open('level3.txt')
    str = ''.join([line for line in file])

    # find all occurencies and fetch a small letter

    small = re.findall(r'[a-z][A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]', str)
    print "".join(small)

# linkedlist

main()
