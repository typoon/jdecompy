from cp.constantpoolfactory import ConstantPoolFactory
from cp.utf8info import Utf8Info
from cp.nameandtypeinfo import NameAndTypeInfo
from cp.methodrefinfo import MethodRefInfo
from constants import *


class ConstantPool:

    def __init__(self):
        self.entries = [None]
        self._count = 0
        self._file = None
        self._size_in_bytes = 0

    def _build(self, f):
        """
        Builds the constant pool representation in this object

        Keyword arguments:
        f -- is the handler to the .class file opened on ClassFile.py
        """

        self._file = f
        self._file.seek(10)  # Point to the beginning of the constant pool

        i = 1
        while i != self._count:
            tag = int.from_bytes(self._file.read(1), byteorder='big')
            self._size_in_bytes += 1

            obj = ConstantPoolFactory.create(tag)

            obj._constant_pool = self
            self._size_in_bytes += obj.populate(self._file)

            self.entries.append(obj)

            if tag == CONSTANT_LONG or tag == CONSTANT_DOUBLE:
                self.entries.append(obj)
                i += 1

            i += 1

    def set_count(self, count):
        self._count = count

    def get_size_in_bytes(self):
        return self._size_in_bytes

    def get_bytes(self):
        ret = b''

        #print(len(self.entries))

        for e in self.entries[1:]:
            ret += e.get_bytes()

        return ret

    def add_methodrefinfo(self, class_index, name_and_type_index):
        mri = MethodRefInfo()

        mri.class_index = class_index
        mri.name_and_type_index = name_and_type_index

        self._count += 1
        self.entries.append(mri)

        return self._count - 1

    def add_nameandtypeinfo(self, name, type):
        name_and_type_info = NameAndTypeInfo()

        name_index = self.add_utf8info(name, len(name))
        descriptor_index = self.add_utf8info(type, len(type))

        name_and_type_info.name_index = name_index
        name_and_type_info.descriptor_index = descriptor_index
        name_and_type_info._constant_pool = self

        self._count += 1
        self.entries.append(name_and_type_info)

        return self._count-1

    def add_utf8info(self, string, length):
        ''' Adds a new Utf8Info entry in the constant pool
        in case one with the same value does not already exist'''

        index = self.get_utf8info_index(string, length)
        if index > 0:
            return index

        utf8 = Utf8Info()
        utf8.length = length
        utf8.bytes = bytes(string, 'utf-8')

        self._count += 1
        self.entries.append(utf8)

        return self._count-1

    def get_utf8info_index(self, string, length):
        ''' Checks if an UTF8Info with the passed string already exists in the
        constant pool. Returns -1 if not, or the index if it does exist'''
        utf8 = Utf8Info()
        utf8.length = length
        utf8.bytes = bytes(string, 'utf-8')

        index = 1
        for i in self.entries[1:]:
            if i.tag == CONSTANT_UTF8:
                if i.bytes == utf8.bytes:
                    return index

            index += 1

        return -1
