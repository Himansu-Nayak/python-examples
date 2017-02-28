#!/usr/bin/python

class Arithmetic:
    # constructor
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        print(self.number + other.number)

    def __sub__(self, other):
        print(self.number - other.number)

    def __mul__(self, other):
        print(self.number * other.number)

    def __truediv__(self, other):
        print(self.number / other.number)


arithmetic = Arithmetic(6)
arithmetic2 = Arithmetic(3)

arithmetic + arithmetic2
arithmetic - arithmetic2
arithmetic * arithmetic2
arithmetic / arithmetic2
