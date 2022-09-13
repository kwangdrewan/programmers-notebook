# After 10,000,000 games, I observe (if the program works correctly) that
# I win at a rate of about 0.761 in the long run.

import random

yourServe = 1
p1Score = 0
p2Score = 0
p1Victory = 0
p2Victory = 0
gamesToPlay = int(input("How many rounds (int only)? "))


for i in range(gamesToPlay): 
    while(1):    
        r = random.random()
        if yourServe == 1 and r < 0.6:
            p1Score += 1
        elif yourServe == 1 and r >= 0.6:
            yourServe = 0
            p2Score += 1
        elif yourServe == 0 and r < 0.5:
            yourServe = 1
            p1Score += 1
        elif yourServe == 0 and r >= 0.5:
            p2Score += 1

        if p1Score == 24:
            print("Your Victory!")
            print("Final Score: \n p1: " + str(p1Score) + ", p2: " + str(p2Score))
            p1Victory += 1
            yourServe = 1
            p1Score = 0
            p2Score = 0
            break
        elif p2Score == 24:
            print("Opponent Victory!")
            print("Final Score: \n p1: " + str(p1Score) + ", p2: " + str(p2Score))
            p2Victory += 1
            yourServe = 1
            p1Score = 0
            p2Score = 0
            break

print("You won at a rate of: " + str(p1Victory/gamesToPlay))
