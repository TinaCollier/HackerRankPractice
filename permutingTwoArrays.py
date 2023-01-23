def twoArrays(k, A, B):
    A.sort( reverse = True )
    B.sort()
    for i in range( len( A ) ):
        if ( A[ i ] + B[ i ] < k ):
            return 'NO'
    return 'YES'
    
random = [1,2,2,1]
random2 = [3,3,3,4]

print( twoArrays ( 5, random, random2 ) )