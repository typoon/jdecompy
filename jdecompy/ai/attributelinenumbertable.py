import struct
from ai.attributeinfoentry import AttributeInfoEntry

class AttributeLineNumberTable(AttributeInfoEntry):

    class LineNumberTable:
        """
        start_pc - an index into the code array pointing to where a line of code starts
        line_number - the number of the line in the source code file
        """
        def __init__(self):
            self.start_pc = 0
            self.line_number = 0

        def populate(self, f):
            self.start_pc = int.from_bytes(f.read(2), byteorder="big")
            self.line_number = int.from_bytes(f.read(2), byteorder="big")
            return 4
            
        def get_bytes(self):
            ret = b''
            
            ret += struct.pack(">h", self.start_pc)
            ret += struct.pack(">h", self.line_number)
            
            return ret
            

    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        self.line_number_table_length = 0  # 2 bytes
        self.line_number_table = []        # variable

    def populate(self, f):
        ret = 2
        self.line_number_table_length = int.from_bytes(f.read(2), byteorder="big")
        for i in range(self.line_number_table_length):
            lnt = self.LineNumberTable()
            ret += lnt.populate(f)
            self.line_number_table.append(lnt)

        return ret

    def get_bytes(self):
        ret = super().get_bytes()
        ret += struct.pack(">h", self.line_number_table_length)
        
        for l in self.line_number_table:
            ret += l.get_bytes()
            
        return ret
