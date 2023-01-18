random = [-4, 3, -9, 0, 4, 1]

def plusMinus( arr ):
    result = [ 0, 0, 0 ]
    for number in arr: 
        if number > 0:
            result[ 0 ] +=1 
        elif number < 0:
            result[ 1 ] += 1
        else:
            result[ 2 ] += 1
    for i in result:
        print( format( i/len( arr ), '.6f' ) )

plusMinus( random )