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
    def access_flags_to_str(af):
        access_flags = []

        if af & ACC_PUBLIC == ACC_PUBLIC:
            access_flags.append("public")

        if af & ACC_PRIVATE == ACC_PRIVATE:
            access_flags.append("private")

        if af & ACC_PROTECTED == ACC_PROTECTED:
            access_flags.append("protected")

        if af & ACC_STATIC == ACC_STATIC:
            access_flags.append("static")

        if af & ACC_FINAL == ACC_FINAL:
            access_flags.append("final")

        if af & ACC_VOLATILE == ACC_VOLATILE:
            access_flags.append("volatile")

        if af & ACC_TRANSIENT == ACC_TRANSIENT:
            access_flags.append("transient")

        if af & ACC_SYNCHRONIZED == ACC_SYNCHRONIZED:
            access_flags.append("synchronized")

        if af & ACC_NATIVE == ACC_NATIVE:
            access_flags.append("native")

        if af & ACC_ABSTRACT == ACC_ABSTRACT:
            access_flags.append("abstract")

        if af & ACC_STRICT == ACC_STRICT:
            access_flags.append("strict")

        if af & ACC_SUPER == ACC_SUPER:
            access_flags.append("super")

        if af & ACC_INTERFACE == ACC_INTERFACE:
            access_flags.append("interface")

        return ", ".join(access_flags)

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
        elif type == 'void':
            type = 'V'

        # TODO: if type has a '.' in it, it should be replaced with a /

        return type


