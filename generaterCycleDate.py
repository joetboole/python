#!/usr/bin/python
from datetime import timedelta
import time
import datetime

withDateMode = False
dateformatPattern = "%Y-%m-%d"
dateToday = datetime.datetime(2015,9,24)
cyleLength = 28
periodLength = 4
membershipId = ""

if(withDateMode):
    millionsPattern = " (%s)(%.0f)"
else:
    millionsPattern = " %s%.0f"
def generateDatetimeBefore(start,endDelta,cycleLength):
    endDatetime = start - timedelta(days = endDelta)
    startDatetime =  endDatetime - timedelta(days = cycleLength - 1)
    startMsg = millionsPattern%(realDateTimeStr(startDatetime),dateToMillions(startDatetime))
    endMsg = millionsPattern%(realDateTimeStr(endDatetime),dateToMillions(endDatetime))
    print("| %s | %s | %s | %d | %d |"%(startMsg, endMsg, membershipId, cyleLength, periodLength))
    return startDatetime

def generateCurrentPredictCycle(periodStartDate):
    endDatetime = periodStartDate + timedelta(days = cyleLength - 1)
    startMsg = millionsPattern%(realDateTimeStr(periodStartDate),dateToMillions(periodStartDate))
    endMsg = millionsPattern%(realDateTimeStr(endDatetime),dateToMillions(endDatetime))
    print("| %s | %s | %s | %d | %d |"%(startMsg, endMsg, membershipId, cyleLength, periodLength))

def realDateTimeStr(visualDateTime):
    result = ""
    if(withDateMode):
        result = (visualDateTime - timedelta(days = 1)).strftime(dateformatPattern)
    return result

def dateToMillions(dateTime):
    return time.mktime(dateTime.timetuple())*1000

def millionsToDate(millions):
    utc_time = datetime.datetime(1970, 1, 1) + timedelta(milliseconds=millions)
    print(utc_time.strftime("%Y-%m-%d"))

lastCycleStart = dateToday + timedelta(days = 1);
lastCycleEnd = lastCycleStart + timedelta(days=cyleLength-1)
print("cyle dateToday:")
print("	",dateToday.strftime("%Y-%m-%d"))
print("============================")
print("| startDate | endDate | memberid | cycle_length | period_length|")
print("|-----------|---------|----------|--------------|-------------|")
generateCurrentPredictCycle(lastCycleStart)

start = generateDatetimeBefore(lastCycleStart,1,cyleLength)
start = generateDatetimeBefore(start,1,cyleLength)
start = generateDatetimeBefore(start,1,cyleLength)
start = generateDatetimeBefore(start,1,cyleLength)



