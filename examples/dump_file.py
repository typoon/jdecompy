import sys
sys.path.append('../')

from jdecompy.classfile import ClassFile

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Use: python3 main.py File.class")
        sys.exit(1)

    c = ClassFile(sys.argv[1])
    c.load()

    print("Magic: ", c.magic)
    print("Minor: ", c.minor_version)
    print("Major: ", c.major_version)
    print("Constant pool count: ", c.constant_pool_count)

    for i in range(1, c.constant_pool_count):
        print("\t[%d] %s" % (i, c.constant_pool.entries[i]))

    print("Constant pool size in bytes: %d" % c.constant_pool.get_size_in_bytes())
    print("Access flags: %d" % c.access_flags)
    print("This class: %s" % c.constant_pool.entries[c.this_class].get_name())
    print("Super class: %s" % c.constant_pool.entries[c.super_class].get_name())
    print("Interfaces count: %s" % c.interfaces_count)
    print("Interfaces ",  c.interfaces)
    print("Fields count: %s" % c.fields_count)

    for i in range(c.fields_count):
        print("\t", c.fields[i])

    print("Methods count: %d" % c.methods_count)

    for i in range(c.methods_count):
        print("\t", c.methods[i].get_method_signature())
        print(c.methods[i].get_code_asm())

    print("Attributes count: %d" % c.attributes_count)

