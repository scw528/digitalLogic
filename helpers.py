from logic import *

def bit(x, bit) :
    return x[bit] == '1'

def add(a, b) :
    lenA = len(a)
    lenB = len(b)

    if (lenA != lenB):
        raise ValueError('Number of bits must be equal. Please try again.')
    else :
        numBits = lenB 

    fullAdders = {}
    for x in range(numBits):
        name = "F{0}".format(x)
        fullAdders[name] = FullAdder(name)
    
    for key, value in fullAdders.items():
        index = int(key[-1])
        if (index < len(fullAdders) - 1) :
            nextKey = "F{0}".format(index+1)
            value.Cout.connect(fullAdders[nextKey].Cin)
    
    list(fullAdders.values())[0].Cin.set(0)

    for key, value in fullAdders.items():
        index = int(key[-1])
        position = (len(fullAdders) - 1) - index
        value.A.set(bit(a, position))
        value.B.set(bit(b, position))

    # TODO: implement function to output the results
    print("{0}{1}{2}{3}{4}".format(fullAdders['F3'].Cout.value, fullAdders['F3'].S.value,
                                   fullAdders['F2'].S.value, fullAdders['F1'].S.value, fullAdders['F0'].S.value))


