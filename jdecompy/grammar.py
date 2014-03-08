import ply.yacc as yacc
import ply.lex as lex
import tokens as tok
from tokens import tokens

cf = None

def p_start(p):
    '''start : identifiers methods
             | identifiers
             | methods'''
    pass

def p_identifiers(p):
    '''identifiers : identifiers var
                   | var'''
    pass

def p_methods(p):
    '''methods : methods STATIC_MODIFIER ACCESS_MODIFIER METHOD_START METHOD_IDENTIFIER PARAMS
               | methods ACCESS_MODIFIER METHOD_START METHOD_IDENTIFIER PARAMS
               | ACCESS_MODIFIER METHOD_START METHOD_IDENTIFIER PARAMS'''
    pass

def p_var(p):
    '''var : STATIC_MODIFIER FINAL_MODIFIER ACCESS_MODIFIER var_int
           | FINAL_MODIFIER ACCESS_MODIFIER var_int
           | STATIC_MODIFIER ACCESS_MODIFIER var_int
           | ACCESS_MODIFIER var_int'''

    print("Accessei o p_var\n")
    pass

def p_var_int(p):
    '''var_int : VAR_INT IDENTIFIER BYTE
              | VAR_INT IDENTIFIER INT
              | VAR_INT IDENTIFIER'''

    print("Accessei o p_var_int\n")
    print(p)
    # TODO: Need to loop over all access modifiers (p[-1] and less) here and put them in an array
    #       Not sure thou how to figure out how many are there :\
    cf.add_class_field([p[-1]], p[2], 'int')
    print("Fim p_var_int")

def p_error(p):
    print("Error: %s" % p)

def compile(classfile, code):
    global cf
    cf = classfile
    lexer = lex.lex(module=tok)
    parser = yacc.yacc(start='start')
    r = parser.parse(code)
    print(r)


