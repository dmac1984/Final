# Accept user input for length of password
# Get random value for each character
# append each character to a list
# Output password list

from random import *

def main():
    pwLst = []
    pwLenStr = input( "How many characters in your password? " )
    pwLen = int( pwLenStr)
    for c in range( pwLen ):
        pwAsc = randrange( 65, 123 )
        if pwAsc < 91 or pwAsc > 96:
            pwChr = chr( pwAsc )
            pwLst.append( pwChr )
    print( "Your password is: ", pwLst )
            
main()