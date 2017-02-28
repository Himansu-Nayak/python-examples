#!/usr/bin/python
# python -h

# if-elif-else block
if 2 + 3 == 5:
    print("himansu")
    print("nayak")
elif True:
    print("hello")
else:
    print("else block")
print("This is outside the if-elif-else block")

# multiline string
multiLineString = "Expression 1" + \
                  "Expression 2" + \
                  "Expression 3"
print(multiLineString)

multiLineString2 = """Multi-Expression String using
                      tripple quotes"""
print(multiLineString2)

multiLineString3 = {"Expression 1 inside {} array",
                    "Expression 2 inside {} array"}
multiLineString4 = ["Expression 1 inside [] array",
                    "Expression 2 inside [] array"]
multiLineString5 = ("Expression 1 inside () array",
                    "Expression 2 inside () array")
print(multiLineString3, multiLineString4, multiLineString5)

# user input
input("Enter any key to exit")

# multi statement
print("multi statement 1");
print("multi statement 2")

# variable
a = b = c = 1
print(a, b, c)

var = 3
del var
# print(var) will throw error as var is removed from the memory
