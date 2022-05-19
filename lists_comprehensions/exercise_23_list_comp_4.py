'''
Given the string "amazing", create a variable called answer,
wich is a list containing all the letters from "amazing" but not the vowels (a, e, i ,o , u).
The answer should look like: ['m', 'z', 'n', 'g'].
'''

answer = [letter for letter in list("amazing") if letter not in "aeiou"]
