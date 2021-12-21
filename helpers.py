from logic import *

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

def add(a, b) -> None :
    if sanitizeInput(a, b) :
        numBits = len(b) 

    fullAdders = {}
    # create the full adders
    for x in range(numBits):
        name = "F{0}".format(x)
        fullAdders[name] = FullAdder(name)
    
    # connect the full adder's carry output to the input of the next full adder
    for key, value in fullAdders.items():
        index = int(key[-1])
        if (index < len(fullAdders) - 1) :
            nextKey = "FA{0}".format(index+1)
            value.Cout.connect(fullAdders[nextKey].Cin)
    
    # set the first full adder's carry input to 0
    list(fullAdders.values())[0].Cin.set(0)

    # set each full adders input's to the corresponding bit
    for key, value in fullAdders.items():
        index = int(key[-1])
        position = (len(fullAdders) - 1) - index
        value.A.set(bit(a, position))
        value.B.set(bit(b, position))

    # TODO: implement function to output the results
    print("{0}{1}{2}{3}{4}".format(fullAdders['F3'].Cout.value, fullAdders['F3'].S.value,
                                   fullAdders['F2'].S.value, fullAdders['F1'].S.value, fullAdders['F0'].S.value))

def multiply(a, b) :
    if sanitizeInput(a, b) :
        numBits = len(b)
    
    # need 2 full adders
    fullAdders = {"FA{0}".format(i): FullAdder("FA{0}".format(i)) for i in range(1, numBits*numBits - numBits + 1)}
    # need 4 and gates
    andGates = {"A{0}".format(i): And("A{0}".format(i)) for i in range(1, (numBits*numBits) + 1)}
    
    # configure output of A2 to len(andGates) + 1
    for index in range (2, len(andGates) + 1) :
        if (index <= numBits):
            print("{0}.C connected to F{1}.A".format(list(andGates.values())[index - 1], index-1))
            list(andGates.values())[index - 1].C.connect(list(fullAdders.values())[index - 1].A)
        else :
            print("{0}.C connected to {1}.B".format(list(andGates.values())[index - 1], list(fullAdders.values())[index - numBits - 1]))
            list(andGates.values())[index - 1].C.connect(list(fullAdders.values())[index - numBits - 1].B)

    # connect all the full adders
    for key, value in fullAdders.items() :
        index = int(key.replace('FA',''))

        # if it is the last fa in the row, connect it to the last fa in the next row
        if index % numBits == 0 :
            # skip connecting if it is the last full adder
            if (index != len(fullAdders)) :
                value.Cout.connect(list(fullAdders.values())[index + numBits - 1].A)
            # set last FA of first row to 0
            if index == numBits :
                print("FA{0}.A set to 0".format(index))
                value.A.set(0)
        else :
            # firstInRow holds the indexes of the first FA in each row. Set these FA's
            # Cin to 0
            firstInRow = [4*i - 3 for i in range(1, (len(fullAdders)//numBits) + 1)]
            if (index in firstInRow) :
                print("FA{0}.Cin set to 0".format(index))
                value.Cin.set(0)
            # connect FA(n-1) Cout to Fa(n) Cin
            value.Cout.connect(list(fullAdders.values())[index - 1].Cin)

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
        
        #print(bit(b,allPositions[index-1]))
        print("A{0}.A set to {1}".format(index, bit(b, allBPositions[index-1])))
        value.A.set(bit(b, allBPositions[index-1]))
        print("A{0}.B set to {1}".format(index, bit(a, allAPositions[index - 1])))
        value.B.set(bit(a, allAPositions[index - 1]))

    # TODO: implement function to output the results
    toString(fullAdders, andGates, numBits)
    #print("{0}{1}{2}{3}".format(fullAdders['FA2'].Cout.value, fullAdders['FA2'].S.value, fullAdders['FA1'].S.value, andGates['A1'].C.value))

def test2BitMult(a, b) :
    a1 = And("a1")
    a2 = And("a2")
    a3 = And("a3")
    a4 = And("a4")

    fa1 = FullAdder("fa1")
    fa2 = FullAdder("fa2")

    a2.C.connect(fa1.A)
    a3.C.connect(fa1.B)
    a4.C.connect(fa2.B)

    fa1.Cout.connect(fa2.Cin)

    fa1.Cin.set(0)
    fa2.A.set(0)

    a1.A.set(1)
    a1.B.set(1)
    a2.A.set(1)
    a2.B.set(1)
    a3.A.set(1)
    a3.B.set(1)
    a4.A.set(1)
    a4.B.set(1)

    print(fa2.Cout.value)
    print(fa2.S.value)
    print(fa1.S.value)
    print(a1.C.value)
    #print("{0}{1}{2}{3}".format(fa2.Cout.value, fa2.S.value, fa1.S.value, a1.C.value))

def test4BitMult(a, b) :
    a1 = And("a1")
    a2 = And("a2")
    a3 = And("a3")
    a4 = And("a4")
    a5 = And("a5")
    a6 = And("a6")
    a7 = And("a7")
    a8 = And("a8")
    a9 = And("a9")
    a10 = And("a10")
    a11 = And("a11")
    a12 = And("a12")
    a13 = And("a13")
    a14 = And("a14")
    a15 = And("a15")
    a16 = And("a16")

    fa1 = FullAdder("fa1")
    fa2 = FullAdder("fa2")
    fa3 = FullAdder("fa3")
    fa4 = FullAdder("fa4")
    fa5 = FullAdder("fa5")
    fa6 = FullAdder("fa6")
    fa7 = FullAdder("fa7")
    fa8 = FullAdder("fa8")
    fa9 = FullAdder("fa9")
    fa10 = FullAdder("fa10")
    fa11 = FullAdder("fa11")
    fa12 = FullAdder("fa12")

    a2.C.connect(fa1.A)
    a3.C.connect(fa2.A)
    a4.C.connect(fa3.A)
    a5.C.connect(fa1.B)
    a6.C.connect(fa2.B)
    a7.C.connect(fa3.B)
    a8.C.connect(fa4.B)
    a9.C.connect(fa5.B)
    a10.C.connect(fa6.B)
    a11.C.connect(fa7.B)
    a12.C.connect(fa8.B)
    a13.C.connect(fa9.B)
    a14.C.connect(fa10.B)
    a15.C.connect(fa11.B)
    a16.C.connect(fa12.B)

    fa1.Cout.connect(fa2.Cin)

    fa1.Cin.set(0)
    fa2.A.set(0)

    a1.A.set(1)
    a1.B.set(1)
    a2.A.set(1)
    a2.B.set(1)
    a3.A.set(1)
    a3.B.set(1)
    a4.A.set(1)
    a4.B.set(1)

    print(fa2.Cout.value)
    print(fa2.S.value)
    print(fa1.S.value)
    print(a1.C.value)
    #print("{0}{1}{2}{3}".format(fa2.Cout.value, fa2.S.value, fa1.S.value, a1.C.value))

def toString(fullAdders, andGates, numBits) :
    for i in range(len(fullAdders), len(andGates) - numBits, -1) :
        key = "F{0}".format(i)
        print(key)




    


    




