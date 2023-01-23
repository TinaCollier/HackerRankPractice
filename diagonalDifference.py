def diagonalDifference(arr):
    mainSum = 0
    secondarySum = 0
    for i in range( len( arr ) ):
        mainSum += arr[ i ][ i ]
        secondarySum += arr[ i ][ len( arr ) - i - 1 ]
    diff = mainSum - secondarySum
    return abs( diff )


    
random = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

print( diagonalDifference ( random ) )