from ai.attributeinfoentry import AttributeInfoEntry

class AttributeInnerClasses(AttributeInfoEntry):
    """
    number_of_classes - number of items in the classes member
    classes - Array of InnerClass classes
    """

    number_of_classes = 0 # 2 bytes
    classes = []          # variable

    class InnerClass:
        """
        inner_class_info_index - Points to a ClassInfo structure into the constant pool
        outer_class_info_index - Either 0 or an index into the constant pool pointing to a ClassInfo structure
        inner_name_index - Either 0 or an index into the constant pool pointing to an Utf8Info structure
        inner_class_access_flags - access_flag value for this inner class
        """
        def __init__(self):
            self.inner_class_info_index = 0    # 2 bytes
            self.outer_class_info_index = 0    # 2 bytes
            self.inner_name_index = 0          # 2 bytes
            self.inner_class_access_flags = 0  # 2 bytes

        def populate(self, f):
            self.inner_class_info_index = int.from_bytes(f.read(2), byteorder="big")
            self.outer_class_info_index = int.from_bytes(f.read(2), byteorder="big")
            self.inner_name_index = int.from_bytes(f.read(2), byteorder="big")
            self.inner_class_access_flags = int.from_bytes(f.read(2), byteorder="big")
            return 8

    def __init__(self, constant_pool):
        super().__init__(constant_pool)
        self.number_of_classes = 0  # 2 bytes
        self.classes = []

    def populate(self, f):
        ret = 2
        self.number_of_classes = int.from_bytes(f.read(2), byteorder="big")
        for i in range(self.number_of_classes):
            ic = self.InnerClass()
            ret += ic.populate(f)
            self.classes.append(ic)

        return ret
