import struct
from cp.constantpoolentry import ConstantPoolEntry

class IntegerInfo(ConstantPoolEntry):

    """
    value - is the value of the integer
    """
    value = 0 # 4 bytes

    def __init__(self):
        super().__init__()
        self.value = 0  # 4 bytes

    def populate(self, f):
        self.value = int.from_bytes(f.read(4), byteorder='big')
        return 4

    def __str__(self):
        ret = 'IntegerInfo: %d' % self.value
        return ret

    def get_bytes(self):
        ret = super().get_bytes()
        
        ret += struct.pack(">I", self.value)
        
        return ret
