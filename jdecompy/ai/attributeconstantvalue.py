import struct
from ai.attributeinfoentry import AttributeInfoEntry

class AttributeConstantValue(AttributeInfoEntry):
    """
    attribute_name_index - is an index into the constant pool pointing to an Utf8Info structure
    attribute_length - Should always be 2
    constant_value - is an index into the constant pool that can point to either a LongInfo, DoubleInfo, FloatInfo,
                     IntegerInfo or StringInfo
    """
    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        self.constant_value_index = 0  # 2 bytes

    def populate(self, f):
        self.constant_value_index = int.from_bytes(f.read(2), byteorder="big")
        return 2

    def get_bytes(self):
        ret = super().get_bytes()
        ret += struct.pack(">h", self.constant_value_index)
        return ret
