#!/usr/bin/python

# parent class
class Employer:
    employerName = ''

    def __init__(self):
        print("calling parent constructor")

    def __init__(self, employerName):
        self.employerName = employerName


# child class
class Employee(Employer):
    empCount = 0

    def __init__(self):
        print("calling child constructor")

    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # the first argument to each method is self
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    # method over loading is not possible in python
    # def displayCount(self, count):
    #    print("Total Employee %d" % count)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
