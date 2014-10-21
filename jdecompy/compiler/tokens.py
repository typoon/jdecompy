import ply.lex as lex

t_ignore = '\t\r '

def t_error(t):
    print("Illegal char '%s' on line %d" % (t.value[0], t.lineno))


states = (
    ('sttvar', 'inclusive'),
    ('sttmethod', 'exclusive'),
    ('sttaccessmod', 'exclusive'),
    ('sttrettype', 'exclusive'),
)

tokens = (
    # Data Types
    'BYTE',
    'CHAR',
    'DOUBLE',
    'FLOAT',
    'INT',
    'LONG',
    'SHORT',
    'BOOL',
    'STRING',
    'NUMBER',
    'HEXNUMBER',
    'ARRAY',


    # Variable/field related
    'VAR',
    'VAR_NAME',

    # Access modifiers
    'ACCESS_MODIFIER',

    # Return type
    'RET_TYPE',

#%token <identifier> IDENTIFIER

    'IDENTIFIER',
	'METHOD_START',
    'METHOD_IDENTIFIER',
    'METHOD_NAME',
#%token <identifier> METHOD_IDENTIFIER
#%token <param> PARAMS
    'PARAMS',
	'METHOD_END',
#%token <visibility> VISIBILITY

    # Opcodes
	'NOP',
	'ACONST_NULL',
	'ICONST_M1',
	'ICONST_0',
	'ICONST_1',
	'ICONST_2',
	'ICONST_3',
	'ICONST_4',
	'ICONST_5',
	'LCONST_0',
	'LCONST_1',
	'FCONST_0',
	'FCONST_1',
	'FCONST_2',
	'DCONST_0',
	'DCONST_1',
	'BIPUSH',
	'SIPUSH',
	'LDC',
	'LDC_W',
	'LDC2_W',
	'ILOAD',
	'LLOAD',
	'FLOAD',
	'DLOAD',
	'ALOAD',
	'ILOAD_0',
	'ILOAD_1',
	'ILOAD_2',
	'ILOAD_3',
	'LLOAD_0',
	'LLOAD_1',
	'LLOAD_2',
	'LLOAD_3',
	'FLOAD_0',
	'FLOAD_1',
	'FLOAD_2',
	'FLOAD_3',
	'DLOAD_0',
	'DLOAD_1',
	'DLOAD_2',
	'DLOAD_3',
	'ALOAD_0',
	'ALOAD_1',
	'ALOAD_2',
	'ALOAD_3',
	'IALOAD',
	'LALOAD',
	'FALOAD',
	'DALOAD',
	'AALOAD',
	'BALOAD',
	'CALOAD',
	'SALOAD',
	'ISTORE',
	'LSTORE',
	'FSTORE',
	'DSTORE',
	'ASTORE',
	'ISTORE_0',
	'ISTORE_1',
	'ISTORE_2',
	'ISTORE_3',
	'LSTORE_0',
	'LSTORE_1',
	'LSTORE_2',
	'LSTORE_3',
	'FSTORE_0',
	'FSTORE_1',
	'FSTORE_2',
	'FSTORE_3',
	'DSTORE_0',
	'DSTORE_1',
	'DSTORE_2',
	'DSTORE_3',
	'ASTORE_0',
	'ASTORE_1',
	'ASTORE_2',
	'ASTORE_3',
	'IASTORE',
	'LASTORE',
	'FASTORE',
	'DASTORE',
	'AASTORE',
	'BASTORE',
	'CASTORE',
	'SASTORE',
	'POP',
	'POP2',
	'DUP',
	'DUP_X1',
	'DUP_X2',
	'DUP2',
	'DUP2_X1',
	'DUP2_X2',
	'SWAP',
	'IADD',
	'LADD',
	'FADD',
	'DADD',
	'ISUB',
	'LSUB',
	'FSUB',
	'DSUB',
	'IMUL',
	'LMUL',
	'FMUL',
	'DMUL',
	'IDIV',
	'LDIV',
	'FDIV',
	'DDIV',
	'IREM',
	'LREM',
	'FREM',
	'DREM',
	'INEG',
	'LNEG',
	'FNEG',
	'DNEG',
	'ISHL',
	'LSHL',
	'ISHR',
	'LSHR',
	'IUSHR',
	'LUSHR',
	'IAND',
	'LAND',
	'IOR',
	'LOR',
	'IXOR',
	'LXOR',
	'IINC',
	'I2L',
	'I2F',
	'I2D',
	'L2I',
	'L2F',
	'L2D',
	'F2I',
	'F2L',
	'F2D',
	'D2I',
	'D2L',
	'D2F',
	'I2B',
	'I2C',
	'I2S',
	'LCMP',
	'FCMPL',
	'FCMPG',
	'DCMPL',
	'DCMPG',
	'IFEQ',
	'IFNE',
	'IFLT',
	'IFGE',
	'IFGT',
	'IFLE',
	'IF_ICMPEQ',
	'IF_ICMPNE',
	'IF_ICMPLT',
	'IF_ICMPGE',
	'IF_ICMPGT',
	'IF_ICMPLE',
	'IF_ACMPEQ',
	'IF_ACMPNE',
	'GOTO',
	'JSR',
	'RET',
	'TABLESWITCH',
	'LOOKUPSWITCH',
	'IRETURN',
	'LRETURN',
	'FRETURN',
	'DRETURN',
	'ARETURN',
	'RETURN',
	'GETSTATIC',
	'PUTSTATIC',
	'GETFIELD',
	'PUTFIELD',
	'INVOKEVIRTUAL',
	'INVOKESPECIAL',
	'INVOKESTATIC',
	'INVOKEINTERFACE',
	'NEW',
	'NEWARRAY',
	'ANEWARRAY',
	'ARRAYLENGTH',
	'ATHROW',
	'CHECKCAST',
	'INSTANCEOF',
	'MONITORENTER',
	'MONITOREXIT',
	'WIDE',
	'MULTIANEWARRAY',
	'IFNULL',
	'IFNONNULL',
	'GOTO_W',
	'JSR_W',
	'BREAKPOINT',
	'LDC_QUICK',
	'LDC_W_QUICK',
	'LDC2_W_QUICK',
	'GETFIELD_QUICK',
	'PUTFIELD_QUICK',
	'GETFIELD2_QUICK',
	'PUTFIELD2_QUICK',
	'GETSTATIC_QUICK',
	'PUTSTATIC_QUICK',
	'GETSTATIC2_QUICK',
	'PUTSTATIC2_QUICK',
	'INVOKEVIRTUAL_QUICK',
	'INVOKENONVIRTUAL_QUICK',
	'INVOKESUPER_QUICK',
	'INVOKESTATIC_QUICK',
	'INVOKEINTERFACE_QUICK',
	'INVOKEVIRTUALOBJECT_QUICK',
	'INVOKEIGNORED_QUICK',
	'NEW_QUICK',
	'ANEWARRAY_QUICK',
	'MULTIANEWARRAY_QUICK',
	'CHECKCAST_QUICK',
	'INSTANCEOF_QUICK',
	'INVOKEVIRTUAL_QUICK_W',
	'GETFIELD_QUICK_W',
	'PUTFIELD_QUICK_W',
	'NONNULL_QUICK',
	'SOFTWARE',
	'HARDWARE'
)

