from paramparser import ParamParser

parser = ParamParser('test.txt')

a = parser.read('a', 'str')
print a
b = parser.read('b', 'int')
print b
c = parser.read('c', 'float')
print c
d = parser.read('d', 'bool')
print d
e = parser.read('e', 'bool')
print e
f = parser.read('f', 'int')
print f
g = parser.read('g', 'bool')
print g