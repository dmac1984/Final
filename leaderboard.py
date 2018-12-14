# Read each line in the input file.
# Create dictionary keyed on difficulty level
# Check the line to see if the score is higher than the previous high score for the level.
# Print out highest score for each difficulty level.

def main():
    scores = []
    infile = open( "scores.txt", "r" )
    easyBest = 0
    medBest = 0
    hardBest = 0
    for line in infile:
        pName, score, dLev = line.split( "," )
        if dLev == "easy":
            if score > easyBest:
                easyBest = score
                scores.insert( 0, line )
        elif dLev == "medium":
            if score > medBest:
                medBest = score
                scores.insert( 1, line )
        elif dLev == "hard":
            if score > hardBest:
                hardBest = score
                scores.insert( 2, line )
    print( "*******Leaderboard******" )
    print( "Easy: ", scores.pop( 0 ) )
    print( "Medium; ", scores.pop( 1 ) )
    print( "Hard: ", scores.pop( 2 ) )
    
main()
