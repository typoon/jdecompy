import struct
from cp.constantpoolentry import ConstantPoolEntry

class StringInfo(ConstantPoolEntry):

    """
    string_index - is an index pointing inside the constant pool to an
                   Utf8Info structure
    """
    string_index = 0  # 2 bytes

    def __init__(self):
        super().__init__()
        self.string_index = 0

    def populate(self, f):
        self.string_index = int.from_bytes(f.read(2), byteorder='big')
        return 2

    def get_string(self):
        return ''.join([chr(x) for x in self._constant_pool.entries[self.string_index].bytes])

    def __str__(self):
        ret = 'StringInfo: ' + self.get_string()
        ret += ' [string_index: %d]' % self.string_index
        return ret

    def get_bytes(self):
        ret = super().get_bytes()
        
        ret += struct.pack(">h", self.string_index)
        
        return ret
