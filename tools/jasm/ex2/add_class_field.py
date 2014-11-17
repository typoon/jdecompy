import sys
from jdecompy.classfile import ClassFile

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Use: python3 main.py File.class")
        sys.exit(1)

    c = ClassFile(sys.argv[1])
    c.load()

    c.compile_from_string('.var static public int meuint')
    c.save('/tmp/', 'Ex2')
    print("File modified succesfully! Check /tmp/Ex2.class")

