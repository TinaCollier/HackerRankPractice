from itertools import repeat

def migratoryBirds(arr):
    types = list( repeat( 0 , max( arr ) ) )
    for i in arr:
        types[ i - 1 ] += 1
    max_value = max( types )
    index = types.index( max_value ) + 1
    return index

            
    
random = [1,1,2,2,3]
random2 = [3,3,3,4]

print( migratoryBirds ( random ) )