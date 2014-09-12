import struct
from attributeinfo import AttributeInfo
from cp.constantpoolutils import ConstantPoolUtils


class FieldInfo:
    """
    access_flags
    name_index
    descriptor_index
    attributes_count
    attributes - list of AttributeInfo structures
    """
    access_flags = 0      # 2 bytes
    name_index = 0        # 2 bytes - Index pointing to Utf8Info
    descriptor_index = 0  # 2 bytes - Index pointing to Utf8Info
    attributes_count = 0  # 2 bytes
    attributes = None       # variable

    def __init__(self, constant_pool):
        self.access_flags = 0
        self.name_index = 0
        self.descriptor_index = 0
        self.attributes_count = 0
        self._constant_pool = constant_pool
        self.attributes = AttributeInfo(constant_pool)

    def __str__(self):
        ret = 'FieldInfo: '
        ret += self.get_field_type() + ' '
        ret += self._constant_pool.entries[self.name_index].get_bytes_as_str() + ' '
        ret += 'Access flags: %d' % self.access_flags
        return ret

    def _build(self, f):
        self.access_flags = int.from_bytes(f.read(2), byteorder="big")
        self.name_index = int.from_bytes(f.read(2), byteorder="big")
        self.descriptor_index = int.from_bytes(f.read(2), byteorder="big")
        self.attributes_count = int.from_bytes(f.read(2), byteorder="big")

        self.attributes.set_count(self.attributes_count)
        #print("Access flags: %d" % self.access_flags)
        #print("Name index %d" % self.name_index)
        #print("Descriptor index %d" % self.descriptor_index)
        #print("Attributes count: ", self.attributes_count)
        #print(self)
        self.attributes.build(f)

    def get_field_type(self):
        info = self._constant_pool.entries[self.descriptor_index].get_bytes_as_str()
        #return info
        return ConstantPoolUtils.parse_field_type(info)

    def get_bytes(self):
        ret = b''

        ret += struct.pack(">h", self.access_flags)
        ret += struct.pack(">h", self.name_index)
        ret += struct.pack(">h", self.descriptor_index)
        ret += struct.pack(">h", self.attributes_count)
        ret += self.attributes.get_bytes()

        return ret
