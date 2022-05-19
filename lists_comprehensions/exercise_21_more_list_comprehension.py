'''
1. Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], create a variable called asnwer,
wich is a new list that is the intersection of the two.
Your output should be [3, 4]. Hint: use the in operator to test whether an element is in a list.
For example: 5 in [1, 5, 2] is True. 3 in [1, 5, 2] is False.
2. Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer2,
wich is a new list with each word reversed and in lower case (use a slice to do the reversal!)
Your output should be ["eile", "mit", "ttam"]
'''

answer = [x for x in [1, 2, 3, 4] if x in [3, 4, 5, 6]]

answer2 = [x[::-1].lower() for x in ["Elie", "Tim", "Matt"]]
