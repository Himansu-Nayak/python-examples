#!usr/bin/python


def add(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def mul(a, b):
    print(a * b)


def div(a, b):
    print(a / b)


dict = {"+": add, "-": sub, "*": mul, "/": div}

method = "/"

if method in dict:
    dict["+"](2, 1)
    dict["-"](2, 1)
    dict["*"](2, 1)
    dict["/"](2, 1)
else:
    raise Exception("method not implemented")
