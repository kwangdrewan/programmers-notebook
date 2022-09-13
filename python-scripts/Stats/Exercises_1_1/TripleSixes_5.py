# Using the brute force that is Monte Carlo over 1,000,000 simulated games,
# I have strong evidence that DeMoivre is correct. By appending the number of
# rolls it takes to win per game to a list and sorting it, one can find the
# median of the list and thus, figure out it will take 150 rolls to get a 
# > 50% chance of getting 3 sixes with three dice.

import random
import math
import statistics
from dice import roll3Dice

totalCount = 0

numberOfGames = int(input("This program allows you to Monte Carlo the 'n' required to get three sixes favorably (> 50%) when rolling 3 dice.\nSelect the # of games that will be played. A higher number is suggested for more precise results.: "))

gamesPlayed = 0
rollList = []
for i in range(numberOfGames):
    totalCount = 0
    gamesPlayed += 1
    while(1):
        r = roll3Dice()
        totalCount += 1
        if r == 18:
            rollList.append(totalCount)
            break

rollList.sort()
print("You need to roll the dice " + str(math.ceil(statistics.median(rollList))) + " times for a >50% chance of getting three sixes.")

