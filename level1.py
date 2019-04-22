# Python Challenge. Level 1
# k->m o->q e->g

INPUT = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
URL = "map"

# To solve shift +2 in ascii table but dont touch space and dot, you get
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and thatws why this text is so long. using string.maketransxy is recommended. now apply on the url.

def solve(input):

    decoded = map(lambda x: chr(96 + (ord(x)-96 +2) % 26) if ord(x) not in (32, 46) else x, input)
    print ''.join(decoded)

solve(INPUT)
solve(URL)

#map -> ocr
