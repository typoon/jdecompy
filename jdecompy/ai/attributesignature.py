import struct
from ai.attributeinfoentry import AttributeInfoEntry

class AttributeSignature(AttributeInfoEntry):
    """
    attribute_name_index - is an index into the constant pool pointing to an Utf8Info structure
    attribute_length - Should always be 2
    constant_value - is an index into the constant pool pointing to an Utf8Info structure
    """
    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        self.signature_index = 0

    def populate(self, f):
        self.signature_index = int.from_bytes(f.read(2), byteorder="big")
        return 2

    def get_bytes(self):
        ret = ret = super().get_bytes()
        ret += struct.pack(">h", self.signature_index)
        return ret
