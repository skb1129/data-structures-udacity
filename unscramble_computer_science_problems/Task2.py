"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    callDurations = {}
    for log in calls:
        if log[0] not in callDurations:
            callDurations[log[0]] = int(log[3])
        else:
            callDurations[log[0]] = int(callDurations.get(log[0])) + int(log[3])
        if log[1] not in callDurations:
            callDurations[log[1]] = int(log[3])
        else:
            callDurations[log[1]] = int(callDurations.get(log[1])) + int(log[3])
    # print(callDurations.items())
    maxDuration = ('0', 0)
    for item in callDurations.items():
        if maxDuration[1] < item[1]:
            maxDuration = item
    print('%s spent the longest time, %d seconds, on the phone during September 2016.' % maxDuration)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
