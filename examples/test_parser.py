import sys
sys.path.append('../')

from jdecompy.classfile import ClassFile
import jdecompy.grammar as parser


if __name__ == '__main__':
    c = ClassFile('./class/Ex1.class')
    c.load()

    c.compile_from_string('''.method public void main (arg) 
                                 .var int x
                                 nop
                                 aconst_null
                                 iconst_m1
                             .method_end''')

