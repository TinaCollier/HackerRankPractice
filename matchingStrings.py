from itertools import repeat

def matchingStrings(strings, queries):
    length = len( queries )
    count = list( repeat( 0, length ) )
    for i in strings:
        for j in range( len( queries ) ):
            if queries[ j ] == i:
                count[ j ]+= 1
    return count

random = ['ab', 'ab', 'abc']
random1 = ['ab', 'abc', 'bc']

print( matchingStrings( random, random1 ) )