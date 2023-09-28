import random

FirstNames = []

def LoadNames():
    with open('first-names.txt') as f:
        [FirstNames.append(line.strip()) for line in f.readlines()]

def UsernameGenerator():
    username = str(FirstNames[random.randint(1,4946)]) + str(random.randint(1,100000000))
    return username

if __name__ == "__main__":
    LoadNames()
    print(UsernameGenerator())