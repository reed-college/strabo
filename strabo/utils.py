'''
This file contains utilities. ***clarification needed*** used where
'''

import os

def safe_pos_int_conv(inputstr):
    ''' Helps forms submission be robust by returning 1 when empty string is passed
    in instead of a number ***clarification needed*** '''
    return  int(inputstr) if not inputstr == '' else 1

def get_extension(filename):
    ext = os.path.splitext(filename)[1]
    if ext:
        #removes dot from extension
        ext = ext[1:]
    return ext

def fill_dict_with(_to,_from): 
    # ***clarification needed*** so, this looks like it is only used in add_database.py.....
    for k,v in _from.items():
        _to[k] = v

def reverse_dict(forward_dict):
    ''' Makes keys values and values keys.'''
    return {v:k for k,v in forward_dict.items()}

def concatenate_dicts(d1,d2):
    con = d1.copy()
    con.update(d2)
    return con
