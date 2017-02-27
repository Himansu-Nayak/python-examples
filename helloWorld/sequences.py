#!/usr/bin/python

# Note: lists, tuples, strings, unicode, buffer and xrange are all sequences in Python. Sequences allow
# indexing and slicing operations
# When a sequence is sliced the resulting object is a brand new object
# https://docs.python.org/2.4/lib/typesseq.html

jvm_langs = ['Java', 'Jython', 'Groovy', 'JRuby', 'Scala', 'Clojure']
print('The first JVM language was ', jvm_langs[0])

# Let's slice the list. Slicing can be done with positive and negative indexes
print('The second and third JVM languages are ', jvm_langs[1:3])
print('The last 2 JVM languages are ', jvm_langs[-2:])
print('The first 2 JVM languages are ', jvm_langs[:2])

name = 'Himansu Nayak'
print('The first name is ', name[0:5])
