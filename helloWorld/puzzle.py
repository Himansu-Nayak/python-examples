#!/usr/bin/python


def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)
    # l.clear() if not clear than the list will be reused for the next call


f(2)
f(3)
f(3, [3, 2, 1])
f(4)
