import struct
from ai.attributeinfoentry import AttributeInfoEntry

class AttributeSignature(AttributeInfoEntry):
    """
    signature_index - is an index into the constant pool pointing to an Utf8Info structure
    """
    signature_index = 0      # 2 bytes
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
