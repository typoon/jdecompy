from ai.attributeinfoentry import AttributeInfoEntry
import attributeinfo
import struct

class AttributeCode(AttributeInfoEntry):
    """
    max_stack - maximum size of the stack for this method
    max_locals - maximum number of local variables
    code_length - amount of bytes in the code list
    code - list of bytes that represent the code
    exception_table_length - number of elements in the exception_table
    exception_table -
    attributes_count - number of attributes associated with the code
    attributes - list of AttributeInfoEntry structures
    """
    max_stack = 0    # 2 bytes
    max_locals = 0   # 2 bytes
    code_length = 0  # 4 bytes
    code = b''        # variable
    exception_table_length = 0  # 2 bytes
    exception_table = []  # variable
    attributes_count = 0  # 2 bytes
    attributes = None

    class ExceptionTable:
        def __init__(self):
            self.start_pc = 0    # 2 bytes
            self.end_pc = 0      # 2 bytes
            self.handler_pc = 0  # 2 bytes
            self.catch_type = 0  # 2 bytes

        def populate(self, f):
            self.start_pc = int.from_bytes(f.read(2), byteorder="big")
            self.end_pc = int.from_bytes(f.read(2), byteorder="big")
            self.handler_pc = int.from_bytes(f.read(2), byteorder="big")
            self.catch_type = int.from_bytes(f.read(2), byteorder="big")
            return 8

        def get_bytes(self):
            ret = b''
            ret += struct.pack(">h", self.start_pc)
            ret += struct.pack(">h", self.end_pc)
            ret += struct.pack(">h", self.handler_pc)
            ret += struct.pack(">h", self.catch_type)

            return ret


    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        self.max_stack = 0    # 2 bytes
        self.max_locals = 0   # 2 bytes
        self.code_length = 0  # 4 bytes
        self.code = []        # variable list of bytes
        self.exception_table_length = 0  # 2 bytes
        self.exception_table = []  # variable
        self.attributes_count = 0  # 2 bytes
        self.attributes = attributeinfo.AttributeInfo(constant_pool)

    def populate(self, f):
        self.max_stack = int.from_bytes(f.read(2), byteorder="big")
        self.max_locals = int.from_bytes(f.read(2), byteorder="big")
        self.code_length = int.from_bytes(f.read(4), byteorder="big")
        self.code = f.read(self.code_length)
        self.exception_table_length = int.from_bytes(f.read(2), byteorder="big")

        for i in range(self.exception_table_length):
            ex = self.ExceptionTable()
            ex.populate(f)
            self.exception_table.append(ex)

        self.attributes_count = int.from_bytes(f.read(2), byteorder="big")
        self.attributes.set_count(self.attributes_count)
        self.attributes.build(f)

        return 2+2+4+self.code_length+2+8*self.exception_table_length+2+self.attributes.get_size_in_bytes()

    def get_bytes(self):
        ret = super().get_bytes()
        ret += struct.pack(">h", self.max_stack)
        ret += struct.pack(">h", self.max_locals)
        ret += struct.pack(">i", self.code_length)
        ret += self.code

        ret += struct.pack(">h", self.exception_table_length)

        for t in self.exception_table:
            ret += t.get_bytes()

        ret += struct.pack(">h", self.attributes_count)
        ret += self.attributes.get_bytes()

        return ret

