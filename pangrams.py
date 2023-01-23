def pangrams(s):
    alphabet = [ 'a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    s = s.lower()
    for i in alphabet:
        if i in s:
            count += 1
    result = 'pangram' if count >= 26 else 'not pangram'
    return result

    
random = "NOVmETKPTbYu ftZPEykhjgF GGkdGjWGwW skjPJsea dtwdqcr DERCUgxOxrRgDQbdzL IZjyXs"

print( pangrams ( random ) )