def cointoss():
    import random
    attempt =0
    heads =0
    tails =0

    for i in range(5000):
        flip = random.randint(0,1)
        if flip == 0:
            heads +=1
            attempt +=1
            print "Attempt", str(attempt),"...", " It's a head!", "...", "Got",str(heads)+" heads"," so far and",str(tails)+" tails", "so far"

        if flip == 1:
            tails +=1
            attempt +=1
            print "Attempt", str(attempt),"...", " It's a tail!", "...", "Got",str(heads)+" heads"," so far and",str(tails)+" tails", "so far"
cointoss()