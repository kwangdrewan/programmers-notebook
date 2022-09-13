import random
import math

# change this var to alter probability of dem or rep victory.
pDems = 0.5025

sampleSize = int(input("Sample size? "))
samplePaths = int(input("Generate how many alternate paths? "))
demVictory = 0
repVictory = 0

for i in range(samplePaths):
    demVotes = 0
    for j in range(sampleSize):
        r = random.random()
        if r <= pDems:
            demVotes += 1

    print("Dem votes: " + str(demVotes))
    print("Rep votes: " + str(sampleSize - demVotes))

    if demVotes/sampleSize < 0.5:
        repVictory += 1
        print("Republicans win with " + str(sampleSize - demVotes) + " votes!")
    elif demVotes/sampleSize > 0.5:
        demVictory += 1
        print("Democrats win with " + str(demVotes) + " votes!")
    else:
        print("A tie???")

print("FINAL MULTIVERSE STATS:")
print("Democrats won " + str(demVictory) + " of the " + str(samplePaths) + " elections!")
print("Republicans won " + str(repVictory) + " of the " + str(samplePaths) + " elections!")
