"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

results = []
texts = []
calls = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts += list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls += list(reader)


def get_unique_numbers(data):
    for number in data:
        if number[0] not in results:
            results.append(number[0])
        if number[1] not in results:
            results.append(number[1])
    return results


get_unique_numbers(calls)

for log in texts:
    try:
        results.remove(log[0])
        results.remove(log[1])
    except:
        pass

for log in calls:
    try:
        results.remove(log[1])
    except:
        pass
results.sort()
print('These numbers could be telemarketers:')
for result in results:
    print(result)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
