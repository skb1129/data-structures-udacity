"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

results = []

def getUniqueNumbers(data):
    for number in data:
        if number[0] not in results:
            results.append(number[0])
        if number[1] not in results:
            results.append(number[1])
    return results

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    getUniqueNumbers(texts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    getUniqueNumbers(calls)
    print('There are %d different telephone numbers in the records.' % len(results))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
