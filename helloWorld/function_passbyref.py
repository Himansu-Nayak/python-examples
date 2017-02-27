#!/usr/bin/python

# Function definition is here
def changeme(myList2):
    myList2.append([1, 2, 3, 4])
    print("Values inside the function: ", myList2)
    return


def reassign(myList3):
    # creating a new list any changes to the myList3 won't affect teh myList1
    myList3 = [0, 1]


def append(myList4):
    myList4.append(1)


myList1 = [10, 20, 30]
changeme(myList1)
reassign(myList1)
append(myList1)
print("Values outside the function: ", myList1)
