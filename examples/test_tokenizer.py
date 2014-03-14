import sys
sys.path.append('../')

from jdecompy.classfile import ClassFile
import jdecompy.tokens as t

if __name__ == '__main__':
    # c.compile_from_string('.var static public int meuint')
    #t.test('''.var static public int meuint
    t.test('''.method public void main (arg) 
                  .var int x
                  nop
                  aconst_null
                  iconst_m1
                  nop
              .method_end''')
    # c.save('/tmp/', 'Ex2')

