#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyright (C) 2018 Jingtao Lai
Parameter Parser
"""

import sys

_VALID_TRUE_VALUES = set(['true', '1', 1])
_VALID_FALSE_VALUES = set(['false', '0', 0])
_VALID_BOOLEAN_VALUES = _VALID_TRUE_VALUES | _VALID_FALSE_VALUES
_VALID_TYPES = set(['int', 'float', 'bool', 'str'])

def _is_int(string):
    """If string s is a int, return true, else return false
    """
    try:
        int(string)
        return True
    except ValueError:
        return False

def _is_float(string):
    """If string s is a float, return true, else return false
    """
    try:
        float(string)
        return True
    except ValueError:
        return False

def _is_bool(string):
    """If string s is a boolean, return true, else return false
    """
    string_lower = string.lower()
    if string_lower in _VALID_BOOLEAN_VALUES:
        return True
    else:
        return False

def _is_list(string):
    """If string s is a list, return true, else return false
    """
    if string[0] in ['[']:
        return True
    else:
        return False

def _str2bool(string):
    return string.lower() in _VALID_TRUE_VALUES

def _str2list(string):
    string = string.replace('[', '')
    string = string.replace(']', '')
    string = string.replace(' ', '')
    s_list = []
    for item in string.split(','):
        s_list.append(item)
    return s_list

def _auto_convert(string):
    print 'test'


_CHECK_TYPE_METHOD = {
    'int': _is_int,
    'float': _is_float,
    'bool': _is_bool
}
_CONVERT_METHOD = {
    'int': int,
    'float': float,
    'bool': _str2bool,
    'auto': _auto_convert
}

class MissingKeyError(Exception):
    """Raise MissingKeyError if the paramters file doesn't have the requested key
    """
    pass

class ParameterValueError(Exception):
    """Raise ParameterValueError if the value is not of the expected type.
    """
    pass

class ParamParser(object):
    """Parameter Parser
    """
    def __init__(self, params_file=None):
        if params_file is None:
            sys.exit("Must provide a params_file.")

        with open(params_file, 'r') as f:
            file_line_list = f.readlines()
        file_line_list = [file_line.strip() for file_line in file_line_list]

        i = 0
        self._params_values = {}
        while i < len(file_line_list):
            key = file_line_list[i].replace(':', '')
            value = file_line_list[i+1]
            if value[-1] == ':':
                sys.exit("{} does not have a value.".format(key))
            self._params_values[key] = value
            i += 2

        self.avail_keys = self._params_values.keys()

    def read(self, key, param_type='auto'):
        """Read parameter value
        """
        if key not in self._params_values:
            raise MissingKeyError("{}".format(key))
        if param_type not in _VALID_TYPES:
            sys.exit("{} is not a valid type.".format(param_type))
        value = self._params_values[key]

        if param_type == 'str':
            return self._params_values[key]

        if param_type != 'auto':
            checker = _CHECK_TYPE_METHOD[param_type]
            if not _is_list(value) and not checker(value):
                raise ParameterValueError("{}: {} is not of type {}".format(key, value, param_type))
            elif _is_list(value):
                value_list = _str2list(value)
                for item in value_list:
                    if not checker(item):
                        raise ParameterValueError("{}: {} in {} is not of type {}".format(key, item, value, param_type))

        converter = _CONVERT_METHOD[param_type]
        if _is_list(value):
            results = []
            value_list = _str2list(value)
            for item in value_list:
                results.append(converter(item))
            return results
        else:
            return converter(value)


