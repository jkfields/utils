# -*- coding: utf-8 -*-

'''
Saw this simplified version in a post on stackoverflow and tried it; it worked 
in my case; there is a the longer version by @gpollatos, 
https://www.github.com/gpollatos/objectview
'''
class ObjectView(dict):
    '''
    Enables a simple dictionary to be addressed as key-value pairs.
    '''
     __delattr__ = dict.__delitem__
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
