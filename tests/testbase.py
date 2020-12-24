"""
Common functionality to all tests runners
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import map
from builtins import *
import sys, unittest

# path fixup to insert the most current path when developing
sys.path.insert(0, '..' )

import boolean2

#
# helper functions
#
def join( data, sep='\n', patt='%s'):
    return patt % sep.join( map(str, data) )

get     = lambda elem, attr: getattr(elem, attr)        
istrue  = lambda x: x 
isfalse = lambda x: not x 

def get_states( mode, text, steps, missing=None):
    """
    Helper function that generates the states based on 
    """
    model  = boolean2.Model( mode=mode, text=text )
    model.initialize( missing=missing )
    model.iterate( steps=steps )
    return model.states

class TestBase( unittest.TestCase ):

    def setUp(self):
        self.EQ = self.assertEqual

def test():
    pass

if __name__ == '__main__':
    test()