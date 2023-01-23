def marsExploration(s):
    count = 0
    n = 3
    array = [ s [ i: i + n ] for i in range( 0, len( s), n ) ]
    newArray = []
    for i in array:
        newArray.append(list( i ))
    for j in range( len( newArray ) ):
        if newArray[ j ][ 0 ] != 'S':
            count += 1
        if newArray[ j ][ 1 ] != 'O':
            count += 1
        if newArray[ j ][ 2 ] != 'S':
            count += 1
    return count
    
random = "SOSTOT"

print( marsExploration ( random ) )