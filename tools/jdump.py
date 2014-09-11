import sys
import getopt

sys.path.append('../')

from jdecompy.classfile import ClassFile

#--------------------------------------------------------------------
# Global variables go here
#--------------------------------------------------------------------
global _method_index
global _cp_index
global _code_index


if __name__ != '__main__':
    print("This file cannot be loaded as a module")
    sys.exit(-1)

def usage(argv):
    print("Usage: python3 %s [-h|--help] [-f|--full] [-m] [-p[index]] [-c[index]] File.class" % (argv[0]))

def help(argv):
    usage(argv)
    print("Options are:")
    print("  -h | --help    Prints this help message")
    print("  -f | --full    Prints all information of the class file")
    print("  -m             Lists all methods in the class file together with")
    print("                 an index that can be used with the -c option")
    print("  -p index       Prints the content of the constant pool on index.")
    print("                 If no index is provided, then the whole constant")    
    print("                 pool is printed")    
    print("  -c index       Prints the code of the method specified by index.")
    print("                 index is obtained from running this program with")
    print("                 the -m option")


_method_index = 0
_cp_index = 0
_code_index = 0

opt_str = "hfmp::c::"
long_opts = ["help", "full"]
opts, args = getopt.getopt(sys.argv[1:], opt_str, long_opts)


for opt, arg in opts:
    if opt in ("-h", "--help"):
        help(sys.argv)
        sys.exit(1)

    if opt in ("-f", "--full"):
        pass

    if opt == "-m":
        _method_index = arg


if len(args) != 1:
    usage(sys.argv)
    sys.exit(1)

c = ClassFile(args[0])
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

