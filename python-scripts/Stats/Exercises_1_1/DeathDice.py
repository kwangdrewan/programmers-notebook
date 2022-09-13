# Death finds you. You plead with him that it's too soon, and he agrees to a
# concession. Every year, he'll roll a set of dice, and if it turns up snake
# eyes (both 1's) he'll take your life, otherwise, you get one more year.

# But it's not necessarily a normal pair of dice.

# On the first year, both "dice" will only have two sides, numbered 1 and 2.
# So in that first year, there's a 25% chance of rolling snake eyes and ending
# things there.

# On the second year, he comes with tetrahedral dice, i.e. both are four-sided, 
# numbered 1 through 4, and again only takes your life if he rolls two 1's.

# The next year, the dice are six-sided, after that, eight-sided, etc., etc.

# Each year you have a lower and lower chance of dying, but he'll come back 
# every year with a new set of dice, never stopping.

# What's the probability you end up immortal?

import random
import math

n = int(input("How many timelines? "))
yearsPastDeath = 0
effectivelyImmortal = 10000
deathScoreList = []
lifeCount = 0

def rollDeathDice(years):
    r1 = random.random()
    r2 = random.random()
    dr1 = math.floor(years*2*r1) + 1 
    dr2 = math.floor(years*2*r2) + 1
    return dr1 + dr2

# Now, what's the probability of rolling two ones?
# Basically, we need to keep running this forever until...when?
# Let's say we go for 5,000 years. That would be mean the dice you roll is
# d10,000, meaning that the chance of snake eyes is 1 in 100,000,000.
# Once you hit 5,000 years, you are effectively immortal.

for i in range(n):
    #print("====== Timeline " + str(i) + " Start. ======")
    yearsPastDeath = 0
    for j in range(effectivelyImmortal):
        yearsPastDeath += 1
        if rollDeathDice(yearsPastDeath) == 2:
            #print("You died on year " + str(yearsPastDeath))
            deathScoreList.append(yearsPastDeath)
            break
        elif yearsPastDeath == effectivelyImmortal:
            #print("You are effectively immortal!")
            lifeCount += 1
    #print("====== Timeline " + str(i) + " Complete. ======")

print("===== FINAL RESULTS =====")
print("The chance that you will become effectively immortal (" + str(effectivelyImmortal) + ") is: " + str((lifeCount/n)*100) + "%.")
print("Your longest lasting non-immortal timeline lasted " + str(max(deathScoreList)) + " years!")
