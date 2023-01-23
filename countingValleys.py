def countingValleys(steps, path):
    numberOfValleys = 0
    levelArray = []
    level = 0
    splitPath = list( path )
    for i in path: 
        if ( i == "U" ):
            level += 1
            levelArray.append( level )
            if ( level == 0 ):
                numberOfValleys += 1
        elif ( i == "D" ):
            level -= 1
            levelArray.append( level )
    return numberOfValleys

    
random = "UDDDUDUU"

print( countingValleys ( 8, random ) )