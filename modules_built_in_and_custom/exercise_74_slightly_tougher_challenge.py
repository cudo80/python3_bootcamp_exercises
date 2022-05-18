'''
Define a function called constains_keyword that accepts any number of string arguments.
It should return True if any of the arguments are considered Python keywords (things like ´def´. ´return´, ´if´, etc.)
Otherwise it should return False. Python has a built-in module called keyword that contains a method called iskeyword 
and then use keyword.iskeyword in your own function to determine if a given string is a keyword.
    contains_keyword("hello", "goodbye") # False
    contains_keyword("def", "haha", "lol", "chicken", "alaska") # True
    contains_keyword("four", "for", "if") # True
    contains_keyword("blah", "doggo", "crab", "anchor") # False
    contains_keyword("grizzly", "ignore", "return", "False") # True

Note: don´t just manually check for the keywords you know like return, def, if and for. 
The test logic for this exercise will use a bunch of keywords we haven´t yet covered, 
so definitely make sure to import and use the keyword module to help you!
That´s the point of this exercise, after all.
'''

import keyword

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item):
            return True
    return False
