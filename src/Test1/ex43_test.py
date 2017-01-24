from sys import exit
from random import randint
quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
        ]
print(len(quips))
print randint(0, len(quips)-1)
help(randint)
dict_test = {1:"sd",2:"sdd"}
print dict_test.get(1)
print dict_test.get(3)