# ---------------------------------------------------------
# Rules for state INITIAL
# ---------------------------------------------------------
def t_NUMBER(t):
    r'[1-9]+[0-9]*'
    t.value = int(t.value)

    if t.value <= 255:
        t.type = 'BYTE'
    else:
        t.type = 'INT'

    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_HEXNUMBER(t):
    r'0x[0-9a-fA-F]{1,8}'
    t.value = int(t.value, 0)

    if t.value <= 255:
        t.type = 'BYTE'
    else:
        t.type = 'INT'

    return t


def t_sttvar(t):
    r'[\.]var'
    t.lexer.push_state('sttvar')
    t.lexer.push_state('sttaccessmod')
    t.type = 'VAR'
    return t

def t_sttmethod(t):
    r'[\.]method'
    t.lexer.push_state('sttmethod')
    t.lexer.push_state('sttaccessmod')
    t.type = 'METHOD_START'
    return t

t_STRING = r'["]([^\\"]+|\\.)*["]'

t_ANY_IDENTIFIER = r'\w+'

# ---------------------------------------------------------
# Rules for state sttvar 
# ---------------------------------------------------------
t_sttvar_ignore = '\t\r '
t_sttvar_ARRAY = r'[\[][1-9]*[\]]'

def t_sttvar_error(t):
    print("Illegal variable declaration. Char '%s' on line %d" % (t.value[0], t.lineno))


#def t_sttvar_VAR_NAME(t):
#    r'\w+'
#    return t


def t_sttvar_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.pop_state()

# ---------------------------------------------------------
# Rules for state sttmethod
# ---------------------------------------------------------
t_sttmethod_ignore = '\t\r '

