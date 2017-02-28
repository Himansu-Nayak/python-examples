#!/usr/bin/python

from basic_class import Employee

employee = Employee("himansu", 65000)
employee.displayEmployee()
print(Employee.empCount)

getattr(employee, 'empCount')
