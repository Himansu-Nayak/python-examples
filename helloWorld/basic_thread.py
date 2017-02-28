#!/usr/bin/python

import _thread
import time


def print_numbers(threadName, delay):
    count = 0
    while count <= 100:
        print(count, threadName)
        time.sleep(delay)
        count += 1


try:
    _thread.start_new_thread(print_numbers("python thread", 2))

except Exception as e:
    print("exception during thread execution", e)