#def t_sttmethod_PARAMS(t):
#    r'[\(][a-zA-Z\[;\/]*[\)][a-zA-Z\[;\/]*'
#    return t


def t_sttmethod_PARAMS(t):
    r'[\(][0-9a-zA-Z\[;\/]*[\)][a-zA-Z\[;\/]*'
    return t

def t_sttmethod_error(t):
    print("Illegal method declaration. Char '%s' on line %d" % (t.value[0], t.lineno))

def t_sttmethod_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_sttmethod_METHOD_END(t):
    r'[\.]method_end'
    t.lexer.pop_state()
    return t

def t_sttmethod_sttvar(t):
    r'[\.]var'
    t.lexer.push_state('sttvar')
    t.lexer.push_state('sttaccessmod')
    t.type = 'VAR'
    return t


opcodes = {
    # opcodes
    'nop': 'NOP',
    'aconst_null': 'ACONST_NULL',
    'iconst_m1': 'ICONST_M1',
    'iconst_0': 'ICONST_0',
    'iconst_1': 'ICONST_1',
    'iconst_2': 'ICONST_2',
    'iconst_3': 'ICONST_3',
    'iconst_4': 'ICONST_4',
    'iconst_5': 'ICONST_5',
    'lconst_0': 'LCONST_0',
    'lconst_1': 'LCONST_1',
    'fconst_0': 'FCONST_0',
    'fconst_1': 'FCONST_1',
    'fconst_2': 'FCONST_2',
    'dconst_0': 'DCONST_0',
    'dconst_1': 'DCONST_1',
    'bipush': 'BIPUSH',
    'sipush': 'SIPUSH',
    'ldc': 'LDC',
    'ldc_w': 'LDC_W',
    'ldc2_w': 'LDC2_W',
    'iload': 'ILOAD',
    'lload': 'LLOAD',
    'fload': 'FLOAD',
    'dload': 'DLOAD',
    'aload': 'ALOAD',
    'iload_0': 'ILOAD_0',
    'iload_1': 'ILOAD_1',
    'iload_2': 'ILOAD_2',
    'iload_3': 'ILOAD_3',
    'lload_0': 'LLOAD_0',
    'lload_1': 'LLOAD_1',
    'lload_2': 'LLOAD_2',
    'lload_3': 'LLOAD_3',
    'fload_0': 'FLOAD_0',
    'fload_1': 'FLOAD_1',
    'fload_2': 'FLOAD_2',
    'fload_3': 'FLOAD_3',
    'dload_0': 'DLOAD_0',
    'dload_1': 'DLOAD_1',
    'dload_2': 'DLOAD_2',
    'dload_3': 'DLOAD_3',
    'aload_0': 'ALOAD_0',
    'aload_1': 'ALOAD_1',
    'aload_2': 'ALOAD_2',
    'aload_3': 'ALOAD_3',
    'iaload': 'IALOAD',
    'laload': 'LALOAD',
    'faload': 'FALOAD',
    'daload': 'DALOAD',
    'aaload': 'AALOAD',
    'baload': 'BALOAD',
    'caload': 'CALOAD',
    'saload': 'SALOAD',
    'istore': 'ISTORE',
    'lstore': 'LSTORE',
    'fstore': 'FSTORE',
    'dstore': 'DSTORE',
    'astore': 'ASTORE',
    'istore_0': 'ISTORE_0',
    'istore_1': 'ISTORE_1',
    'istore_2': 'ISTORE_2',
    'istore_3': 'ISTORE_3',
    'lstore_0': 'LSTORE_0',
    'lstore_1': 'LSTORE_1',
    'lstore_2': 'LSTORE_2',
    'lstore_3': 'LSTORE_3',
    'fstore_0': 'FSTORE_0',
    'fstore_1': 'FSTORE_1',
    'fstore_2': 'FSTORE_2',
    'fstore_3': 'FSTORE_3',
    'dstore_0': 'DSTORE_0',
    'dstore_1': 'DSTORE_1',
    'dstore_2': 'DSTORE_2',
    'dstore_3': 'DSTORE_3',
    'astore_0': 'ASTORE_0',
    'astore_1': 'ASTORE_1',
    'astore_2': 'ASTORE_2',
    'astore_3': 'ASTORE_3',
    'iastore': 'IASTORE',
    'lastore': 'LASTORE',
    'fastore': 'FASTORE',
    'dastore': 'DASTORE',
    'aastore': 'AASTORE',
    'bastore': 'BASTORE',
    'castore': 'CASTORE',
    'sastore': 'SASTORE',
    'pop': 'POP',
    'pop2': 'POP2',
    'dup': 'DUP',
    'dup_x1': 'DUP_X1',
    'dup_x2': 'DUP_X2',
    'dup2': 'DUP2',
    'dup2_x1': 'DUP2_X1',
    'dup2_x2': 'DUP2_X2',
    'swap': 'SWAP',
    'iadd': 'IADD',
    'ladd': 'LADD',
    'fadd': 'FADD',
    'dadd': 'DADD',
    'isub': 'ISUB',
    'lsub': 'LSUB',
    'fsub': 'FSUB',
    'dsub': 'DSUB',
    'imul': 'IMUL',
    'lmul': 'LMUL',
    'fmul': 'FMUL',
    'dmul': 'DMUL',
    'idiv': 'IDIV',
    'ldiv': 'LDIV',
    'fdiv': 'FDIV',
    'ddiv': 'DDIV',
    'irem': 'IREM',
    'lrem': 'LREM',
    'frem': 'FREM',
    'drem': 'DREM',
    'ineg': 'INEG',
    'lneg': 'LNEG',
    'fneg': 'FNEG',
    'dneg': 'DNEG',
    'ishl': 'ISHL',
    'lshl': 'LSHL',
    'ishr': 'ISHR',
    'lshr': 'LSHR',
    'iushr': 'IUSHR',
    'lushr': 'LUSHR',
    'iand': 'IAND',
    'land': 'LAND',
    'ior': 'IOR',
    'lor': 'LOR',
    'ixor': 'IXOR',
    'lxor': 'LXOR',
    'iinc': 'IINC',
    'i2l': 'I2L',
    'i2f': 'I2F',
    'i2d': 'I2D',
    'l2i': 'L2I',
    'l2f': 'L2F',
    'l2d': 'L2D',
    'f2i': 'F2I',
    'f2l': 'F2L',
    'f2d': 'F2D',
    'd2i': 'D2I',
    'd2l': 'D2L',
    'd2f': 'D2F',
    'i2b': 'I2B',
    'i2c': 'I2C',
    'i2s': 'I2S',
    'lcmp': 'LCMP',
    'fcmpl': 'FCMPL',
    'fcmpg': 'FCMPG',
    'dcmpl': 'DCMPL',
    'dcmpg': 'DCMPG',
    'ifeq': 'IFEQ',
    'ifne': 'IFNE',
    'iflt': 'IFLT',
    'ifge': 'IFGE',
    'ifgt': 'IFGT',
    'ifle': 'IFLE',
    'if_icmpeq': 'IF_ICMPEQ',
    'if_icmpne': 'IF_ICMPNE',
    'if_icmplt': 'IF_ICMPLT',
    'if_icmpge': 'IF_ICMPGE',
    'if_icmpgt': 'IF_ICMPGT',
    'if_icmple': 'IF_ICMPLE',
    'if_acmpeq': 'IF_ACMPEQ',
    'if_acmpne': 'IF_ACMPNE',
    'goto': 'GOTO',
    'jsr': 'JSR',
    'ret': 'RET',
    'tableswitch': 'TABLESWITCH',
    'lookupswitch': 'LOOKUPSWITCH',
    'ireturn': 'IRETURN',
    'lreturn': 'LRETURN',
    'freturn': 'FRETURN',
    'dreturn': 'DRETURN',
    'areturn': 'ARETURN',
    'return': 'RETURN',
    'getstatic': 'GETSTATIC',
    'putstatic': 'PUTSTATIC',
    'getfield': 'GETFIELD',
    'putfield': 'PUTFIELD',
    'invokevirtual': 'INVOKEVIRTUAL',
    'invokespecial': 'INVOKESPECIAL',
    'invokestatic': 'INVOKESTATIC',
    'invokeinterface': 'INVOKEINTERFACE',
    'reserved': 'RESERVED',
    'new': 'NEW',
    'newarray': 'NEWARRAY',
    'anewarray': 'ANEWARRAY',
    'arraylength': 'ARRAYLENGTH',
    'athrow': 'ATHROW',
    'checkcast': 'CHECKCAST',
    'instanceof': 'INSTANCEOF',
    'monitorenter': 'MONITORENTER',
    'monitorexit': 'MONITOREXIT',
    'wide': 'WIDE',
    'multianewarray': 'MULTIANEWARRAY',
    'ifnull': 'IFNULL',
    'ifnonnull': 'IFNONNULL',
    'goto_w': 'GOTO_W',
    'jsr_w': 'JSR_W',
    'breakpoint': 'BREAKPOINT',
    'ldc_quick': 'LDC_QUICK',
    'ldc_w_quick': 'LDC_W_QUICK',
    'ldc2_w_quick': 'LDC2_W_QUICK',
    'getfield_quick': 'GETFIELD_QUICK',
    'putfield_quick': 'PUTFIELD_QUICK',
    'getfield2_quick': 'GETFIELD2_QUICK',
    'putfield2_quick': 'PUTFIELD2_QUICK',
    'getstatic_quick': 'GETSTATIC_QUICK',
    'putstatic_quick': 'PUTSTATIC_QUICK',
    'getstatic2_quick': 'GETSTATIC2_QUICK',
    'putstatic2_quick': 'PUTSTATIC2_QUICK',
    'invokevirtual_quick': 'INVOKEVIRTUAL_QUICK',
    'invokenonvirtual_quick': 'INVOKENONVIRTUAL_QUICK',
    'invokesuper_quick': 'INVOKESUPER_QUICK',
    'invokestatic_quick': 'INVOKESTATIC_QUICK',
    'invokeinterface_quick': 'INVOKEINTERFACE_QUICK',
    'invokevirtualobject_quick': 'INVOKEVIRTUALOBJECT_QUICK',
    'invokeignored_quick': 'INVOKEIGNORED_QUICK',
    'new_quick': 'NEW_QUICK',
    'anewarray_quick': 'ANEWARRAY_QUICK',
    'multianewarray_quick': 'MULTIANEWARRAY_QUICK',
    'checkcast_quick': 'CHECKCAST_QUICK',
    'instanceof_quick': 'INSTANCEOF_QUICK',
    'invokevirtual_quick_w': 'INVOKEVIRTUAL_QUICK_W',
    'getfield_quick_w': 'GETFIELD_QUICK_W',
    'putfield_quick_w': 'PUTFIELD_QUICK_W',
    'nonnull_quick': 'NONNULL_QUICK',
    'software': 'SOFTWARE',
    'hardware': 'HARDWARE'
}

