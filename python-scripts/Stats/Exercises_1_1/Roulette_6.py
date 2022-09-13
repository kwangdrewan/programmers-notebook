# The lesson is to never play standard roulette.

import random
import math

n = int(input("How many games (int only)? "))
redOrBlack = input("Red or black (str only)? ")
money = 0

for i in range(n):
    r = random.randint(0, 37)
    print("Your number is: " + str(r-1))
    if r == 1 or r == 0:
        money -= 1
        print("Lose.")
    elif (r != 1 or r != 0) and (r - 1) % 2 == 0 and redOrBlack == "red":
        money += 1
        print("Win!")
    elif (r != 1 or r != 0) and (r - 1) % 2 == 0 and redOrBlack == "black":
        money -= 1
        print("Lose.")
    elif (r != 1 or r != 0) and (r - 1) % 2 != 0 and redOrBlack == "black":
        money += 1
        print("Win!")
    elif (r != 1 or r != 0) and (r - 1) % 2 != 0 and redOrBlack == "red":
        money -= 1
        print("Lose.")

if money < 0:
    print("You've lost " + str(abs(money)) + " dollars because you're a monkey brain.")
else:
    print("Youve earned " + str(money) + " dollars!")
