#!/usr/bin/python

from basic_class import Employee

employee = Employee("himansu", 65000)

if isinstance(employee, Employee):
    print("employee is the instance of Employee class")

employee.displayEmployee()
print(Employee.empCount)

getattr(employee, 'empCount')

# call static method
Employee.static
