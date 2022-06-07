'''
Write a function called get_multiples, which accepts a number and a count,
and returns a generator that yelds the first count multiples of the number.
The default number should be 1 and the default count should be 10.
'''

def get_multiples(number=1, count=10):
    next_num = number
    while count > 0:
        yield next_num
        count -= 1
        next_num += number
