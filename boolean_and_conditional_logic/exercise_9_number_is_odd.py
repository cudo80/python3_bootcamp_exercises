'''
You will be provided with a random number in a variable called num.
Use a conditinal statement to check if the number is odd.
If num is odd, print "odd". Otherwise print "even".
Hint: use modulus % to figure out if the number is odd!
'''

from random import randint

num = randint(1, 1000)

if num % 2 != 0:
    print('odd')
else:
    print('even')
