import random
import math

coinToss = 0
headCount = 0
val = input("Enter n: ")
for i in range(int(val)):
    r = random.random()
    coinToss += 1
    if(r > 0.5):
        headCount += 1
    if(coinToss % 100 == 0):
        print(str(headCount/coinToss - 0.5))
        #print(headCount - coinToss/2)
