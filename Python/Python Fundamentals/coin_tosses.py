import random

def coin_toss():
    #these will keep count of how many times each side has been flipped
    heads = 0
    tails = 0
    for each in range(5000):
        #fliping the coin and storing it
        toss = random.randint(0,1)
        if toss == 1:
            #this wil run for coin flip of heads
            heads += 1
            result = "heads"
        elif toss == 0:
            #this will run for a coin flip of tails
            tails += 1
            result = "tails"
        #printing the final result of current flip along with total count
        print "Attempt #" + str(each + 1) + ": Throwing a coin... It's " + result + "! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"

coin_toss()
