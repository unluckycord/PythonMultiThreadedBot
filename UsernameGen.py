import random

FirstNames = []

def LoadNames():
    with open('first-names.txt') as f:
        [FirstNames.append(line.strip()) for line in f.readlines()]

def UsernameGenerator():
    username = str(FirstNames[random.randint(1,4946)]) + str(random.randint(10000,1000000))
    return username
