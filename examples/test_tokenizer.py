import sys
sys.path.append('../')

from jdecompy.classfile import ClassFile
import jdecompy.tokens as t

if __name__ == '__main__':
    # c.compile_from_string('.var static public int meuint')
    #t.test('''.var static public int meuint
    t.test('''.method public static void main (args)
                   nop
               .method_end''')
    # c.save('/tmp/', 'Ex2')

