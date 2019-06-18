#	Python Challenge level 10
#	"What are you looking at?"
#

# 	This is the Look and say sequence
#	input a = [1, 11, 21, 1211, 111221, ... ]
#	output len(a[30])

import re

def lookAndSay(pos, prev='1'):
		
	result = ''
	for m in re.finditer(r'(.)\1*', prev):
		buf = m.group(0)
		result += str(len(buf)) + buf[0]
	
	
	if pos>1:
		return lookAndSay(pos-1, result)
	else:
		return result


print(len(lookAndSay(30, '1')))
