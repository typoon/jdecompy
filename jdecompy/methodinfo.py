import struct
import sys
from attributeinfo import AttributeInfo
from cp.constantpoolutils import ConstantPoolUtils
from opcodes import OPC
from constants import *

class MethodInfo:
    """
    access_flags
    name_index - Points to an Utf8Info containing the unqualified method 
                 name
    descriptor_index - Points to an Utf8Info representing a valid method 
                       descriptor
    attributes_count - Number of items in the attributes list
    attributes - list of AttributeInfo structures
    """
    access_flags = 0      # 2 bytes
    name_index = 0        # 2 bytes
    descriptor_index = 0  # 2 bytes
    attributes_count = 0  # 2 bytes
    attributes = None       # variable

    def __init__(self, constant_pool):
        self.access_flags = 0
        self.name_index = 0
        self.descriptor_index = 0
        self.attributes_count = 0
        self._constant_pool = constant_pool
        self.attributes = AttributeInfo(constant_pool)

    def get_method_signature(self):
        info = ConstantPoolUtils.parse_method_type(self._constant_pool.entries[self.descriptor_index].get_bytes_as_str())
        name = self._constant_pool.entries[self.name_index].get_bytes_as_str()
        ret = info['ret_type'] + ' ' + name + '(' + ','.join(info['params']) + ')'
        return ret

    def get_code_attr(self):
        c = None
        for i in range(self.attributes_count):
            if self.attributes.get_attr_name(i) == ATTR_CODE:
                c = self.attributes.entries[i]

        return c

    def get_code_bytes(self):
        """
        Returns a byte list with all the bytes that represent the code of the
        current method
        """
        c = []
        code_attr = self.get_code_attr()
        if code_attr:
            c = code_attr.code
            print("Code len: %d" % code_attr.code_length)

        return c

    def get_code_asm(self):
        code = self.get_code_bytes()
        abort = False

        if not code:
            return ''

        e = enumerate(code)
        asm = '\t'

        count = 0
        for _, b in e:
            # Somehow b is automagically converted to int :|
            # TODO: Understand the above mentioned magic AND refactor this 

            opc_index = b
            opc = OPC[opc_index]

            asm += opc['name']
            #print("opc %s" % opc['name'])
            #print("opc %s args %d" % (opc['name'], opc['num_args']))
            #print("count = %d" % count)

            if opc['name'] == "lookupswitch":

                # Read the padding bytes here
                pad = 4 - ((count+1) % 4)

                if pad == 4:
                    pad = 0

                print("Pad: %d - Count %d" % (pad,count))
                for i in range(pad):
                    _, b = next(e)
                    print(' ' + str(hex(b)))
                    asm += ' ' + str(hex(b))

                # Read the default bytes here
                for i in range(4):
                    _, b = next(e)
                    print(' ' + str(hex(b)))
                    asm += ' ' + str(hex(b))

                # Read the npairs bytes
                total_pairs = 0

                _, b = next(e)
                asm += ' ' + str(hex(b))
                total_pairs = b << 24 

                _, b = next(e)
                asm += ' ' + str(hex(b))
                total_pairs |= b << 16 

                _, b = next(e)
                asm += ' ' + str(hex(b))
                total_pairs |= b << 8 

                _, b = next(e)
                asm += ' ' + str(hex(b))
                total_pairs |= b  

                print("Total pairs %d" % total_pairs)

                # Each npair consists of a 32 bit int match + 32 bit int offset
                # hence the total_pairs*8
                for i in range(total_pairs*8):
                    _, b = next(e)
                    asm += ' ' + str(hex(b))

                count += 1 + pad + 4 + 4 + total_pairs*8

            elif opc['name'] == "tableswitch":
                # Read the padding bytes here
                pad = 4 - ((count+1) % 4)

                if pad == 4:
                    pad = 0

                print("Pad: %d - Count %d" % (pad,count))
                for i in range(pad):
                    _, b = next(e)
                    print(' ' + str(hex(b)))
                    asm += ' ' + str(hex(b))

                # Read the default bytes here
                for i in range(4):
                    _, b = next(e)
                    print(' ' + str(hex(b)))
                    asm += ' ' + str(hex(b))

                # Read the low bytes
                low = 0

                _, b = next(e)
                asm += ' ' + str(hex(b))
                low = b << 24 

                _, b = next(e)
                asm += ' ' + str(hex(b))
                low = b << 16

                _, b = next(e)
                asm += ' ' + str(hex(b))
                low = b << 8

                _, b = next(e)
                asm += ' ' + str(hex(b))
                low = b  

                # Read the high bytes
                high = 0

                _, b = next(e)
                asm += ' ' + str(hex(b))
                high = b << 24 

                _, b = next(e)
                asm += ' ' + str(hex(b))
                high = b << 16

                _, b = next(e)
                asm += ' ' + str(hex(b))
                high = b << 8

                _, b = next(e)
                asm += ' ' + str(hex(b))
                high = b  

                # Read the offsets
                for i in range(high - low + 1):
                    _, b = next(e)
                    asm += ' ' + str(hex(b))
                    _, b = next(e)
                    asm += ' ' + str(hex(b))
                    _, b = next(e)
                    asm += ' ' + str(hex(b))
                    _, b = next(e)
                    asm += ' ' + str(hex(b))

                # count + opcode + pad + default + high + low + (4 bytes of each jump offset)
                count = count + 1 + pad + 4 + 4 + 4 + ((high - low + 1) * 4)

            elif opc['name'] == "wide":

                _, b = next(e)

                name = OPC[b]['name']

                if name in ('iload', 'fload', 'aload', 'lload', 'dload', 'istore', 'fstore', 'astore', 'lstore', 'dstore', 'ret'):
                    # Index byte
                    _, b = next(e)
                    asm += ' ' + str(hex(b))
                    _, b = next(e)
                    asm += ' ' + str(hex(b))

                    # count + wide + opcode + 2*indexbyte
                    count = count + 1 + 1 + 1 + 1

                elif name == 'iinc':
                    # Index byte
                    _, b = next(e)
                    asm += ' ' + str(hex(b))
                    _, b = next(e)
                    asm += ' ' + str(hex(b))

                    # Const byte
                    _, b = next(e)
                    asm += ' ' + str(hex(b))
                    _, b = next(e)
                    asm += ' ' + str(hex(b))

                    count = count + 1 + 1 + 4

                else:
                    asm += 'wide opcode could not be parsed correctly.'
                    asm += 'From this point, this disasm cannot be trusted'

                    count = count + 2


                abort = True

            else:
                count = count + 1 + opc['num_args']
                for i in range(opc['num_args']):
                    _, b = next(e)
                    asm += ' ' + str(hex(b))

            asm += "\n\t"

        if abort:
            print(asm)
            sys.exit(2)
        return asm
    
    def get_bytes(self):
        ret = b''
        
        ret += struct.pack(">h", self.access_flags)
        ret += struct.pack(">h", self.name_index)
        ret += struct.pack(">h", self.descriptor_index)
        ret += struct.pack(">h", self.attributes_count)
        ret += self.attributes.get_bytes()
        
        return ret
        
    def __str__(self):
        ret = 'FieldInfo: '
        ret += self.get_field_type() + ' '
        ret += self._constant_pool.entries[self.name_index].get_bytes_as_str()
        return ret

    def _build(self, f):
        self.access_flags = int.from_bytes(f.read(2), byteorder="big")
        self.name_index = int.from_bytes(f.read(2), byteorder="big")
        self.descriptor_index = int.from_bytes(f.read(2), byteorder="big")
        self.attributes_count = int.from_bytes(f.read(2), byteorder="big")

        self.attributes.set_count(self.attributes_count)
        self.attributes.build(f)
