import struct
from cp.constantpoolentry import ConstantPoolEntry
from cp.constantpoolutils import ConstantPoolUtils

class InterfaceMethodRefInfo(ConstantPoolEntry):

    """
    class_index - is an index pointing inside the constant pool to a
                  ClassInfo structure
    name_and_type_index - is an index pointing inside the constant pool
                          to a NameAndTypeInfo structure
    """
    class_index = 0          # 2 bytes
    name_and_type_index = 0  # 2 bytes

    def __init__(self):
        super().__init__()
        self.class_index = 0
        self.name_and_type_index = 0

    def populate(self, f):
        self.class_index = int.from_bytes(f.read(2), byteorder='big')
        self.name_and_type_index = int.from_bytes(f.read(2), byteorder='big')
        return 4

    def get_class_name(self):
        return self._constant_pool.entries[self.class_index].get_name()

    def get_method_name(self):
        return self._constant_pool.entries[self.name_and_type_index].get_class_name()

    def get_method_type(self):
        info = self._constant_pool.entries[self.name_and_type_index].get_descriptor()
        return ConstantPoolUtils.parse_method_type(info)

    def get_method_signature(self):
        method_type = self.get_method_type()
        method_name = self.get_method_name()

        s = ', '.join(method_type['params'])
        r = method_type['ret_type'] + ' ' + method_name + '(' + s + ')'
        return r

    def __str__(self):
        ret = 'InterfaceMethodRefInfo: '
        ret += self.get_method_signature()
        ret += ' [class_index = %d]' % self.class_index
        ret += ' [name_and_type_index = %d]' % self.name_and_type_index
        return ret

    def get_bytes(self):
        ret = super().get_bytes()
        
        ret += struct.pack(">h", self.class_index)
        ret += struct.pack(">h", self.name_and_type_index)
        
        return ret
