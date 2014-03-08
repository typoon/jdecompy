import struct
from ai.attributeinfoentry import AttributeInfoEntry


class AttributeExceptions(AttributeInfoEntry):
    """
    number_of_exceptions - The number of exceptions in the exception_index_table
    exception_index_table - A list with indexes into the constant pool pointing to a ClassInfo structure
    """
    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        self.number_of_exceptions = 0    # 2 bytes
        self.exception_index_table = []  # variable length

    def populate(self, f):
        self.number_of_exceptions = int.from_bytes(f.read(2), byteorder="big")
        for i in range(self.number_of_exceptions):
            self.exception_index_table.append(int.from_bytes(f.read(2), byteorder="big"))

        return 2 + self.number_of_exceptions*2

    def get_bytes(self):
        ret = super().get_bytes()
        ret += struct.pack(">h", self.number_of_exceptions)
        
        for e in self.exception_index_table:
            ret += struct.pack(">h", e)
            
        return ret
