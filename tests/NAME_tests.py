from nose.tools import *
from NAME.find import listSum
#from NAME import find

def setup():
    print('setup!')

def teardown():
    print('Tear down')

def test_basic():
    print('RUN')

def test_advance():
    print('RUN')

def test_listSum():
    #res = find.listSum([1,2,3,4,5])
    res = listSum([1,2,3,4,5])
    assert_equal(15, res)
