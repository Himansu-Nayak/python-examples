#!/usr/bin/python

# Note: Python tuples are (immutable list) just like strings
# Tuples are fixed size in nature whereas lists are dynamic.
# You can't add elements to a tuple. Tuples have no append or extend method.
# You can't remove elements from a tuple. Tuples have no remove or pop method.

jvm_langs = ('Java', 'Jython', 'JRuby')
print(jvm_langs)

print('Oops I forgot Scala and Groovy but I cannot add to an existing tuple')

jvm_langs_revised = ('Scala', 'Groovy', 'Clojure', jvm_langs)
# Notice that the earlier sequence is retained and not flattened

print(jvm_langs_revised)
for langs in jvm_langs_revised:
    print(langs)
