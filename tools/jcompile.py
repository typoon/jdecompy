#!/usr/bin/python3

import sys
import getopt
import os

sys.path.append('../')

from jdecompy.classfile import ClassFile

#--------------------------------------------------------------------
# Global variables go here
#--------------------------------------------------------------------
global input_file
global output_file
global code_file

#--------------------------------------------------------------------
# Function definitions
#--------------------------------------------------------------------

def usage(argv):
    print("Usage: python3 %s -i File.class -a File.jasm -o NewFile.class" % (argv[0]))

def help(argv):
    usage(argv)
    print("Options are:")
    print("  -h | --help    Prints this help message")
    print("  -i             Input class file to be modified")
    print("  -a             Input file with the assembly code to be used to ")
    print("                 modify the input class file")
    print("  -o             Output file")

#--------------------------------------------------------------------
# Main code
#--------------------------------------------------------------------

if __name__ != '__main__':
    print("This file cannot be loaded as a module")
    sys.exit(-1)

input_file = None
output_file = None
code_file = None

opt_str = "hi::a::o::"
long_opts = ["help"]
opts, args = getopt.getopt(sys.argv[1:], opt_str, long_opts)


for opt, arg in opts:
    if opt in ("-h", "--help"):
        help(sys.argv)
        sys.exit(1)


for opt, arg in opts:
    if opt == "-i":
        input_file = arg

    if opt == "-o":
        output_file = arg

    if opt == "-a":
        code_file = arg

if not input_file:
    print("You need to specify an input class file (-i)")
    sys.exit(-1)

if not output_file:
    print("You need to specify an output class file (-o)")
    sys.exit(-1)

if not code_file:
    print("You need to specify an assembly code file (-a)")
    sys.exit(-1)

cf = ClassFile(input_file)
r = cf.load()

if not r:
    print(cf.get_error())
    print("Aborting...")
    sys.exit(-1)

dest_class = os.path.basename(output_file).replace(".class","")
dest_dir = os.path.dirname(output_file)

cf.compile_from_file(code_file)
cf.save(dest_dir, dest_class)

print("Compilation completed succesfully!")
