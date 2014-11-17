import struct
import ply.yacc as yacc
import ply.lex as lex
import compiler.tokens as tok
from compiler.tokens import tokens
from opcodes import opc_compile
from methodinfo import MethodInfo
from fieldinfo import FieldInfo
from classfilehelper import ClassFileHelper
from attributeinfo import AttributeInfo
from ai.attributeinfofactory import AttributeInfoFactory
from constants import *
from cp.methodrefinfo import MethodRefInfo

# TODO: Should this be here? And should it be called MethodTree?
class MethodTree:
    def __init__(self):
        self.access_modifiers = []
        self.ret_type = ''
        self.name = ''
        self.params = ''
        self.variables = []
        self.code = b''


cf = None
g_method = MethodTree()

def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    if p is None:
        print("Unexpected end of file reached")
    else:
        print("Unexpected token %s on line %d position %d (%s)" % (p.type, p.lineno, p.lexpos, p.value))


# ----------------------------------------------------------------------------
# Start here
# ----------------------------------------------------------------------------
def p_start(p):
    '''start : fields methods
             | fields
             | methods
             | empty'''
    pass


# ----------------------------------------------------------------------------
# Method related parsing
# ----------------------------------------------------------------------------
def p_methods(p):
    '''methods : methods method_start method_body method_end
               | empty method_start method_body method_end'''

    pass
    
def p_method_start(p):
    '''method_start : METHOD_START access_modifiers RET_TYPE IDENTIFIER PARAMS'''
    print("Inside p_method_start %s" % p[4])
    #g_method.access_modifiers = p[2]
    g_method.ret_type = p[3]
    g_method.name = p[4]
    g_method.params = p[5]

    #print("access_modifiers = ", g_method.access_modifiers)
    #print("ret_type = ", g_method.ret_type)
    #print("name = ", g_method.name)
    #print("params = ", g_method.params)


def p_method_body(p):
    '''method_body : vars
                   | empty mnemonics
                   | vars mnemonics
                   | empty'''

    print("Inside p_method_body")

def p_method_end(p):
    '''method_end : METHOD_END'''

    global g_method
    found = False

    cp = cf.constant_pool
    mi = MethodInfo(cp)
    ai = AttributeInfo(cp)

    ret_type = ClassFileHelper.translate_type(g_method.ret_type)
    method_signature = g_method.params + ret_type

    #print("method_end")
    #print("method_signature = ", method_signature)

    method_name_index = cp.get_utf8info_index(g_method.name, len(g_method.name))
    method_signature_index = cp.get_utf8info_index(method_signature, 3)


    aie = AttributeInfoFactory.create(ATTR_CODE, cp)

    aie.max_stack = 10
    aie.max_locals = 10
    aie.code_length = len(g_method.code)
    aie.code = g_method.code
    
    aie.name_index = cp.add_utf8info(ATTR_CODE, len(ATTR_CODE))
    aie.length = 12 + aie.code_length # 12 + bytes in aie.code

    # Can I find this method in the class already?
    if method_name_index > 0 and method_signature_index > 0:
        attr = None
        for m in cf.methods:
            if m.name_index == method_name_index and m.descriptor_index == method_signature_index:
                attr = m.attributes

        if attr:
            attrcode_name_index = cp.add_utf8info(ATTR_CODE, len(ATTR_CODE))

            for a in attr.entries:
                if a.name_index == attrcode_name_index:
                    a.max_stack = aie.max_stack
                    a.max_locals = aie.max_locals
                    a.code_length = aie.code_length
                    a.code = aie.code

                    # Removing the attributes to avoid problems
                    # related to line counting (LineNumberTable attriute)
                    a.attributes_count = 0
                    a.attributes = None

                    a.length = 12 + a.code_length
                    found = True
        

    if not found:
        ai.add_entry(aie)

        name_and_type_index = cp.add_nameandtypeinfo(g_method.name, method_signature)
        cp.add_methodrefinfo(cf.this_class, name_and_type_index)

        mi.access_flags = ClassFileHelper.translate_access_flags(g_method.access_modifiers)
        mi.name_index = cp.add_utf8info(g_method.name, len(g_method.name))
        mi.descriptor_index = cp.add_utf8info(method_signature, len(method_signature))  # For now, only void ...() methods
        mi.attributes_count = 1  # 2 bytes
        mi.attributes = ai

        cf.add_method(mi)

    g_method = MethodTree()

