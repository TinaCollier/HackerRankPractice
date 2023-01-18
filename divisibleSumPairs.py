random1 = [1,2,3,4,5,6]
from itertools import combinations

def divisibleSumPairs( n, k, ar ):
    count = 0
    ar.sort()
    result = combinations(ar, 2)
    for i in list(result):
        if sum( i ) % k == 0:
            count += 1
    return count

print( divisibleSumPairs( 6, 5, random1 ) )