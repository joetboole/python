#!usr/python/bin
#date to millionseconds
import time
import datetime
import calendar
import timedelta
# should input date plus 1
d = datetime.datetime(2015,9,25)
s = time.mktime(d.timetuple())
print(s)
