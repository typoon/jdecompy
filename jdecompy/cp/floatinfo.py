import struct
from cp.constantpoolentry import ConstantPoolEntry

class FloatInfo(ConstantPoolEntry):

    def __init__(self):
        super().__init__()
        self.value = 0  # 4 bytes

    def populate(self, f):
        self.value = float(int.from_bytes(f.read(4), byteorder='big'))
        return 4

    def __str__(self):
        ret = 'FloatInfo: %f' % self.value
        return ret

    def get_bytes(self):
        ret = super().get_bytes()
        
        ret += struct.pack(">f", self.value)
        
        return ret
