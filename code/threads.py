#!/usr/bin/python3

import _thread
import time

# Define a recording thread
def recording():
    import recordtest

# Define a processing thread
def soundProcessing(file):
    import audioAnalysis

# Define a transmission thread
#def transmission():
    

# Create 3 threads as follows
try:
   _thread.start_new_thread( recording )
   _thread.start_new_thread( soundProcessing, 'test1.py' )
except:
   print ("Error: unable to start thread")

while 1:
   pass


'''
# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time())))
      
'''
