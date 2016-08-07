"""
This file contains utilities.
"""

import os

def extract_name_extension(filename):
    '''Splits filename into name and extension.

    Returns name as the first argument and extension as the second.'''
    dot_loc = filename.rfind('.')

    find_not_found_value = -1
    dot_idx = dot_loc if dot_loc != find_not_found_value else len(filename) - 1

    return filename[:dot_idx], filename[dot_idx+1:]

def remove_extension(filename):
    return extract_name_extension(filename)[0]

def get_extension(filename):
    return extract_name_extension(filename)[1]

def fill_dict_with(_to,_from):
    for k,v in _from.items():
        _to[k] = v

def reverse_dict(forward_dict):
    '''makes keys values and values keys'''
    return {v:k for k,v in forward_dict.items()}

def concatenate_dicts(d1,d2):
    con = d1.copy()
    con.update(d2)
    return con
