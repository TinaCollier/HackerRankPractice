def birthday( s, d, m ):  
    return sum( 1 for i in range( len( s ) ) if sum( s[ i:i+m ] ) == d )
    
array = [ 1, 2, 1, 3, 2 ]
print(birthday(array, 3, 2))