import struct
from constants import *
from cp.constantpoolentry import ConstantPoolEntry

class NameAndTypeInfo(ConstantPoolEntry):

    """
    name_index - is an index pointing into the constant pool to
                  an Utf8Info structure representing the name of
                  method or field
    descriptor_index - is an index pointing into the constant pool to
                       an Utf8Info structure that represents the method
                       return type and arguments or the field type
    """
    name_index = 0       # 2 byes
    descriptor_index = 0  # 2 bytes

    def __init__(self):
        super().__init__(CONSTANT_NAMEANDTYPE)
        self.name_index = 0
        self.descriptor_index = 0

    def populate(self, f):
        self.name_index = int.from_bytes(f.read(2), byteorder='big')
        self.descriptor_index = int.from_bytes(f.read(2), byteorder='big')
        return 4

    def get_name(self):
        print("Name index: %d" % self.name_index)
        return self._constant_pool.entries[self.name_index].get_bytes_as_str()

    def get_descriptor(self):
        return self._constant_pool.entries[self.descriptor_index].get_bytes_as_str()

    def __str__(self):
        ret = 'NameAndTypeInfo: '
        ret += self.get_name()
        ret += ' ; '
        ret += self.get_descriptor()
        ret += ' [name_index = %d]' % self.name_index
        ret += ' [name_and_type_index = %d]' % self.descriptor_index
        return ret

    def get_bytes(self):
        ret = super().get_bytes()

        ret += struct.pack(">h", self.name_index)
        ret += struct.pack(">h", self.descriptor_index)

        return ret
