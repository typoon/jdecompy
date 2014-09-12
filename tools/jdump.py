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


#--------------------------------------------------------------------
# Function definitions
#--------------------------------------------------------------------

def usage(argv):
    print("Usage: python3 %s [-h|--help] [-f|--full] [-m] [-p[index]] [-c[index]] File.class" % (argv[0]))

def help(argv):
    usage(argv)
    print("Options are:")
    print("  -h | --help    Prints this help message")
    print("  -f | --full    Prints all information of the class file")
    print("                 that would be printed with -c -i -m -p")
    print("  -i | --info    Prints information about the class file")
    print("  -m             Lists all methods in the class file together with")
    print("                 an index that can be used with the -c option")
    print("  -p index       Prints the content of the constant pool on index.")
    print("                 If no index is provided, then the whole constant")    
    print("                 pool is printed")    
    print("  -c index       Prints the code of the method specified by index.")
    print("                 index is obtained from running this program with")
    print("                 the -m option. You can pass more than one index")
    print("                 by separating them using a comma, i.e: -c 1,2,10")

def print_info(cf):
    print("Magic word: ", cf.magic)
    print("Minor version: ", cf.minor_version)
    print("Major version: ", cf.major_version)
    print("Constant pool count: ", cf.constant_pool_count)
    print("Constant pool size in bytes: %d" % cf.constant_pool.get_size_in_bytes())
    print("Access flags: %d" % cf.access_flags)
    print("This class: %s" % cf.constant_pool.entries[cf.this_class].get_name())
    print("Super class: %s" % cf.constant_pool.entries[cf.super_class].get_name())
    print("Interfaces count: %s" % cf.interfaces_count)
    print("Fields count: %s" % cf.fields_count)
    print("Attributes count: %d" % cf.attributes_count)

def print_presentation_line(s):
    repeat = 39 - int(len(s)/2)
    print("=" * repeat, end=" ")
    print(s, end=" ")
    print("=" * repeat)

def print_method_list(cf):
    for i in range(cf.methods_count):
        print("[%d] - %s" % (i, cf.methods[i].get_method_signature()))

def print_method_code(cf, idx):
    print("%s" % (cf.methods[i].get_method_signature()))
    print(cf.methods[idx].get_code_asm())

def print_cp(cf, idx):
    print("[%d] %s" % (idx, cf.constant_pool.entries[idx]))
    pass

#--------------------------------------------------------------------
# Main code
#--------------------------------------------------------------------

if __name__ != '__main__':
    print("This file cannot be loaded as a module")
    sys.exit(-1)

_method_index = 0
_cp_index = 0
_code_index = 0

opt_str = "ihfmp::c::"
long_opts = ["info", "help", "full"]
opts, args = getopt.getopt(sys.argv[1:], opt_str, long_opts)


for opt, arg in opts:
    if opt in ("-h", "--help"):
        help(sys.argv)
        sys.exit(1)

if len(args) != 1:
    usage(sys.argv)
    sys.exit(1)

cf = ClassFile(args[0])
r = cf.load()

if not r:
    print(cf.get_error())
    print("Aborting...")
    sys.exit(-1)

for opt, arg in opts:
    if opt in ("-i", "--info"):
        print_presentation_line("INFO")
        print_info(cf)
        print_presentation_line("END INFO")

    if opt in ("-f", "--full"):
        pass

    if opt == "-m":
        print_presentation_line("METHODS LIST")
        print_method_list(cf)
        print_presentation_line("END METHODS LIST")

    if opt == "-p":
        arg = arg.split(",")
        print_presentation_line("CONSTANT POOL")

        if arg == ['--']:
            for i in range(1, cf.constant_pool_count):
                print_cp(cf, i)
        else:
            for i in arg:
                i = int(i)
                print_cp(cf, i)

        print_presentation_line("END CONSTANT POOL")


    if opt == "-c":
        arg = arg.split(",")
        for i in arg:
            print_presentation_line("METHOD")
            i = int(i)
            print_method_code(cf, i)
            print_presentation_line("END METHOD")

    print("")



#for i in range(1, c.constant_pool_count):
#    print("\t[%d] %s" % (i, c.constant_pool.entries[i]))
#
#for i in range(c.fields_count):
#    print("\t", c.fields[i])
#
#print("Methods count: %d" % c.methods_count)
#

#