def t_sttmethod_opcodes(t):
    r'[_a-zA-Z]+[_0-9a-zA-Z]*'
    t.type = opcodes.get(t.value, 'IDENTIFIER')

    #print(vars(t))
    return t

def t_sttmethod_NUMBER(t):
    r'[1-9]+[0-9]*'
    t.value = int(t.value)

    if t.value <= 255:
        t.type = 'BYTE'
    elif t.value <= 65535:
        t.type = 'SHORT'
    else:
        t.type = 'INT'

    return t





# ---------------------------------------------------------
# Rules for state sttaccessmod
# ---------------------------------------------------------
t_sttaccessmod_ignore = '\t\r '

reserved_sttaccessmod = {
    'public'    : 'ACCESS_MODIFIER',
    'private'   : 'ACCESS_MODIFIER',
    'protected' : 'ACCESS_MODIFIER',
    'static'    : 'ACCESS_MODIFIER',
    'synthetic' : 'ACCESS_MODIFIER',
    'volatile'  : 'ACCESS_MODIFIER',
    'transient' : 'ACCESS_MODIFIER',
    'final'     : 'ACCESS_MODIFIER',
}


def t_sttaccessmod_error(t):
    print("Illegal access modifier declaration. Char '%s' on line %d" % (t.value[0], t.lineno))


def t_sttaccessmod_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.pop_state()

def t_sttaccessmod_reserved(t):
    r'\w+'
    t.type = reserved_sttaccessmod.get(t.value, 'OTHER')

    if t.type == 'OTHER': # We probably parsed the ret type
        t.lexer.pop_state()
        t.lexer.push_state('sttrettype')
        
        # We need to reparse the current token. How to do that?
        # I guess the following workaround might do it
        t.lexer.skip(len(t.value)*-1)

    else:
        return t


# ---------------------------------------------------------
# Rules for state sttrettype
# ---------------------------------------------------------
t_sttrettype_ignore = '\t\r '

def t_sttrettype_error(t):
    print("Invalid type. Char '%s' on line %d" % (t.value[0], t.lineno))

def t_sttrettype_RET_TYPE(t):
    r'(\w+)(\.\w+)*'
    t.type = 'RET_TYPE'
    t.lexer.pop_state()
    return t


def test(data):
   lexer = lex.lex()
   lexer.input(data)
   while True:
       tok = lexer.token()
       if not tok: break
       print(tok)
