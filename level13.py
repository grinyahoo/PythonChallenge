# Python Challenge level 13
# Call evil
#
# http://www.pythonchallenge.com/pc/return/disproportional.html
#
# 5 is clickable
# http://www.pythonchallenge.com/pc/phonebook.php
# 
# there is xml error, google it
# need to use xmlrpc library to access phonebook
# 

import xmlrpc.client

URL = 'http://www.pythonchallenge.com/pc/phonebook.php'

with xmlrpc.client.ServerProxy(URL) as phonebook:
    print(phonebook.phone("Bert"))