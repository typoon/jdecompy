import ply.yacc as yacc
import ply.lex as lex
import tokens as tok
from tokens import tokens


cf = None

def p_empty(p):
    '''empty :'''
    pass

def p_start(p):
    '''start : fields
             | empty'''
    pass

def p_fields(p):
    '''fields : vars'''
    pass

def p_vars(p):
    '''vars : vars var
            | empty var'''
    pass

def p_var(p):
    '''var : VAR access_modifiers VAR_TYPE VAR_NAME'''
    print("%s %s %s %s" % (p[1], p.modifiers, p[3], p[4]))

    if not cf.add_class_field(p.modifiers, p[3], p[4]):
        print(cf.get_error())
        raise SyntaxError


def p_access_modifiers(p):
    ''' access_modifiers : access_modifiers ACCESS_MODIFIER
                         | empty ACCESS_MODIFIER'''

    if not hasattr(p, 'modifiers'):
        p.modifiers = []

    p.modifiers.append(p[2])


# def p_start(p):
#     '''start : identifiers methods
#              | identifiers
#              | methods'''
#     pass
# 
# def p_identifiers(p):
#     '''identifiers : identifiers var
#                    | var'''
#     pass
# 
# def p_methods(p):
#     '''methods : methods STATIC_MODIFIER ACCESS_MODIFIER METHOD_START METHOD_IDENTIFIER PARAMS
#                | methods ACCESS_MODIFIER METHOD_START METHOD_IDENTIFIER PARAMS
#                | ACCESS_MODIFIER METHOD_START METHOD_IDENTIFIER PARAMS'''
#     pass
# 
# def p_var(p):
#     '''var : STATIC_MODIFIER FINAL_MODIFIER ACCESS_MODIFIER var_int
#            | FINAL_MODIFIER ACCESS_MODIFIER var_int
#            | STATIC_MODIFIER ACCESS_MODIFIER var_int
#            | ACCESS_MODIFIER var_int'''
# 
#     print("bla = %d" % p.bla)
#     pass
# 
# def p_var_int(p):
#     '''var_int : VAR_INT IDENTIFIER BYTE
#               | VAR_INT IDENTIFIER INT
#               | VAR_INT IDENTIFIER'''
# 
#     # TODO: Need to loop over all access modifiers (p[-1] and less) here and put them in an array
#     #       Not sure thou how to figure out how many are there :\
#     p.bla = 123
#     # cf.add_class_field([p[-1]], p[2], 'int')

def p_error(p):
    print("Unexpected token %s on line %d position %d (%s)" % (p.type, p.lineno, p.lexpos, p.value))

def compile(classfile, code):
    global cf
    cf = classfile
    lexer = lex.lex(module=tok)
    parser = yacc.yacc(start='start')
    r = parser.parse(code)
    print(r)


