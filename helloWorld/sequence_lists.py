#!/usr/bin/python

jvm_langs = ['Java', 'Jython', 'Groovy', 'Scala', 'JRuby']

# It's not a good idea to directly us __xxx__ methods
# A better way is. Remember there is usually a top level function which
# is the idiomatic way to access the __xxx__method
# len() call _len_() internally
# http://stackoverflow.com/questions/2481421/difference-between-len-and-len
print('I know of ', jvm_langs.__len__(), 'langs that can run on the JVM')
print('I know of ', len(jvm_langs), 'langs that can run on the JVM')

# Adding item to list
print('Oops I forgot Clojure')
jvm_langs.append('Clojure')
jvm_langs.extend(['Extension : Python can be uses both as scripting and as a oop'])

# iterate list using for in
for lang in jvm_langs:
    print(lang)

# iterate list using while
count = 0
while count < len(jvm_langs):
    print(jvm_langs[count])
    count += 1

# Reading elements from list
print("The 3rd JVM language is ", jvm_langs[2])
print("The first 3 JVM languages are ", jvm_langs[:3])
print("The 2nd to 4th JVM languages are ", jvm_langs[1:4])

print("let's sort these languages")
jvm_langs.sort()
print(jvm_langs)

# remove element from the list
print('Remove element from list')
jvm_langs.pop()
print(jvm_langs)

jvm_langs.pop(1)
print(jvm_langs)

jvm_langs.remove('Clojure')
print(jvm_langs)

# insert element from the list
jvm_langs.insert(0, 'Insert element in the start')
print(jvm_langs)

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)
print(movies)

# isinstance
name = ['Himansu Nayak']
address = [name, 'Republic of Ireland']
if isinstance(address[0], list):
    print(name, ' is a list inside a List')
