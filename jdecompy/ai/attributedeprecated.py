import struct
from ai.attributeinfoentry import AttributeInfoEntry

class AttributeDeprecated(AttributeInfoEntry):
    """
    Nothing to do here
    """
    def __init__(self, constant_pool):
        super().__init__(constant_pool)

    def populate(self, f):
        return 0
    
    def get_bytes(self):
        ret = super().get_bytes()
        return ret
