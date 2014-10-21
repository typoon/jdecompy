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
                              nop
                              iload_1
                              iload_2
                              isub
                              istore_3
                              getstatic 4
                              new 5
                              dup
                              invokespecial 6
                              ldc 7
                              invokevirtual 8
                              iload_3
                              invokevirtual 9
                              invokevirtual 10
                              invokevirtual 11
                              iload_3
                              ireturn
                             .method_end''')

    c.compile_from_string('''.method public void myMethod(II)
                              nop
                              iload_1
                              ireturn
                             .method_end''')

    c.save('/tmp/', 'Ex2')

