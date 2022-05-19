'''
Given a list ["Ellie", "Tim", "Matt"], create a variable called answer,
wich is a new list containing the first letter of each name in the list.
I would use a list comprehension, though you could also loop over manually.
Given a list [1, 2, 3, 4, 5, 6], create a new variable called answer2,
wich is a new list of all the even values. Another good candidate for a list comprehension.
'''

answer = [x[0] for x in ["Ellie", "Tim", "Matt"]]

answer2 = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]
