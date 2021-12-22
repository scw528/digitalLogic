from logic import FullAdder, And
from helpers import bit, sanitizeInput, twosCompliment, toString

def add(a, b) -> None :
    """
        add() will compute the addition of 2 n-bit binary strings

        :param a: binary string a
        :param b: binary string b
        
        :return: sum of a and b in binary
    """ 
    if sanitizeInput(a, b) :
        numBits = len(b) 

    fullAdders = {}
    # create the full adders
    for x in range(numBits):
        name = "FA{0}".format(x)
        fullAdders[name] = FullAdder(name)
    
    # connect the full adder's carry output to the input of the next full adder
    for key, value in fullAdders.items():
        index = int(key[-1])
        if (index < len(fullAdders) - 1) :
            value.Cout.connect(list(fullAdders.values())[index + 1].Cin)
    
    # set the first full adder's carry input to 0
    list(fullAdders.values())[0].Cin.set(0)

    # set each full adders input's to the corresponding bit
    for key, value in fullAdders.items():
        index = int(key[-1])
        position = (len(fullAdders) - 1) - index
        value.A.set(bit(a, position))
        value.B.set(bit(b, position))

    return toString(fullAdders, {})

def subtract(a, b) -> None :
    """
        subtract() will compute the subtraction of 2 n-bit binary strings

        :param a: binary string a
        :param b: binary string b
        
        :return: difference of a and b in binary (a - b)
    """ 
    if sanitizeInput(a, b) :
        numBits = len(b)

    twosCompB = twosCompliment(b)
    return add(a, twosCompB)

def multiply(a, b) :
    """
        multiply() will compute the product of 2 n-bit binary strings

        :param a: binary string a
        :param b: binary string b
        
        :return: product of a and b in binary (a - b)
    """
    if sanitizeInput(a, b) :
        numBits = len(b)
    
    # create all full adders
    fullAdders = {"FA{0}".format(i): FullAdder("FA{0}".format(i)) for i in range(1, numBits*numBits - numBits + 1)}
    # create all and gates
    andGates = {"A{0}".format(i): And("A{0}".format(i)) for i in range(1, (numBits*numBits) + 1)}

    # configure output of andGates A2 to len(andGates) + 1
    for index in range (2, len(andGates) + 1) :
        if (index <= numBits):
            list(andGates.values())[index - 1].C.connect(list(fullAdders.values())[index - 2].A)
        else :
            list(andGates.values())[index - 1].C.connect(list(fullAdders.values())[index - numBits - 1].B)

    # firstInRow holds the indexes of the first FA in each row (right to left, top to bottom). Set these FA's Cin to 0
    ''' 
        numBits   |   firstInRowIndexes
        _______________________________
            2     |     [1]
            3     |     [1 ,4]
            4     |     [1, 5, 9]
    '''
    firstInRowIndexes = [numBits*i - (numBits - 1) for i in range(1, (len(fullAdders)//numBits) + 1)]
    # hold the last row of FA's. numFA - numBits
    '''
        numBits   |   lastRowIndexes
        _______________________________
            2     |     [1, 2]
            3     |     [4, 5, 6]
            4     |     [9, 10, 11, 12]
    '''
    lastRowIndexes = [i for i in range(len(fullAdders) - numBits + 1, len(fullAdders) + 1)]
    
    # connect all the full adders
    for key, value in fullAdders.items() :
        index = int(key.replace('FA',''))

        # if it is the last fa in the row, connect it to the last fa in the next row
        if index % numBits == 0 :
            # for 4x4 bits, this will be indexes 4, 8
            # skip connecting if it is the last full adder
            if (index != len(fullAdders)) and (len(fullAdders) > numBits):
                # connect FA's cout to the left most FA-A below
                value.Cout.connect(list(fullAdders.values())[index + (numBits - 1)].A)

                # if numBits > 2, connect the last FA in the first numBits/2 rows
                value.S.connect(list(fullAdders.values())[index + (numBits - 1) - 1].A)
            # set last FA of first row to 0
            if index == numBits :
                # set the last FA.A in the first row to 0
                value.A.set(0)
        else :
            # for 4x4 bits, this will be indexes 2,3,6,7
            if index in firstInRowIndexes :
                # set the Cin for the index of the first row of FA of each index. ex: [1,5,9] for 4bits X 4bits
                value.Cin.set(0)
            
            if (len(fullAdders) > numBits) and (index not in firstInRowIndexes) and (index not in lastRowIndexes) :
                # connect its Sum to below FA (if it exists)
                value.S.connect(list(fullAdders.values())[index + (numBits - 1) - 1].A)

            # connect FA(n-1) Cout to Fa(n) Cin
            value.Cout.connect(list(fullAdders.values())[index].Cin)
    
    # list to hold all possile positions of an input bit
    inputBitBPositions = [i for i in range(numBits)]

    # list to hold the position of all B input bits, in reversed order (right most bit first)
    allBPositions = [item for item in inputBitBPositions for i in range(numBits)]
    allBPositions.reverse()

    # list to hold the position of all A input bits, in reversed order (right most bit first)
    allAPositions = [i for i in range(numBits)] * numBits
    allAPositions.reverse()

    # set all and gates input
    for key, value in andGates.items():
        index = int(key.replace('A',''))
        value.A.set(bit(b, allBPositions[index - 1]))
        value.B.set(bit(a, allAPositions[index - 1]))

    # call function to output the results
    return toString(fullAdders, andGates)

'''
    ****************************************************
    *                                                  *
    *   Below you will find all the helper functions   *
    *                                                  *
    ****************************************************
'''
def bit(x, bit) :
    """
        bit() returns the value of a bit string at index bit

        :param x: binary string
        :param bit: position of x you wish to return
        
        :return: value of binary string at position bit
    """
    if x[bit] == '1':
        return 1
    else : 
        return 0

def sanitizeInput(a, b) -> bool :
    """
        sanitizeInput() ensures that both input binary strings are of equal length

        :param a: binary string a
        :param b: binary string b
        
        :return: True if valid, else raise error
    """
    lenA = len(a)
    lenB = len(b)

    if (lenA != lenB):
        raise ValueError('Number of bits must be equal. Please try again.')
    else :
        return True

def twosCompliment(bitString) :
    """
        twosCompliment() returns the 2's Compliment of a binary string

        :param bitString: binary string
        
        :return: negative (2's compliment) value of input
    """
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
    """
        toString() returns the output value for addition and multiplication

        :param fullAdders: dict of full adders
        :param andGates: dict of and gates
        
        :return: value of what is being added/multipled
    """
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




    


    




