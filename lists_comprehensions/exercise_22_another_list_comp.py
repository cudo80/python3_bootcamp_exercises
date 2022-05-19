'''
For all the numbers between 1 and 100 (including 100), create a variable called answer,
wich contains a list with all the numbersthat are divisible by 12. (12, 24, etc)
'''

answer = [val for val in range(1, 101) if val % 12 == 0]
