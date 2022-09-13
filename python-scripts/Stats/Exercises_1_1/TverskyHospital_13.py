import random
import math

LHBirths = 45
SHBirths = 15
SHBoyCount = 0
n = int(input("How many timelines bro? "))

LH60Count = 0
SH60Count = 0

TotalLH60Count = []
TotalSH60Count = []

def isBoy():
    r = random.random()
    if r < 0.5:
        return 1
    else:
        return 0

for x in range(n):
    LH60Count = 0
    SH60Count = 0
    for i in range(365):
        LHBoyCount = 0
        SHBoyCount = 0
        for j in range(LHBirths):
            if isBoy() == 1:
                LHBoyCount += 1
        for k in range(SHBirths): 
            if isBoy() == 1:
                SHBoyCount += 1
        if LHBoyCount/LHBirths >= 0.6:
            LH60Count += 1
        if SHBoyCount/SHBirths >= 0.6:
            SH60Count += 1
    TotalLH60Count.append(LH60Count)
    TotalSH60Count.append(SH60Count)

avgLH = str(sum(TotalLH60Count)/len(TotalLH60Count))
avgSH = str(sum(TotalSH60Count)/len(TotalSH60Count))

print("=== FINAL STATISTICS ===")
print("On average, the LH had " + avgLH + " of >= 60% boy days.")
print("On average, the SH had " + avgSH + " of >= 60% boy days.")
print("------------------------")
print("The highest number of boys born in a given timeline year in the large hospital is " + str(max(TotalLH60Count)) + ".")
print("The lowest number of boys born in a given timeline year in the small hospital is " + str(min(TotalSH60Count)) + ".")
