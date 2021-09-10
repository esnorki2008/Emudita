from cpu import Cpu

class Bus():
    def __init__(self):
        self.cpu = None
        self.ram = range(0x0000,0xFFFF)

    def addCPU(self):
        self.cpu = Cpu()
        self.cpu.connectBus(self)

    def write(self,address,data):
        """
            Writing to ram
        """
        if address >= 0x0000 and address <= 0xFFFF:
            self.ram[address] = data
        else:
            print("Invalid address")


    def read(self,address,readOnly=False):
        if address >= 0x0000 and address <= 0xFFFF:
            return self.ram[address] 
        else:
            print("Invalid address")
            return 0x00