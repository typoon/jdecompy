import ply.yacc as yacc
import ply.lex as lex
import tokens as tok
from tokens import tokens
from opcodes import opc_compile


cf = None
g_code = b''

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

    print("inside p_methods")
    print("p[1]", p[1])
    print("p[2]", p[2])
    print("p[3]", p[3])
    print("p[4]", p[4])

    pass

def p_method_start(p):
    '''method_start : METHOD_START access_modifiers RET_TYPE IDENTIFIER PARAMS'''
    if not hasattr(p, 'code'):
        p.code = b''

    print("p.code = ", p.code)

def p_method_body(p):
    '''method_body : vars
                   | mnemonics'''

    p[0] = p[1]
    print("Method body... p[0] ", p[0])

def p_method_body_2(p):
    '''method_body : vars mnemonics'''

    print("Method body 2")

def p_method_end(p):
    '''method_end : METHOD_END'''

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
# Access modifiers for class/fields parsing
# ----------------------------------------------------------------------------
def p_access_modifiers(p):
    ''' access_modifiers : access_modifiers ACCESS_MODIFIER
                         | empty ACCESS_MODIFIER
                         | empty'''

    if not hasattr(p, 'modifiers'):
        p.modifiers = []

    p.modifiers.append(p[2])


# ----------------------------------------------------------------------------
# External functions
# ----------------------------------------------------------------------------

def compile(classfile, code):
    global cf

    cf = classfile
    lexer = lex.lex(module=tok)
    parser = yacc.yacc(start='start')

    parser.parse(code)

