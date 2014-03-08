import re


class ConstantPoolUtils:

    @staticmethod
    def parse_field_type(info):
        ret_type = ''
        add_array = 0

        e = enumerate(info)
        for i, type in e:
            if type == 'I':
                ret_type = 'int'

            elif type == 'B':
                ret_type = 'byte'

            elif type == 'C':
                ret_type = 'char'

            elif type == 'D':
                ret_type = 'double'

            elif type == 'F':
                ret_type = 'float'

            elif type == 'J':
                ret_type = 'long'

            elif type == 'S':
                ret_type = 'short'

            elif type == 'Z':
                ret_type = 'boolean'

            elif type == 'V':
                ret_type = 'void'

            elif type == 'L':
                pos = info[i:].find(';') + i
                ret_type = info[i+1:pos]
                ret_type = ret_type.replace('/', '.')

                count = info[i:].find(';')
                while count > 0:
                    next(e)
                    count -= 1

            elif type == '[':
                add_array += 1

            while add_array > 0:
                ret_type += '[]'
                add_array -= 1

        return ret_type

    @staticmethod
    def parse_method_type(info):
        regex = re.match('\(([^()]*)\)(.*)', info).groups()
        p = regex[0]
        r = regex[1]
        params = []

        add_array = 0
        found_type = False
        e = enumerate(p)
        for i, type in e:
            if type == 'I':
                params.append('int')
                found_type = True

            elif type == 'B':
                params.append('byte')
                found_type = True

            elif type == 'C':
                params.append('char')
                found_type = True

            elif type == 'D':
                params.append('double')
                found_type = True

            elif type == 'F':
                params.append('float')
                found_type = True

            elif type == 'J':
                params.append('long')
                found_type = True

            elif type == 'S':
                params.append('short')
                found_type = True

            elif type == 'Z':
                params.append('boolean')
                found_type = True

            elif type == 'L':
                pos = p[i:].find(';') + i
                params.append(p[i+1:pos])
                found_type = True

                params[-1] = params[-1].replace('/', '.')

                count = p[i:].find(';')
                while count > 0:
                    next(e)
                    count -= 1

            elif type == '[':
                add_array += 1
                found_type = False

            if (found_type == True) and (add_array > 0):
                while add_array > 0:
                    params[-1] += '[]'
                    add_array -= 1

        ret = {'ret_type': ConstantPoolUtils.parse_field_type(r), 'params': params}
        return ret;
