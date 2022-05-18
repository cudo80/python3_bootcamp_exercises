'''
Your job is to write a simple conditional to check if choice is 7.
If choice is 7, print out "lucky". Otherwise, print out "unlucky".
'''

from random import randint

choice = randint(1, 10)

if choice == 7:
    print('lucky')
else:
    print('unlucky')
