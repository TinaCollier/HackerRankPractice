from itertools import repeat

def gradingStudents(grades):
    length = len( grades )
    results = list( repeat( 0, length) )
    for i in range( len( grades ) ):
        if grades[ i ] < 38:
            results[ i ] = grades[ i ]
        elif grades[ i ] % 5 <= 2:
            results[ i ] = grades[ i ]
        else: 
            results[ i ] = round(grades[ i ] / 5) * 5
    return results


random = [73, 67, 38, 33]

print( gradingStudents ( random ) )