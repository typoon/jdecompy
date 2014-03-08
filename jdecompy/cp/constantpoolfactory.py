from constants import *
import cp


class ConstantPoolFactory:

    def __init__(self):
        pass

    @staticmethod
    def create(tag):
        obj = None

        if tag == CONSTANT_CLASS:
            obj = cp.ClassInfo()

        elif tag == CONSTANT_FIELDREF:
            obj = cp.FieldRefInfo()

        elif tag == CONSTANT_METHODREF:
            obj = cp.MethodRefInfo()

        elif tag == CONSTANT_INTERFACEMETHODREF:
            obj = cp.InterfaceMethodRefInfo()

        elif tag == CONSTANT_STRING:
            obj = cp.StringInfo()

        elif tag == CONSTANT_INTEGER:
            obj = cp.IntegerInfo()

        elif tag == CONSTANT_FLOAT:
            obj = cp.FloatInfo()

        elif tag == CONSTANT_LONG:
            obj = cp.LongInfo()

        elif tag == CONSTANT_DOUBLE:
            obj = cp.DoubleInfo()

        elif tag == CONSTANT_NAMEANDTYPE:
            obj = cp.NameAndTypeInfo()

        elif tag == CONSTANT_UTF8:
            obj = cp.Utf8Info()

        if obj is not None:
            obj.tag = tag

        return obj

