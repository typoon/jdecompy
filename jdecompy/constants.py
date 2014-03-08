# JVM Constants
JAVA_MAGIC = 0xCAFEBABE

# Constants for the 'tag' component in the cp_info structure
CONSTANT_UTF8               = 1
CONSTANT_INTEGER            = 3
CONSTANT_FLOAT              = 4
CONSTANT_LONG               = 5
CONSTANT_DOUBLE             = 6
CONSTANT_CLASS              = 7
CONSTANT_STRING             = 8
CONSTANT_FIELDREF           = 9
CONSTANT_METHODREF          = 10
CONSTANT_INTERFACEMETHODREF = 11
CONSTANT_NAMEANDTYPE        = 12


# Constants for the 'access_flags' field in both the field_info and
# method_info structures
ACC_PUBLIC     = 0x0001 #Declared public; may be accessed from outside its package.
ACC_PRIVATE    = 0x0002 #Declared private; usable only within the defining class.
ACC_PROTECTED  = 0x0004 #Declared protected; may be accessed within subclasses.
ACC_STATIC     = 0x0008 #Declared static.
ACC_FINAL      = 0x0010 #Declared final; no further assignment after initialization.

# Constants for the 'access_flags' field in the field_info structure
ACC_VOLATILE   = 0x0040 #Declared volatile; cannot be cached.
ACC_TRANSIENT  = 0x0080 #Declared transient; not written or read by a persistent object manager.

# Constants for the 'access_flags' field in the method_info structure
ACC_SYNCHRONIZED = 0x0020 #Declared synchronized; invocation is wrapped in a monitor lock.
ACC_NATIVE       = 0x0100 #Declared native; implemented in a language other than Java.
ACC_ABSTRACT     = 0x0400 #Declared abstract; no implementation is provided.
ACC_STRICT       = 0x0800 #Declared strictfp; floating-point mode is FP-strict

# Constants for the 'access_flags' field in the ClassFile struct
#ACC_PUBLIC    = 0x0001
#ACC_FINAL     = 0x0010
ACC_SUPER      = 0x0020 #Treat superclass methods specially when invoked by the invokespecial instruction.
ACC_INTERFACE  = 0x0200 #Is an interface, not a class.
#ACC_ABSTRACT  = 0x0400 #Declared abstract; may not be instantiated.


# Constants for the Attribute Names
# In my opinion this is not very cool. Sun could/should have used tags for
# attribute types just as they did with the constant pool entries
ATTR_CONSTANTVALUE      = "ConstantValue"
ATTR_CODE               = "Code"
ATTR_STACKMAPTABLE      = "StackMapTable"
ATTR_EXCEPTIONS         = "Exceptions"
ATTR_INNERCLASSES       = "InnerClasses"
ATTR_SYNTHETIC          = "Synthetic"
ATTR_SOURCEFILE         = "SourceFile"
ATTR_LINENUMBERTABLE    = "LineNumberTable"
ATTR_LOCALVARIABLETABLE = "LocalVariableTable"
ATTR_DEPRECATED         = "Deprecated"


# Below attributes are currently not being read. They should be.
# Not reading them will cause class files with these attributes set to be read
# incorrectly
ATTR_ENCLOSINGMETHOD                      = "EnclosingMethod"
ATTR_SIGNATURE                            = "Signature"
ATTR_SOURCEDEBUGEXTENSION                 = "SourceDebugExtension"
ATTR_LOCALVARIABLETYPETABLE               = "LocalVariableTypeTable"
ATTR_RUNTIMEVISIBLEANNOTATIONS            = "RuntimeVisibleAnnotations"
ATTR_RUNTIMEINVISIBLEANNOTATIONS          = "RuntimeInvisibleAnnotations"
ATTR_RUNTIMEVISIBLEPARAMETERANNOTATIONS   = "RuntimeVisibleParameterAnnotations"
ATTR_RUNTIMEINVISIBLEPARAMETERANNOTATIONS = "RuntimeInvisibleParameterAnnotations"
ATTR_ANNOTATIONDEFAULT                    = "AnnotationDefault"

