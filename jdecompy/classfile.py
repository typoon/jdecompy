import sys
import struct
import compiler.grammar as grammar
from constants import *
from constantpool import ConstantPool
from fieldinfo import FieldInfo
from methodinfo import MethodInfo
from attributeinfo import AttributeInfo
from cp.utf8info import Utf8Info

class ClassFile:

    def __init__(self, file_path):

        self.magic = 0                       # 4 bytes
        self.minor_version = 0               # 2 bytes
        self.major_version = 0               # 2 bytes
        self.constant_pool_count = 0         # 2 bytes
        self.constant_pool = ConstantPool()  # variable
        self.access_flags = 0                # 2 bytes
        self.this_class = 0                  # 2 bytes
        self.super_class = 0                 # 2 bytes
        self.interfaces_count = 0            # 2 bytes
        self.interfaces = []                 # variable
        self.fields_count = 0                # 2 bytes
        self.fields = []                     # variable - Array of FieldInfo
        self.methods_count = 0               # 2 bytes
        self.methods = []                    # variable
        self.attributes_count = 0            # 2 bytes
        self.attributes = None               # variable

        self._file = None
        self._file_path = file_path

        # Used to report errors to the compiler
        self._error = ""

    def load(self):
        """
        This method will open the file pointed by file_path and populate the
        ClassFile object with the appropriate values
        """
        try:
            self._file = open(self._file_path, mode="rb")
        except IOError:
            print("Error opening file ", self._file_path)
            print("Exception: ", sys.exc_info())
            print("Aborting...")
            sys.exit(-1)

        self._read_magic()
        self._read_minor_version()
        self._read_major_version()
        self._read_constant_pool_count()
        self._read_constant_pool()
        self._read_access_flags()
        self._read_this_class()
        self._read_super_class()
        self._read_interfaces_count()
        self._read_interfaces()
        self._read_fields_count()
        self._read_fields()
        self._read_methods_count()
        self._read_methods()
        self._read_attributes_count()
        self._read_attributes()

    def _read_magic(self):
        self._file.seek(0)
        self.magic = self._file.read(4)

        if self.magic != b'\xca\xfe\xba\xbe':
            print("Error, magic signature does not match 0xCAFEBABE")

    def _read_minor_version(self):
        self._file.seek(4)
        self.minor_version = self._file.read(2)

    def _read_major_version(self):
        self._file.seek(6)
        self.major_version = self._file.read(2)

    def _read_constant_pool_count(self):
        self._file.seek(8)
        self.constant_pool_count = int.from_bytes(self._file.read(2), byteorder='big')
        self.constant_pool.set_count(self.constant_pool_count)

    def _read_constant_pool(self):
        self.constant_pool._build(self._file)

    def _read_access_flags(self):
        self._file.seek(self.constant_pool.get_size_in_bytes() + 10)
        self.access_flags = int.from_bytes(self._file.read(2), byteorder='big')

    def _read_this_class(self):
        """
        The value read here is an index into the constant pool pointing
        to a ClassInfo structure
        """
        self._file.seek(self.constant_pool.get_size_in_bytes() + 12)
        self.this_class = int.from_bytes(self._file.read(2), byteorder='big')

    def _read_super_class(self):
        """
        The value read here is an index into the constant pool pointing
        to a ClassInfo structure
        """
        self._file.seek(self.constant_pool.get_size_in_bytes() + 14)
        self.super_class = int.from_bytes(self._file.read(2), byteorder='big')

    def _read_interfaces_count(self):
        self._file.seek(self.constant_pool.get_size_in_bytes() + 16)
        self.interfaces_count = int.from_bytes(self._file.read(2), byteorder='big')

    def _read_interfaces(self):
        """
        Each value read here is an index pointing into the constant pool
        to a ClassInfo structre
        """
        self._file.seek(self.constant_pool.get_size_in_bytes() + 18)
        for i in range(self.interfaces_count):
            self.interfaces.append(int.from_bytes(self._file.read(2), byteorder='big'))

    def _read_fields_count(self):
        #pos = self.constant_pool.get_size_in_bytes + 18 + (self.interfaces_count * 2)
        #self._file.seek(pos)
        self.fields_count = int.from_bytes(self._file.read(2), byteorder='big')

    def _read_fields(self):
        for i in range(self.fields_count):
            fi = FieldInfo(self.constant_pool)
            fi._build(self._file)
            self.fields.append(fi)

    def _read_methods_count(self):
        self.methods_count = int.from_bytes(self._file.read(2), byteorder='big')

    def _read_methods(self):
        for i in range(self.methods_count):
            mi = MethodInfo(self.constant_pool)
            mi._build(self._file)
            self.methods.append(mi)

    def _read_attributes_count(self):
        self.attributes_count = int.from_bytes(self._file.read(2), byteorder='big')

    def _read_attributes(self):
        self.attributes = AttributeInfo(self.constant_pool)
        self.attributes.set_count(self.attributes_count)
        self.attributes.build(self._file)
        print(self._file.tell())

    def set_error(self, message):
        self._error = message

    def get_error(self):
        return self._error

    def get_bytes(self):
        ret = b''

        ret += self.magic
        ret += self.minor_version
        ret += self.major_version
        ret += struct.pack(">h", self.constant_pool_count)
        ret += self.constant_pool.get_bytes()
        ret += struct.pack(">h", self.access_flags)
        ret += struct.pack(">h", self.this_class)
        ret += struct.pack(">h", self.super_class)
        ret += struct.pack(">h", self.interfaces_count)

        for i in self.interfaces:
            ret += struct.pack(">h", i)

        ret += struct.pack(">h", self.fields_count)

        for f in self.fields:
            ret += f.get_bytes()

        ret += struct.pack(">h", self.methods_count)

        for m in self.methods:
            ret += m.get_bytes()

        ret += struct.pack(">h", self.attributes_count)
        ret += self.attributes.get_bytes()

        return ret

    def compile_from_file(self, path):
        try:
            f = open(path, mode="r")
        except IOError:
            print("Cannot open file %s" % path)
            print("Exception: ", sys.exc_info())
            print("Aborting...")
            sys.exit(-1)

        code = f.read()
        self.compile_from_string(code)

    def compile_from_string(self, code):
        grammar.compile(self, code)

    def get_name(self):
        return str(self.constant_pool.entries[self.this_class].get_name())

    def rename_class(self, name):
        name_index = self.constant_pool.entries[self.this_class].name_index
        self.constant_pool.entries[name_index].length = len(name)
        self.constant_pool.entries[name_index].bytes = name.encode('utf-8')

    # TODO: This method should get a FieldInfo parameter instead of what it
    #       does now
    def add_class_field(self, field):
        """ Add a new field to the class and returns it to the caller """
        self.fields.append(field)
        self.fields_count += 1
        self.constant_pool_count = self.constant_pool._count

    def add_method(self, access_flags, name, signature, code):
        


        pass

    def save(self, path, classname):
        self.rename_class(classname)

        # TODO: This is a hack, as the methods inside the constant_pool
        #       do not have access to the classfile.constant_pool_count
        #       I need to update the count here to reflect the correct 
        #       value. There is probably a better way to do this, but I
        #       am not sure what it is right now. Need to think

        self.constant_pool_count = self.constant_pool._count

        buf = self.get_bytes()
        path = '/%s/%s.class' % (path, classname)

        try:
            f = open(path, mode="wb")
            f.write(buf)
            f.close()
        except IOError:
            print("Could not save file %s" % path)
 
