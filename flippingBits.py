def flippingBits(n):
    binary = '{:032b}'.format( n )
    binaryArray = [ int( x ) for x in str( binary ) ]
    flippedArray = []
    for i in binaryArray:
        if i == 1:
           flippedArray.append( 0 )
        elif i == 0:
            flippedArray.append( 1 )
    binaryResult = ''.join([ str(x) for x in flippedArray ])
    return int( binaryResult, 2 )
    
random = 2147483647

print( flippingBits ( random ) )