def p_mnemonics(p):
    '''mnemonics : mnemonics opcode
                 | empty opcode'''
    pass

def p_opcode(p):
    '''opcode : nop
              | astore_0
              | astore_1
              | astore_2
              | astore_3
              | aload_0
              | aload_1
              | aload_2
              | aload_3
              | iload_0
              | iload_1
              | iload_2
              | iload_3
              | isub
              | istore_0
              | istore_1
              | istore_2
              | istore_3
              | getstatic
              | new
              | dup
              | invokespecial
              | invokevirtual
              | ldc
              | bipush
              | ireturn
              | return
              | iconst_m1
              | iconst_0
              | iconst_1
              | iconst_2
              | iconst_3
              | iconst_4
              | iconst_5'''
    #p[0] = p[1]
    #print("opcode: p[0] ", p[0])
    g_method.code += p[1]


# ----------------------------------------------------------------------------
# Method variables parsing
# ----------------------------------------------------------------------------
def p_vars(p):
    '''vars : vars var
            | empty var'''
    pass

def p_var(p):
    '''var : VAR RET_TYPE IDENTIFIER'''
    #print("VAR: %s %s %s"  % (p[1], p[2], p[3]))

    #if cf.add_class_field(p.modifiers, p[3], p[4]) is None:
    #    print(cf.get_error())
    #    raise SyntaxError


def p_var_array(p):
    '''var : VAR access_modifiers RET_TYPE array_types IDENTIFIER'''
    # TODO: Add arrays support
    #print("Arrays not supported yet")
    raise SyntaxError

def p_array_types(p):
    '''array_types : array_types ARRAY
                   | empty ARRAY'''
    pass

# ----------------------------------------------------------------------------
# Opcodes parsing
# ----------------------------------------------------------------------------
def p_nop(p):
    '''nop : NOP'''
    p[0] = opc_compile(p[1])

def p_astore_0(p):
    '''astore_0 : ASTORE_0'''
    p[0] = opc_compile(p[1])

def p_astore_1(p):
    '''astore_1 : ASTORE_1'''
    p[0] = opc_compile(p[1])

def p_astore_2(p):
    '''astore_2 : ASTORE_2'''
    p[0] = opc_compile(p[1])

def p_astore_3(p):
    '''astore_3 : ASTORE_3'''
    p[0] = opc_compile(p[1])

def p_aload_0(p):
    '''aload_0 : ALOAD_0'''
    p[0] = opc_compile(p[1])

def p_aload_1(p):
    '''aload_1 : ALOAD_1'''
    p[0] = opc_compile(p[1])

def p_aload_2(p):
    '''aload_2 : ALOAD_2'''
    p[0] = opc_compile(p[1])

def p_aload_3(p):
    '''aload_3 : ALOAD_3'''
    p[0] = opc_compile(p[1])

def p_iload_0(p):
    '''iload_0 : ILOAD_0'''
    p[0] = opc_compile(p[1])

def p_iload_1(p):
    '''iload_1 : ILOAD_1'''
    p[0] = opc_compile(p[1])

def p_iload_2(p):
    '''iload_2 : ILOAD_2'''
    p[0] = opc_compile(p[1])

def p_iload_3(p):
    '''iload_3 : ILOAD_3'''
    p[0] = opc_compile(p[1])

def p_isub(p):
    '''isub : ISUB'''
    p[0] = opc_compile(p[1])

def p_istore_0(p):
    '''istore_0 : ISTORE_0'''
    p[0] = opc_compile(p[1])

def p_istore_1(p):
    '''istore_1 : ISTORE_1'''
    p[0] = opc_compile(p[1])

def p_istore_2(p):
    '''istore_2 : ISTORE_2'''
    p[0] = opc_compile(p[1])

def p_istore_3(p):
    '''istore_3 : ISTORE_3'''
    p[0] = opc_compile(p[1])

def p_getstatic(p):
    '''getstatic : GETSTATIC SHORT
                 | GETSTATIC BYTE'''
    p[0] = opc_compile(p[1])
    p[0] += struct.pack('>h', p[2])


def p_new(p):
    '''new : NEW SHORT
           | NEW BYTE'''
    p[0] = opc_compile(p[1])
    p[0] += struct.pack('>h', p[2])


def p_dup(p):
    '''dup : DUP'''
    p[0] = opc_compile(p[1])

