from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
import sys, unittest, string
from random import randint, choice
from itertools import *

# import path fixup
sys.path.append( '..' )

class CodegenTest( unittest.TestCase ):
    
    def test_import( self ):
        "Testing import"
  
        
def get_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase( CodegenTest )
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner( verbosity=2 ).run( get_suite() )  
    
