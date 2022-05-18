'''
In this exercise x and y are two random variables.
The code at the top of the dile randomly assigns them (we´ll learn how it works later on).

1. If both are positive numbers, print "both positive".
2. If both are negative, print "both negative".
3. Otherwise, tell us wich one is positive and wich one is negative, 
e.g. "x is positive and y is negative".
'''

from random import randint

x = randint(-100, 100)

while x == 0: # make sure x is not zero
    x = randint(-100, 100)

y = randint(-100, 100)

while y == 0: # make sure y is not zero
    y = randint(-100, 100)

if x > 0 and y > 0:
    print('both positive')
elif x < 0 and y < 0:
    print('both negative')
elif x > 0 and y < 0:
    print('x is positive and y is negative')
elif x < 0 and y > 0:
    print('y is positive and x is negative')
