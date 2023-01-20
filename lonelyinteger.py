import collections

def lonelyinteger(a):
    result = [ item for item, count in collections.Counter(a).items() if count == 1 ] 
    return result.pop()


random = [15, 60, 74, 1, 94, 93, 28, 48, 70, 98, 45, 94, 42, 45, 48, 1, 72, 9, 24, 93, 41, 70, 60, 28, 11, 20, 72, 35, 11, 98, 31, 74, 31, 41, 9, 42, 20, 35, 24]

print( lonelyinteger( random) )