'''
In this exercise you will be given a few variables 
that will be set randomly to Boolean values (True or False):

- actually_sick - when you legit have the flu!
- kinda_sick - you are feeling under the weather 
and it is enough to treat yourself with a day off if you can spare it.
- hate_your_job - work sucks, I know...

You are also given a random number of sick_days between 0 and 10.
Finally, there is a variable called calling_in_sick that you must set to True or False
based on the following scenarios:

Set to True if:
- You are actually_sick and you have sick_days remaining
- You are kinda_sick and hate_your_job and you have sick_days remaining

Otherwise, set to False.
'''

from random import choice, randint

actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

calling_in_sick = None
if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False
