import random
import math

def rollDice():
    r = random.random()
    diceRoll = math.floor(6*r) + 1
    return diceRoll

def roll2Dice():    
    r1 = random.random()
    r2 = random.random()
    dr1 = math.floor(6*r1) + 1
    dr2 = math.floor(6*r2) + 1
    return dr1 + dr2

def roll3Dice():
    r1 = random.random()
    r2 = random.random()
    r3 = random.random()

    dr1 = math.floor(6*r1) + 1
    dr2 = math.floor(6*r2) + 1
    dr3 = math.floor(6*r3) + 1

    return dr1 + dr2 + dr3

"""
count = 0
pCount = 0

while(1):
    count = count + 1
    dr = rollDice()
    dr2 = rollDice()
    if(dr == 4):
        pCount = pCount + 1
        print(pCount / count)
"""
def DeMere2():
    success = 0
    for i in range(1000):
        for rolls in range(24):
            dr = rollDice()
            dr2 = rollDice()
            if(dr == dr2):
                success = success + 1
                print("Success!")
    print(success)
    print("Probability of winning: " + str(success/1000))

