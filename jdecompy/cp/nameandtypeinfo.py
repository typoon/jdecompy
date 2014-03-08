import struct
from cp.constantpoolentry import ConstantPoolEntry

class NameAndTypeInfo(ConstantPoolEntry):

    """
    class_index - is an index pointing into the constant pool to
                  an Utf8Info structure representing the name of
                  method or field
    descriptor_index - is an index pointing into the constant pool to
                       an Utf8Info structure that represents the method
                       return type and arguments or the field type
    """
    class_index = 0       # 2 byes
    descriptor_index = 0  # 2 bytes

    def __init__(self):
        super().__init__()
        self.class_index = 0
        self.descriptor_index = 0

    def populate(self, f):
        self.class_index = int.from_bytes(f.read(2), byteorder='big')
        self.descriptor_index = int.from_bytes(f.read(2), byteorder='big')
        return 4

    def get_class_name(self):
        return self._constant_pool.entries[self.class_index].get_bytes_as_str()

    def get_descriptor(self):
        return self._constant_pool.entries[self.descriptor_index].get_bytes_as_str()

    def __str__(self):
        ret = 'NameAndTypeInfo: '
        ret += self.get_class_name()
        ret += ' ; '
        ret += self.get_descriptor()
        ret += ' [class_index = %d]' % self.class_index
        ret += ' [name_and_type_index = %d]' % self.descriptor_index
        return ret

    def get_bytes(self):
        ret = super().get_bytes()
        
        ret += struct.pack(">h", self.class_index)
        ret += struct.pack(">h", self.descriptor_index)
        
        return ret
