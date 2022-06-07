'''
Write a function called get_unlimited_multiples, 
which accepts and returns a generator 
that will yield an unlimited number of multiples of that number.
The default number should be 1.
'''

def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num
