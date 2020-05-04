'''
Created on Sep 26, 2018

@author: gaura
'''
import copy

class Foo(object):
    def __init__(self, val):
         self.val = val

    def __repr__(self):
        return str(self.val)

foo = Foo(1)

a = ['foo', foo]
b = a.copy()
c = a[:]
d = list(a)
e = copy.copy(a)
f = copy.deepcopy(a)

# edit orignal list and instance 
a.append('baz')
foo.val = 5

print('original: %r\n list.copy(): %r\n slice: %r\n list(): %r\n copy: %r\n deepcopy: %r'
      % (a, b, c, d, e, f))