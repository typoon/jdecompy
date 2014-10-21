import struct
from ai.attributeinfofactory import AttributeInfoFactory


class AttributeInfo:
    
    def __init__(self, constant_pool):
        self.entries = []
        self._count = 0
        self._file = None
        self._size_in_bytes = 0
        self._constant_pool = constant_pool

    def add_entry(self, entry):
        self.entries.append(entry)
        self._count += 1

    def set_count(self, count):
        self._count = count

    def get_size_in_bytes(self):
        return self._size_in_bytes

    def get_attr_name(self, idx):
        name_index = self.entries[idx].name_index
        name = self._constant_pool.entries[name_index].get_bytes_as_str()
        return name

    def build(self, f):
        self._file = f

        for i in range(self._count):
            name_index = int.from_bytes(self._file.read(2), byteorder='big')
            length = int.from_bytes(self._file.read(4), byteorder='big')
            name = self._constant_pool.entries[name_index].get_bytes_as_str()

            attr = AttributeInfoFactory.create(name, self._constant_pool)
            attr.name_index = name_index
            attr.length = length

            self._size_in_bytes += attr.populate(f) + 6  # 6 is from name_index + length

            self.entries.append(attr)
    
    def get_bytes(self):
        ret = b''
        
        for e in self.entries:
            ret += e.get_bytes()
        
        return ret
