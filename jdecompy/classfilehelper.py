from constants import *

class ClassFileHelper:

    @staticmethod
    def translate_access_flags(af):
        access_flags = 0

        for i in af:
            if i == "public":
                access_flags |= ACC_PUBLIC

            elif i == "private":
                access_flags |= ACC_PRIVATE

            elif i == "protected":
                access_flags |= ACC_PROTECTED

            elif i == "static":
                access_flags |= ACC_STATIC

            elif i == "final":
                access_flags |= ACC_FINAL

            elif i == "volatile":
                access_flags |= ACC_VOLATILE

            elif i == "transient":
                access_flags |= ACC_TRANSIENT

            elif i == "synchronized":
                access_flags |= ACC_SYNCHRONIZED

            elif i == "native":
                access_flags |= ACC_NATIVE

            elif i == "abstract":
                access_flags |= ACC_ABSTRACT

            elif i == "strict":
                access_flags |= ACC_STRICT

            elif i == "super":
                access_flags |= ACC_SUPER

            elif i == "interface":
                access_flags |= ACC_INTERFACE

        return access_flags

    @staticmethod
    def translate_type(type):
        if type == 'byte':
            type = 'B'
        elif type == 'char':
            type = 'C'
        elif type == 'double':
            type = 'D'
        elif type == 'float':
            type = 'F'
        elif type == 'int':
            type = 'I'
        elif type == 'long':
            type = 'L'
        elif type == 'short':
            type = 'S'
        elif type == 'bool':
            type = 'Z'

        # TODO: if type has a '.' in it, it should be replaced with a /

        return type


