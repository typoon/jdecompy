import ply.yacc as yacc
import ply.lex as lex
import compiler.tokens as tok
from compiler.tokens import tokens
from opcodes import opc_compile
from methodinfo import MethodInfo
from classfilehelper import ClassFileHelper

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

    cp = cf.constant_pool
    mi = MethodInfo(cp)
    mi.access_flags = ClassFileHelper.translate_access_flags(g_method.access_modifiers)
    mi.name_index = cp.add_utf8info(g_method.name, len(g_method.name))


def p_method_start(p):
    '''method_start : METHOD_START access_modifiers RET_TYPE IDENTIFIER PARAMS'''
    print("Inside p_method_start")
    #g_method.access_modifiers = p[2]
    g_method.ret_type = p[3]
    g_method.name = p[4]
    g_method.params = p[5]


def p_method_body(p):
    '''method_body : vars
                   | empty mnemonics
                   | vars mnemonics
                   | empty'''

    print("Inside p_method_body")
    # TODO: Maybe this should be in p_mnemonics?
    if p[1] is None:
        return
    g_method.code = p[2]
    print("Method body... p[2] ", p[2])


def p_method_end(p):
    '''method_end : METHOD_END'''
    # TODO: All magic to handle the MethodTree object should happen here
    print("Inside p_method_end")

    pass

def p_mnemonics(p):
    '''mnemonics : mnemonics opcode
                 | empty opcode'''
    if not p[1]:
        p[1] = b''

    print("p[0] = ", p[0])
    print("p[1] = ", p[1])
    print("p[2] = ", p[2])
    p[1] += p[2]
    p[0] = p[1]
    print("mnemonics: p[0] ", p[0])

def p_opcode(p):
    '''opcode : nop
              | aconst_null
              | iconst_m1'''
    p[0] = p[1]
    print("opcode: p[0] ", p[0])


# ----------------------------------------------------------------------------
# Method variables parsing
# ----------------------------------------------------------------------------
def p_vars(p):
    '''vars : vars var
            | empty var'''
    pass

def p_var(p):
    '''var : VAR RET_TYPE IDENTIFIER'''
    print("VAR: %s %s %s"  % (p[1], p[2], p[3]))

    #if cf.add_class_field(p.modifiers, p[3], p[4]) is None:
    #    print(cf.get_error())
    #    raise SyntaxError


def p_var_array(p):
    '''var : VAR access_modifiers RET_TYPE array_types IDENTIFIER'''
    # TODO: Add arrays support
    print("Arrays not supported yet")
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
    print("Nop: p[0] ", p[0])

def p_aconst_null(p):
    '''aconst_null : ACONST_NULL'''
    p[0] = b'\x01'
    print("aconst_null: p[0]", p[0])

def p_iconst_m1(p):
    '''iconst_m1 : ICONST_M1'''
    p[0] = b'\x02'
    print("iconst_m1: p[0]", p[0])


# ----------------------------------------------------------------------------
# Access modifiers for class/fields parsing
# ----------------------------------------------------------------------------
def p_access_modifiers(p):
    ''' access_modifiers : access_modifiers ACCESS_MODIFIER
                         | empty ACCESS_MODIFIER
                         | empty'''

    print("Adding access_modifier: ", p[2])
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
    print("FIELD: %s %s %s %s" % (p[1], p.modifiers, p[3], p[4]))

    if cf.add_class_field(p.modifiers, p[3], p[4]) is None:
        print(cf.get_error())
        raise SyntaxError

    del p.modifiers


# ----------------------------------------------------------------------------
# External functions
# ----------------------------------------------------------------------------

def compile(classfile, code):
    global cf

    cf = classfile
    lexer = lex.lex(module=tok)
    parser = yacc.yacc(start='start')

    parser.parse(code)

