def pageCount( n, p ):
    return min( n // 2 - p // 2, p // 2 )

random = 6
random2 = 2

print( pageCount ( random, random2 ) )