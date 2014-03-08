import struct

class ConstantPoolEntry:

    def __init__(self, tag = None):
        self._constant_pool = None  # Reference to the constant pool
                                    # so I can lookup my references
        self.tag = '' # 1 byte

        if tag is not None:
            self.tag = tag

    def populate(self, f):
        return 0
    
    def get_bytes(self):
        ret = b''
        ret += struct.pack(">b", self.tag)
        
        return ret
        
