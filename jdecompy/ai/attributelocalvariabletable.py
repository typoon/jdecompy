import struct
from ai.attributeinfoentry import AttributeInfoEntry

# TODO: Implement me

class AttributeLocalVariableTable(AttributeInfoEntry):
    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        data = b''

    def populate(self, f):
        self.data = f.read(self.length)
        return self.length
        
    def get_bytes(self):
        ret = super().get_bytes()
        ret += self.data
        
        return ret
