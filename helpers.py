from logic import Not
from store import add

def bit(x, bit) :
    if x[bit] == '1':
        return 1
    else : 
        return 0

def sanitizeInput(a, b) -> bool :
    lenA = len(a)
    lenB = len(b)

    if (lenA != lenB):
        raise ValueError('Number of bits must be equal. Please try again.')
    else :
        return True

def twosCompliment(bitString) :
    # to preform this, we must flip all the bits and add one. return the result
    numBits = len(bitString)
    # string to hold the flipped input bitString
    flippedBitString = ""
    # string to hold 1. This will be added to the flippedBitString
    one = "0" * (numBits - 1)
    one += "1"
    # flip all the bits using our Not gate
    bitList = [bit for bit in bitString]
    notGates = {"N{0}".format(i): Not("N{0}".format(i)) for i in range(1, numBits + 1)}
    
    for key, value in notGates.items() :
        index = int(key.replace('N',''))
        value.A.set(int(bitList[index - 1]))
    
    for key, value in notGates.items() :
        flippedBitString = flippedBitString + str(value.B.value)

    twosCompliment = add(flippedBitString, one)
    
    return twosCompliment

def toString(fullAdders, andGates) :
    # output will hold the output bits in reverse order
    output = []

    # first and gate will always be the lowest bit (farthest right).
    if bool(andGates) :
        output.append(list(andGates.values())[0].C.value)

    for key, value in fullAdders.items() :
        index = int(key.replace('FA',''))
        if len(value.S.connects) == 0:
            # append FA.S.value to the output list if S does not connect to anything
            output.append(value.S.value)
            if index == len(fullAdders):
                # append FA.Cout.value to the output list if it is the last FA
                output.append(value.Cout.value)

    
    output.reverse()
    outputString = "".join(map(str, output))
    
    return outputString