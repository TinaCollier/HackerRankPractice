random1 = 'C;V;can of coke'
random2 = 'S;M;sweatTea()'
random3 = 'S;V;epsonPrinter'
random4 = 'C;M;santa claus'
random5 = 'C;C;mirror'
random6 = 'S;C;LargeSoftwareBook'


def convert( string ):
    import re
    array =  string.split(';')
    first = array[ 0 ]
    second = array[ 1 ]
    phrase = array[ 2 ]
    if first == 'S':
        if second == 'M':
            phrase = phrase[ :-2 ]
            splitPhrase = " ".join(filter(len, re.split(r'([A-Z][a-z]+)', phrase)))
            return splitPhrase.lower()
        elif second == 'C' or array[ 1 ] == 'V':
            splitPhrase = " ".join(filter(len, re.split(r'([A-Z][a-z]+)', phrase)))
            return splitPhrase.lower()
    elif first == 'C':
        spaceIndices = [ i for i , x in enumerate( phrase ) if x == ' ']
        if second == 'M':
            for i in spaceIndices:
                i += 1
                phrase = phrase[ :i ] + phrase[ i ].upper() + phrase[ i + 1: ]
            return phrase.replace(' ', '') + '()'
        elif second == 'C':
            phrase = phrase.capitalize()
            for i in spaceIndices:
                i += 1
                phrase = phrase[ :i ] + phrase[ i ].upper() + phrase[ i + 1: ]
            return phrase.replace(' ', '')
        elif second == 'V':
            for i in spaceIndices:
                i += 1
                phrase = phrase[ :i ] + phrase[ i ].upper() + phrase[ i + 1: ]
            return phrase.replace(' ', '')


print( convert( random1 ) )
print( convert( random2 ) )
print( convert( random3 ) )
print( convert( random4 ) )
print( convert( random5 ) )
print( convert( random6 ) )