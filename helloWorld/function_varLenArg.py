#!/usr/bin/python


def printing(name, *fruits):
    print("Name: ", name)
    for fruit in fruits:
        print(fruit)
    return


# Now you can call printing function
printing("himansu", "apple", "banana", "orange")
