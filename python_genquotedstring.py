# Objective: Take any string of words separated by variable spaces as input
# output a quoted string suitable for R.

# Usage cat file_with_words_of_interest | python python_genquotedstring.py
import re
import fileinput

source = ""
for line in fileinput.input():
    source += line.replace('\n', ' ')
# print(example_input)

# Convert a string of words into a vector of strings suitable for input into R
# .strip() removes all whitespace at the start and end, including spaces, tabs, newlines and carriage returns
# Read left to right whenever a method is used
states = r'('+','.join(['"' + x.strip() + '"' for x in source.replace(' ', ',').split(',') if len(x) > 0])+r')'

# rvector = parsed.replace("'", '"')
print(states)
