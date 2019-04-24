# Python Challenge. level 4 Linked list
# Hint: urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.
# Hint: link to "linkedlist.php?nothing=12345". By clicking response "and the next nothing is 44827"

# Hint: at nothing 16044 response 'Yes. Divide by two and keep going.'

import re
from urllib.request import urlopen

def main():
    # Start with given
    next_nothing('48827')

# Limited to 400 iterations as suggested
# Recursive approach
def next_nothing(nothing, counter=400):

    if counter > 0:
        with urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nothing) as response:

            html = response.read().decode('utf-8')
            next = re.findall(r'and the next nothing is (\d+)', html)
            print(html)

        # Stop when there's no next nothing
        if next:

            # Follow intructions in hint at nothing = 16044
            if next[0] == '16044':
                next[0] = '8022'

            next_nothing(next[0], counter - 1)

main()
# result peak.html
