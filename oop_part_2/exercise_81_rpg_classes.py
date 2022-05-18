'''
Let's pretend we are building a RPG (roleplaying game) in Python.
1. Define a base class "Character" that has the following properties:
    - name - String
    - hp - an Integer value representing health (aka hitpoints)
    - level - an Integer value representing experience level
2. Define a subclass "NPC" (wich stands for Non-Player Character) that inherits from Character,
and has an additional instance method called speak wich prints the speech that character would say when a player interacts with them.
'''

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
        
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
    
    def speak(self):
        return "{} says something".format(self)
