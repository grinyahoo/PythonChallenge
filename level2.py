# Python Challenge level 2
# level2.txt holds info from source of web-page
# Hint: recognize the characters. maybe they are in the book, but MAYBE they are in the page source.

import re

def main():
    file = open('level2.txt')
    next = "".join([re.sub(r'[^a-zA-Z]', '', line) for line in file ])
    print next

main()
