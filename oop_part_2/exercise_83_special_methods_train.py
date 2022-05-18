'''
Create a class Train that has one attribute: num_cars 
wich is specified when the train is instantiated.
There should also be two special/magic/dunder methods on it:
- One method that describes the train when we call print on it by saying "x car train"
where x is the number of cars (see example below)
- One method that denotes the lenght of the train when we call len on it
Example:
    a_train = Train(4)
    print(a_train) # 4 car train
    len(a_train) # 4

Note: You do not need ti instantiate Train for the tests to pass. 
The tests will try to instantiate Trai for you.
'''


class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars
        
    def __repr__(self):
        return "{} car train".format(self.num_cars)
    
    def __len__(self):
        return self.num_cars
