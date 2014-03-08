import struct
from cp.constantpoolentry import ConstantPoolEntry

class LongInfo(ConstantPoolEntry):

    def __init__(self):
        super().__init__()
        self.high = 0  # 4 bytes
        self.low = 0   # 4 bytes

    def populate(self, f):
        self.high = int.from_bytes(f.read(4), byteorder='big')
        self.low = int.from_bytes(f.read(4), byteorder='big')
        return 8

    def get_bytes(self):
        ret = super().get_bytes()
        
        ret += struct.pack(">I", self.high)
        ret += struct.pack(">I", self.low)
        
        return ret
