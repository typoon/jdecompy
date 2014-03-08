import struct
from constants import *
from cp.constantpoolentry import ConstantPoolEntry

class Utf8Info(ConstantPoolEntry):

    """
    length - represents the number of bytes in the 'bytes' property
    bytes - is the UTF-8 representation of a string
    """
    length = 0
    bytes = 0

    def __init__(self):
        super().__init__(CONSTANT_UTF8)
        self.length = 0  # 2 bytes
        self.bytes = b''

    def populate(self, f):
        self.length = int.from_bytes(f.read(2), byteorder='big')
        self.bytes = f.read(self.length)
        return 2 + self.length

    def get_bytes_as_str(self):
        return ''.join([chr(i) for i in self.bytes])

    def __str__(self):
        ret = 'Utf8Info: '
        ret += ''.join([chr(i) for i in self.bytes])
        return ret

    def get_bytes(self):
        ret = super().get_bytes()
        
        ret += struct.pack(">h", self.length)
        ret += self.bytes
        
        return ret
