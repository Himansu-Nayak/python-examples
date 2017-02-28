#!/usr/bin/python


def printing(name, age=30):
    print("Name: ", name)
    print("Age ", age)
    return


# Now you can call printing function
printing(name="himansu")
printing(name="himansu", age=10)
printing(age=10, name="himansu")