def p_invokespecial(p):
    '''invokespecial : INVOKESPECIAL SHORT
                     | INVOKESPECIAL BYTE'''
    p[0] = opc_compile(p[1])
    p[0] += struct.pack('>h', p[2])


def p_invokevirtual(p):
    '''invokevirtual : INVOKEVIRTUAL SHORT
                     | INVOKEVIRTUAL BYTE
                     | INVOKEVIRTUAL IDENTIFIER'''

    isString = False
    cp = cf.constant_pool

    print("Inside invokevirtual")

    try:
        p[2] = int(p[2])
    except:
        isString = True

    if not isString:
        p[0] = opc_compile(p[1])
        p[0] += struct.pack('>h', p[2])
    else:
        print("inside invokevirtual 2")
        p[0] = opc_compile(p[1])
        method_name = None
        found = False

        mri_index = 1
        for i in cp.entries[1:]:
            if i.tag == CONSTANT_METHODREF:
                    nat_index = i.name_and_type_index
                    method_name = cp.entries[cp.entries[nat_index].name_index].get_bytes_as_str()
                    print("method_name = %s" % method_name)
                    if method_name == p[2]:
                        found = True
                        break

            mri_index += 1

        if found:
            print("Found on index %d" % mri_index)
            p[0] += struct.pack('>h', mri_index)

def p_ldc(p):
    '''ldc : LDC BYTE'''
    p[0] = opc_compile(p[1])
    p[0] += bytes([p[2]])


def p_bipush(p):
    '''bipush : BIPUSH BYTE'''
    p[0] = opc_compile(p[1])
    p[0] += bytes([p[2]])



def p_ireturn(p):
    '''ireturn : IRETURN'''
    p[0] = opc_compile(p[1])


def p_return(p):
    '''return : RETURN'''
    p[0] = opc_compile(p[1])

def p_aconst_null(p):
    '''aconst_null : ACONST_NULL'''
    p[0] = b'\x01'
    #print("aconst_null: p[0]", p[0])

def p_iconst_m1(p):
    '''iconst_m1 : ICONST_M1'''
    p[0] = b'\x02'
    #print("iconst_m1: p[0]", p[0])


def p_iconst_0(p):
    '''iconst_0 : ICONST_0'''
    p[0] = b'\x03'


def p_iconst_1(p):
    '''iconst_1 : ICONST_1'''
    p[0] = b'\x04'


def p_iconst_2(p):
    '''iconst_2 : ICONST_2'''
    p[0] = b'\x05'


def p_iconst_3(p):
    '''iconst_3 : ICONST_3'''
    p[0] = b'\x06'

def p_iconst_4(p):
    '''iconst_4 : ICONST_4'''
    p[0] = b'\x07'

def p_iconst_5(p):
    '''iconst_5 : ICONST_5'''
    p[0] = b'\x08'




# ----------------------------------------------------------------------------
# Access modifiers for class/fields parsing
# ----------------------------------------------------------------------------
def p_access_modifiers(p):
    ''' access_modifiers : access_modifiers ACCESS_MODIFIER
                         | empty ACCESS_MODIFIER
                         | empty'''

    #print("Adding access_modifier: ", p[2])
    if p[2]:
        g_method.access_modifiers.append(p[2])

# ----------------------------------------------------------------------------
# Class fields parsing
# ----------------------------------------------------------------------------
def p_fields(p):
    '''fields : fields field
              | empty field'''
    pass

def p_field(p):
    '''field : VAR access_modifiers RET_TYPE IDENTIFIER'''
    #print("FIELD: %s %s %s %s" % (p[1], p[2], p[3], p[4]))

    cp = cf.constant_pool

    name = p[4]
    ret_type = ClassFileHelper.translate_type(p[3])
    access_flags = ClassFileHelper.translate_access_flags(g_method.access_modifiers)
    name_and_type_index = cp.add_nameandtypeinfo(name, ret_type)
    name_and_type_info  = cp.entries[name_and_type_index]

    field = FieldInfo(cp)
    field.access_flags = access_flags
    field.name_index = name_and_type_info.name_index
    field.descriptor_index = name_and_type_info.descriptor_index
    field.attributes_count = 0

    cf.add_class_field(field)


# ----------------------------------------------------------------------------
# External functions
# ----------------------------------------------------------------------------

def compile(classfile, code):
    global cf

    cf = classfile
    lexer = lex.lex(module=tok)
    parser = yacc.yacc(start='start')

    parser.parse(code)

