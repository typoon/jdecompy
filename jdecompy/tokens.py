import ply.lex as lex

t_ignore = '\t\r '

def t_error(t):
    print("Illegal char '%s' on line %d" % (t.value[0], t.lineno))



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
    # General asm identifiers
	'VAR_BYTE',
    'VAR_CHAR',
    'VAR_DOUBLE',
    'VAR_FLOAT',
    'VAR_INT',
    'VAR_LONG',
    'VAR_SHORT',
    'VAR_BOOL',
    'VAR_STRING',
    'VAR_OTHERTYPE',
	'DEREF',
    'ACCESS_MODIFIER',
    'STATIC_MODIFIER',
    'FINAL_MODIFIER',

#%token <identifier> IDENTIFIER

    'IDENTIFIER',
	'METHOD_START',
    'METHOD_IDENTIFIER',
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

t_STRING = r'["]([^\\"]+|\\.)*["]'

t_VAR_BYTE = r'[\.]byte'
t_VAR_CHAR = r'[\.]char'
t_VAR_DOUBLE = r'[\.]double'
t_VAR_FLOAT = r'[\.]float'
t_VAR_INT = r'[\.]int'
t_VAR_LONG = r'[\.]long'
t_VAR_SHORT = r'[\.]short'
t_VAR_BOOL = r'[\.]bool'
t_VAR_STRING = r'[\.]string'
t_VAR_OTHERTYPE = r'[\.]class\/[a-zA-Z\.]+' # TODO: This is awful

t_METHOD_START = r'[\.]method'
t_METHOD_END = r'[\.]method_end'
t_PARAMS = r'[\(][a-zA-Z\[;\/]*[\)][a-zA-Z\[;\/]*' 
t_IDENTIFIER = r'[$][a-zA-Z_$]+'

reserved = {
    # Access modifiers
    'public' :  'ACCESS_MODIFIER',
    'private' : 'ACCESS_MODIFIER',
    'protected' : 'ACCESS_MODIFIER',

    'static' : 'STATIC_MODIFIER',
    'final' : 'FINAL_MODIFIER',

    # opcodes
    'nop'           :  'NOP',           
    'aconst_null'   :  'ACONST_NULL',   
    'iconst_m1'     :  'ICONST_M1',     
    'iconst_0'      :  'ICONST_0',      
    'iconst_1'      :  'ICONST_1',      
    'iconst_2'      :  'ICONST_2',      
    'iconst_3'      :  'ICONST_3',      
    'iconst_4'      :  'ICONST_4',      
    'iconst_5'      :  'ICONST_5',      
    'lconst_0'      :  'LCONST_0',      
    'lconst_1'      :  'LCONST_1',      
    'fconst_0'      :  'FCONST_0',      
    'fconst_1'      :  'FCONST_1',      
    'fconst_2'      :  'FCONST_2',      
    'dconst_0'      :  'DCONST_0',      
    'dconst_1'      :  'DCONST_1',      
    'bipush'        :  'BIPUSH',        
    'sipush'        :  'SIPUSH',        
    'ldc'           :  'LDC',           
    'ldc_w'         :  'LDC_W',         
    'ldc2_w'        :  'LDC2_W',        
    'aaload'        :  'AALOAD',        
    'return'        :  'RETURN',        
    'getstatic'     :  'GETSTATIC',     
    'newarray'      :  'NEWARRAY',      
    'pop'           :  'POP',           
    'pop2'          :  'POP2',          
    'dup'           :  'DUP',           
    'invokevirtual' :  'INVOKEVIRTUAL', 
    'invokestatic'  :  'INVOKESTATIC',  
}


def t_METHOD_IDENTIFIER(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value, 'METHOD_IDENTIFIER')
    return t


