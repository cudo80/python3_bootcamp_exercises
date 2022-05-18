'''
Write a function called yes_or_no, wich returns a generator that first yields "yes", 
then "no", then "yes", then "no", and so on.
'''

'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    gen = "yes"
    while True:
        yield gen
        gen = "no" if gen == "yes" else "yes"
