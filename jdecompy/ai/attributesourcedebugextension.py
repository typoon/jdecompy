from ai.attributeinfoentry import AttributeInfoEntry

class AttributeSourceDebugExtension(AttributeInfoEntry):
    """
    debug_extension - an Utf8 string containing extended debug information
    """
    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        self.debug_extension = b''

    def populate(self, f):
        self.debug_extension = f.read(self.length)
        return self.length

    def get_bytes(self):
        ret = ret = super().get_bytes()
        ret += self.debug_extension
        return ret
