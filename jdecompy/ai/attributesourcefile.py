import struct
from ai.attributeinfoentry import AttributeInfoEntry


class AttributeSourceFile(AttributeInfoEntry):
    """
    sourcefile_index - should be an index into the constant pool pointing to an Utf8Info structure that represents
                       the name of the file from which this class was compiled
    """
    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        self.sourcefile_index = 0  # 2 bytes

    def populate(self, f):
        self.sourcefile_index = int.from_bytes(f.read(2), byteorder="big")
        return 2

    def get_bytes(self):
        ret = ret = super().get_bytes()
        ret += struct.pack(">h", self.sourcefile_index)
        return ret
