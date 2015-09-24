#!usr/python/bin
#date to millionseconds
import time
import datetime
import calendar
from datetime import timedelta
# should input date plus 1
d = datetime.datetime(2015,9,25)
s = time.mktime(d.timetuple()) * 1000
print(s)
