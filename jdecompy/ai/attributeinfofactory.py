import struct
from constants import *
import ai

class AttributeInfoFactory:

    def __init__(self):
        pass

    @staticmethod
    def create(name, constant_pool):
        attr = None

        if name == ATTR_CONSTANTVALUE:
            attr = ai.AttributeConstantValue(constant_pool)

        elif name == ATTR_CODE:
            attr = ai.AttributeCode(constant_pool)

        elif name == ATTR_STACKMAPTABLE:
            attr = ai.AttributeStackMapTable(constant_pool)

        elif name == ATTR_EXCEPTIONS:
            attr = ai.AttributeExceptions(constant_pool)

        elif name == ATTR_INNERCLASSES:
            attr = ai.AttributeInnerClasses(constant_pool)

        elif name == ATTR_SYNTHETIC:
            attr = ai.AttributeSynthetic(constant_pool)

        elif name == ATTR_SOURCEFILE:
            attr = ai.AttributeSourceFile(constant_pool)

        elif name == ATTR_LINENUMBERTABLE:
            attr = ai.AttributeLineNumberTable(constant_pool)

        elif name == ATTR_LOCALVARIABLETABLE:
            attr = ai.AttributeLocalVariableTable(constant_pool)

        elif name == ATTR_DEPRECATED:
            attr = ai.AttributeDeprecated(constant_pool)

        elif name == ATTR_ENCLOSINGMETHOD:
            attr = ai.AttributeEnclosingMethod(constant_pool)

        elif name == ATTR_SIGNATURE:
            attr = ai.AttributeSignature(constant_pool)

        elif name == ATTR_SOURCEDEBUGEXTENSION:
            attr = ai.AttributeSourceDebugExtension(constant_pool)

        elif name == ATTR_LOCALVARIABLETYPETABLE:
            attr = ai.AttributeLocalVariableTable(constant_pool)

        elif name == ATTR_RUNTIMEVISIBLEANNOTATIONS:
            attr = ai.AttributeRuntimeVisibleAnnotations(constant_pool)

        elif name == ATTR_RUNTIMEINVISIBLEANNOTATIONS:
            attr = ai.AttributeRuntimeInvisibleAnnotations(constant_pool)

        elif name == ATTR_RUNTIMEVISIBLEPARAMETERANNOTATIONS:
            attr = ai.AttributeRuntimeVisibleParameterAnnotations(constant_pool)

        elif name == ATTR_RUNTIMEINVISIBLEPARAMETERANNOTATIONS:
            attr = ai.AttributeRuntimeInvisibleParameterAnnotations(constant_pool)

        elif name == ATTR_ANNOTATIONDEFAULT:
            attr = ai.AttributeAnnotationDefault(constant_pool)

        return attr
