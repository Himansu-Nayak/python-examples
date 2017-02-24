#!/usr/bin/python

import string

greeting = 'Hello'
name = 'John'

print("%s %s how are you?" % (greeting, name))

print("%(greeting)s %(name)s how are you?" % locals())

print(string.Template('$greeting $name how are you?').substitute(locals()))

print("{greeting} {name} how are you?".format(**locals()))
