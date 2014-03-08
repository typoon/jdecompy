import struct
from cp.constantpoolentry import ConstantPoolEntry


class ClassInfo(ConstantPoolEntry):

    """
    name_index - is an index pointing inside the constant pool to an
                 Utf8Info structure
    """
    name_index = 0

    def __init__(self):
        super().__init__()
        self.name_index = 0  # 2 bytes

    def populate(self, f):
        self.name_index = int.from_bytes(f.read(2), byteorder='big')
        return 2

    def get_name(self):
        return ''.join([chr(x) for x in self._constant_pool.entries[self.name_index].bytes])

    def __str__(self):
        ret = 'ClassInfo: '
        ret += self.get_name()
        ret += ' [name_index = %d]' % self.name_index
        return ret
    
    def get_bytes(self):
        ret = super().get_bytes()
        
        ret += struct.pack(">h", self.name_index)
        
        return ret
