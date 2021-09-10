class Cpu:
    def __init__(self):
        self.bus = None

        """
                    Processor flags
        Bits: 7   6   5   4   3   2   1   0

                                        |e├─── Emulation: 0 = Native Mode
            |n| |v| |m| |x| |d| |i| |z| |c|
            └┼───┼───┼───┼───┼───┼───┼───┼┘
            │   │   │   │   │   │   │   └──────── Carry: 1 = Carry set
            │   │   │   │   │   │   └───────────── Zero: 1 = Result is zero
            │   │   │   │   │   └────────── IRQ Disable: 1 = Disabled
            │   │   │   │   └───────────── Decimal Mode: 1 = Decimal, 0 = Hexadecimal
            │   │   │   └──────── Index Register Select: 1 = 8-bit, 0 = 16-bit
            │   │   └─────────────── Accumulator Select: 1 = 8-bit, 0 = 16-bit
            │   └───────────────────────────── Overflow: 1 = Overflow set
            └───────────────────────────────── Negative: 1 = Negative set
        """
        # Carry, Zero, Disable, Decimal, Index, Accumulator, Overflow, Negative
        self.flags = 0b00000000
        self.a = 0x00
        self.x = 0x00
        self.y = 0x00
        self.stackPtr = 0x00
        self.programCounter = 0x00
        self.status = 0x00



    def connectBus(self, bus):
        """Add the bus to the CPU"""
        self.bus = bus

    def read(self, address):
        """Read from the bus"""
        return self.bus.read(address)

    def write(self, address, data):
        """Write to the bus"""
        self.bus.write(address, data)
    
    """Addressing Modes"""
    def IMP(self):
        pass
    def IMM(self):
        pass
    def ZP0(self):
        pass
    def ZPX(self):
        pass
    def ZPY(self):
        pass
    def REL(self):
        pass
    def ABS(self):
        pass
    def ABX(self):
        pass
    def ABY(self):
        pass
    def IND(self):
        pass
    def IZX(self):
        pass
    def IZY(self):
        pass

    """Opcodes"""
    def ADC(self):
        pass

    def AND(self):
        pass

    def ASL(self):
        pass

    def BCC(self):
        pass
    #


    
    def BCS(self):
        pass

    def BEQ(self):
        pass

    def BIT(self):
        pass

    def BMI(self):
        pass

    #

    def BNE(self):
        pass

    def BPL(self):
        pass

    def BRK(self):
        pass


    def ILLEGAL(self):
        """ Activited in case Illegal Opcode"""
        pass