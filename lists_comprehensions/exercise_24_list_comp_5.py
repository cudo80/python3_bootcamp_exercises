'''
Using a nested list comprehension and range(), create a variable called answer,
with the follwing value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
To break it down, start by using range and a list comprehension to generate the list [0, 1, 2].
And then repeat that whole thing 3 times in a nested list comprehension.
'''

answer = [[x for x in range(0, 3)] for val in range(0, 3)]