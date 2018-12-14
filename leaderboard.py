from random import *

def intro1():
    moolah = int(input("Enter the number of dollars you start with: "))
    spins = int(input("Enter the number of spins you will play: "))
    bet = int(input("Enter how many dollars you will bet for each spin: "))
    return moolah, spins, bet;

def intro2():
    print("Choose one of the following strategy choices")
    print("- Bet on a (s)ingle number (pays 35 to 1)")
    print("- Bet on (e)ven or odd numbers (pays 1 to 1)")
    print("- Bet on a (d)ozen numbers (pays 2 to 1)")
    print()
    strat = input("Enter your strategy choice (s, e, d): ")
    return strat;

def doz(third):
    if third == 1:
        winm = randrange(0, 38)
        if winm > 0 or winm < 13:
            w = True
        elif winm == 0 or winm > 12:
            w = False
    elif third == 2:
        winm = randrange(0, 38)
        if winm > 13 and winm < 24:
            w = True
        elif winm > 13 or winm > 24:
            w = False
    elif third == 3:
        winm = randrange(0, 38)
        if winm > 24 and winm != 37:
            w = True
        elif winm < 25 or winm == 37:
            w = False
    return w;

def eo(side):
    if side == "e":
        wins = random()
        if wins < .5:
            w = True
        elif wins >= .5:
            w = False
    elif side == "o":
        wins = random()
        if wins >= .5:
            w = True
        elif wins < .5:
            w = False
    return w;

def sing(num):
    if num == 00:
        num = 37
    elif num != 00:
        num = num
    winum = randrange(0, 38)
    if winum == num:
        w = True
    elif winum != num:
        w = False
    return w;

def main():
    bank, turns, wager = intro1()
    t = 0
    wincount = 0
    losscount = 0
    origbank = bank
    strategy = intro2()
    if strategy == "d":
        thrd = int(input("Enter 1 to bet on numbers 1-12, 2 for numbers 13-24, or 3 for numbers 25-36: "))
        while bank > 0 and t != turns:
            win = doz(thrd)
            if win == True:
                t = t + 1
                wincount = wincount + 1
                bank = bank + wager * 2
            elif win == False:
                t = t + 1
                losscount = losscount + 1
                bank = bank - wager
    elif strategy == "e":
        oe = input("Enter if you want to bet on (e)ven or (o)dd numbers: ")
        while bank > 0 and t != turns:
            win = eo(oe)
            if win == True:
                t = t + 1
                wincount = wincount + 1
                bank = bank + wager
            elif win == False:
                t = t + 1
                losscount = losscount + 1
                bank = bank - wager
    elif strategy == "s":
        bnum = int(input("Enter the single number you want to bet on (00 or 0 to 36): "))
        while bank > 0 and t != turns:
            win = sing(bnum)
            if win == True:
                t = t + 1
                wincount = wincount + 1
                bank = bank + wager * 35
            elif win == False:
                t = t + 1
                losscount = losscount + 1
                bank = bank - wager
    winper = 100 * (wincount / t)
    lossper = 100 * (losscount / t)
    left = bank - origbank
    print("After", t, "spins")
    print("Wins: ", wincount, winper, "%")
    print("Losses: ", losscount, lossper, "%")
    print("Ending bank: $", bank)
    print("Net winnings: $", left)
    
main()

    
    