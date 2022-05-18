'''
Your task is to write a function in the helpers.py file, and then call is from the exercise.py file.
More specifically:
    1 - In helpers.py, define a function called lucky_number() that always returns the number 37.
    That's it. It always returns 37, no matter what.
    2 - In exercise.py, import the helpers module.
    3 - From inside exercise.py, call the lucky_number function you define in the helpers module.
    Save the result to a variable called num
'''

#Import your helpers module here.  Do not use the 'from' or 'as' syntax, just use a plain old 'import'
import helpers


#Call the lucky_number function from your helpers module, and save the result to a variable called num
num = helpers.lucky_number()
