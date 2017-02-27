#!/usr/bin/python

# A Python dictionary is a collection which contains key value pairs, where the
# key must be an immutable object

# you can also run this in the interpreter

phonebook = {'joe': '568-564-1109', 'ashish': '657-097-7862'}

print("\nPrinting the phonebook ", phonebook)

# insert item to dictionary
phonebook['himansu'] = '657'

# insert itme using update to dictionary
phonebook.update({'nayak': '3'})
phonebook.update({'nayak': '4'})

print("\nPrinting the phonebook after insertion", phonebook)

print("\nPrinting the phone number of the newly added contact joel", phonebook['himansu'])

print("\nHere's how we remove an element from the dictionary - removing 'himansu'")
del (phonebook['himansu'])

print("\nIterating across the phonebook with it's keys")
for k in phonebook.keys():
    print(k, phonebook[k])

print("\nIterating across the phonebook with key and value")
for k, v in phonebook.items():
    print(k, v)
