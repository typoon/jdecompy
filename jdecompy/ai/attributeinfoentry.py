import struct

class AttributeInfoEntry:

    def __init__(self, constant_pool):
        self.name_index = 0  # 2 bytes
        self.length = 0      # 4 bytes
        self._constant_pool = constant_pool

    def populate(self, f):
        """This method should populate the subclass and return the number
        of bytes that were read from the file during the process
        """
        return 0
    
    def get_name(self):
        name = self._constant_pool.entries[self.name_index].get_bytes_as_str()
        return name
        
    
    def get_bytes(self):
        """ This method needs to be implemented in every subclass, and return
        the class representation in bytes
        """
        ret = b''
        ret += struct.pack(">h", self.name_index)
        ret += struct.pack(">i", self.length)
        return ret
