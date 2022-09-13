# To answer problem 3b), I have no idea how the gamblers detected such a
# small variation but I think they're correct. In the long run (n = 10000000),
# you get about 1% more 10's than 9's when you roll 3 dice.


import random
import math

def roll3Dice():
    r1 = random.random()
    r2 = random.random()
    r3 = random.random()

    dr1 = math.floor(6*r1) + 1
    dr2 = math.floor(6*r2) + 1
    dr3 = math.floor(6*r3) + 1

    return dr1 + dr2 + dr3

count9 = 0
count10 = 0
rollCount = 0

j = input("Define n (int only): ")

for i in range(int(j)):
    rollResult = roll3Dice()
    rollCount += 1
    if rollResult == 9:
        count9 += 1
    if rollResult == 10:
        count10 += 1
    # Positive means more 9's. Negative means more 10's.
    # n = 1000, ratio ~= -0.008
    # n = 10000, ratio ~= -0.0195
    # n = 100000, ratio ~= -0.0105
    # n = 1000000, ratio ~= -0.00903
    # n = 10000000, ratio ~= -0.00925
    print("Ratio of 9's - Ratio of 10's: " + str(count9/rollCount - count10/rollCount))
