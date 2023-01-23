def sockMerchant(n, ar):
    counts = 0
    for i in set( ar ):
        counts += ( ar.count( i ) // 2)
    return counts
            
    
random = [1,1,3,1,2,1,3,3,3,3]
random2 = [3,3,3,4]

print( sockMerchant ( 10, random ) )