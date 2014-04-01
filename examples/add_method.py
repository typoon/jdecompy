import sys
sys.path.append('../')

from jdecompy.classfile import ClassFile

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Use: python3 main.py File.class")
        sys.exit(1)

    c = ClassFile(sys.argv[1])
    c.load()

    c.compile_from_string('''.method public void myMethod()
                             .method_end''')
    c.save('/tmp/', 'Ex2')

