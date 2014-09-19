import struct
from ai.attributeinfoentry import AttributeInfoEntry


class AttributeEnclosingMethod(AttributeInfoEntry):
    """
    class_index - should be an index into the constant pool pointing to a ClassInfo structure
    method_index - should be an index into the constant pool pointing to a NameAndTypeInfo structure
    """
    class_index  = 0 # 2 bytes
    method_index = 0 # 2 bytes

    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        self.class_index = 0   # 2 bytes
        self.method_index = 0  # 2 bytes

    def populate(self, f):
        self.class_index = int.from_bytes(f.read(2), byteorder="big")
        self.method_index = int.from_bytes(f.read(2), byteorder="big")
        return 4

    def get_bytes(self):
        ret = super().get_bytes()
        ret += struct.pack(">h", self.class_index)
        ret += struct.pack(">h", self.method_index)
        return ret
