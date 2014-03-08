from ai.attributeinfoentry import AttributeInfoEntry

class AttributeSynthetic(AttributeInfoEntry):
    """
    Does nothing and has no members
    """
    def __init__(self, constant_pool):
        super().__init__(constant_pool)

    def populate(self, f):
        return 0

    def get_bytes(self):
        ret = ret = super().get_bytes()
        return ret
