#!/usr/bin/python

# from sys module import a member called 'argv'
import sys

filename = sys.argv[0]
fp = open(filename)
print("Reading file %r " % fp)
print(fp.read())
fp.close()
