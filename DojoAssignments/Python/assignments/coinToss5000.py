import random
heads = 0
tails = 0
count = 0

for each in range(0,5000):
    coin = random.random()
    count += 1
    strAttempt = "Attempt: " + str(count) + " Throwing a coin..."
    if round(coin) == 1:
        heads += 1
        strAttempt += " It's heads! ... Got "
    else:
        tails += 1
        strAttempt += " It's tails! ... Got "
    strAttempt += str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
    print(strAttempt)
print("End of Program")
