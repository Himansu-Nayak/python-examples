#!/usr/bin/python
import calendar
import datetime
import time

import dateutil

# install python dateutil pkg - python -m pip install python-dateutil

print(calendar, time)

time_py = time.time()
print(time_py)
print(time.localtime(time_py))

cal = calendar.month(2008, 1)
print(cal)

# http://stackoverflow.com/questions/32517248/what-is-the-difference-between-python-functions-datetime-now-and-datetime-t
print(datetime.datetime.now())
print(datetime.datetime.today())
print(dateutil.__version__.format(datetime.today))
