from logic import And, FullAdder, Not, Or, Xor

def testNot() :
    n1 = Not("n1")
    n1.B.monitor = 1

    n1.A.set(1)
    n1.B.set(0)

def testAnd() :
    a1 = And("n1")

    a1.C.monitor = 1
    a1.A.set(1)
    a1.B.set(1)

def testOr() :
    o1 = Or("o1")

    o1.C.monitor = 1
    o1.A.set(1)
    o1.B.set(0)

def testXor() :
    x1 = Xor("x1")

    x1.C.monitor = 1
    x1.A.set(1)
    x1.B.set(1)

def test2BitMult() :
    a1 = And("a1")
    a2 = And("a2")
    a3 = And("a3")
    a4 = And("a4")

    fa1 = FullAdder("fa1")
    fa2 = FullAdder("fa2")

    a4.C.connect(fa2.B)
    a2.C.connect(fa1.A)
    a3.C.connect(fa1.B)
    

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

    print("{0}{1}{2}{3}".format(fa2.Cout.value, fa2.S.value, fa1.S.value, a1.C.value))

def test4BitMult() :
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
    fa2.Cout.connect(fa3.Cin)
    fa3.Cout.connect(fa4.Cin)
    fa4.Cout.connect(fa8.A)
    fa5.Cout.connect(fa6.Cin)
    fa6.Cout.connect(fa7.Cin)
    fa7.Cout.connect(fa8.Cin)
    fa8.Cout.connect(fa12.A)
    fa9.Cout.connect(fa10.Cin)
    fa10.Cout.connect(fa11.Cin)
    fa11.Cout.connect(fa12.Cin)

    fa4.A.set(0)

    fa1.Cin.set(0)
    fa5.Cin.set(0)
    fa9.Cin.set(0)

    a1.A.set(1)
    a1.B.set(1)
    a2.A.set(1)
    a2.B.set(1)
    a3.A.set(1)
    a3.B.set(1)
    a4.A.set(1)
    a4.B.set(1)
    a5.A.set(1)
    a5.B.set(1)
    a6.A.set(1)
    a6.B.set(1)
    a7.A.set(1)
    a7.B.set(1)
    a8.A.set(1)
    a8.B.set(1)
    a9.A.set(1)
    a9.B.set(1)
    a10.A.set(1)
    a10.B.set(1)
    a11.A.set(1)
    a11.B.set(1)
    a12.A.set(1)
    a12.B.set(1)
    a13.A.set(1)
    a13.B.set(1)
    a14.A.set(1)
    a14.B.set(1)
    a15.A.set(1)
    a15.B.set(1)
    a16.A.set(1)
    a16.B.set(1)

    print("{0}{1}{2}{3}{4}{5}{6}{7}".format(fa12.Cout.value, fa12.S.value, fa11.S.value,
            fa10.S.value, fa9.S.value, fa5.S.value, fa1.S.value, a1.C.value))