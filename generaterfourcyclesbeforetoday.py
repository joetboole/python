#!/usr/bin/python
from datetime import *
import datetime
dateToday = datetime.datetime(2015,9,24)
cyleLength = 28
lastCycleStart = dateToday + timedelta(days = 1);
lastCycleEnd = lastCycleStart + timedelta(days=cyleLength-1)
print("cyle dateToday:")
print("	",lastCycleEnd.strftime("%Y-%m-%d"))