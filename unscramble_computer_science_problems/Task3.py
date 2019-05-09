"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    results = []
    b2bCalls = 0
    callsFromB = 0
    for log in calls:
        number1 = log[0].split(')')[0][1:]
        if number1 != '080':
            continue
        else:
            callsFromB += 1
        number2 = log[1]
        if number2.startswith('140'):
            continue
        code = number2.split(')')[0][1:] if number2.startswith('(') else number2[:4]
        if code == '080':
            b2bCalls += 1
        if code not in results:
            results.append(code)
    print('The numbers called by people in Bangalore have codes:')
    results.sort()
    for result in results:
        print(result)
    print()
    print('%0.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.' % (
                b2bCalls * 100 / callsFromB))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
- Fixed lines start with an area code enclosed in brackets. The area
codes vary in length but always begin with 0.
- Mobile numbers have no parentheses, but have a space in the middle
of the number to help readability. The prefix of a mobile number
is its first four digits, and they always start with 7, 8 or 9.
- Telemarketers' numbers have no parentheses or space, but they start
with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
<list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
