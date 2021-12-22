# Connector will connect from a component's output, to the next component's input.
class Connector :
    def __init__(self, owner, name, activates=0, monitor=0) :
        self.value = None
        self.owner = owner
        self.name = name
        self.activates = activates
        self.monitor = monitor
        self.connects = []

    def connect(self, inputs) :
        # ensure that inputs is a list
        if not isinstance(inputs, list):
            inputs = [inputs]
        for input in inputs:
            self.connects.append(input)

    def set(self, value):
        # commenting these lines will result in slower computation. However, it fixes the issue of some values not getting set.
        if self.value == value:
            return
        self.value = value
        if self.activates:
            self.owner.evaluate()
        if self.monitor and (self.value != None):
            # set the new value of the values dict
            # self.owner.values[self.name] = self.value
            print("{0}-{1} set to {2}".format(self.owner.name, self.name, self.value))
        for con in self.connects:
            if value == True:
                value = 1
            elif value == False:
                value = 0
            con.set(value)

class LogicCircuit :
    def __init__(self, name) :
        self.name = name
    
    def evaluate(self):
        return

class Gate(LogicCircuit) :
    def __init__(self, name) :
        LogicCircuit.__init__(self, name)
        self.A = Connector(self, "A", activates=1)
        self.B = Connector(self, "B", activates=1)
        self.C = Connector(self, "C")

class Not(LogicCircuit) :
    def __init__(self, name)  :
        LogicCircuit.__init__(self, name)
        self.A = Connector(self, "A", activates=1)
        self.B = Connector(self, "B")
    
    def evaluate(self) :
        boolValue = self.A.value
        if boolValue == True or boolValue == 1:
            self.B.set(0)
        elif boolValue == False or boolValue == 0:
            self.B.set(1)
        elif boolValue == None:
            self.B.set(None)

"""
              xxxxxxxxx
A             x        xx
 xxxxxxxxxxxxxx         xx
              x          x xxxxxxxxx
 xxxxxxxxxxxxxx         xx          C
B             x        xx
              xxxxxxxxx

"""
class And(Gate) :
    def __init__(self, name)  :
        Gate.__init__(self, name)

    def evaluate(self) :
        self.C.set(self.A.value and self.B.value)


"""

A             xxxxxxxxxx
 xxxxxxxxxxxxxxx        x
                x        x
                x        x xxxxxxxxxx
                x        x           C
 xxxxxxxxxxxxx x        x
B             xxxxxxxxxx

"""
class Or(Gate):
    def __init__(self, name)  :
        Gate.__init__(self, name)

    def evaluate(self):
        self.C.set(self.A.value or self.B.value)
    
"""

A             x xxxxxxxx
 xxxxxxxxxxxxx x x      x
                x x      x
                x x      x xxxxxxxxxx
                x x      x           C
 xxxxxxxxxxxxx x x      x
B             x xxxxxxxx

"""
class Xor(Gate):
    def __init__(self, name):
        Gate.__init__(self, name)
        self.A1 = And("A1")
        self.A2 = And("A2")
        self.N1 = Not("N1")
        self.N2 = Not("N2")
        self.O1 = Or("O1")
        self.A.connect([self.A1.A, self.N2.A])
        self.B.connect([self.N1.A, self.A2.A])
        self.N1.B.connect([self.A1.B])
        self.N2.B.connect([self.A2.B])
        self.A1.C.connect([self.O1.A])
        self.A2.C.connect([self.O1.B])
        self.O1.C.connect([self.C])

class HalfAdder(LogicCircuit) :
    def __init__(self, name)  :
        LogicCircuit.__init__(self, name)
        self.A = Connector(self, "A", activates=1)
        self.B = Connector(self, "B", activates=1)
        self.S = Connector(self, "S")
        self.C = Connector(self, "C")
        self.X1 = Xor("X1")
        self.A1 = And("A1")
        self.A.connect([self.X1.A, self.A1.A])
        self.B.connect([self.X1.B, self.A1.B])
        self.X1.C.connect([self.S])
        self.A1.C.connect([self.C])

# 2 half adders and 1 or
class FullAdder(LogicCircuit) :
    def __init__(self, name) :
        LogicCircuit.__init__(self, name)
        self.Cin = Connector(self, "Cin", activates=1, monitor=1)
        self.A = Connector(self, "A", activates=1, monitor=1)
        self.B = Connector(self, "B", activates=1, monitor=1)
        self.Cout = Connector(self, "Cout", monitor=1)
        self.S = Connector(self, "S", monitor=1)
        self.H1 = HalfAdder("H1")
        self.H2 = HalfAdder("H2")
        self.O1 = Or("O1")
        self.Cin.connect([self.H2.A])
        self.A.connect([self.H1.A])
        self.B.connect([self.H1.B])
        self.H1.S.connect(self.H2.B)
        self.H1.C.connect(self.O1.B)
        self.H2.S.connect(self.S)
        self.H2.C.connect(self.O1.A)
        self.O1.C.connect(self.Cout)
    





        



