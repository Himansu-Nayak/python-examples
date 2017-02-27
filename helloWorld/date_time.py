#!/usr/bin/python
import time
import calendar
import datetime

print(calendar, time)

time_py = time.time()
print(time_py)
print(time.localtime(time_py))

cal = calendar.month(2008, 1)
print(cal)

# http://stackoverflow.com/questions/32517248/what-is-the-difference-between-python-functions-datetime-now-and-datetime-t
print(datetime.datetime.now())
print(datetime.datetime.today())

