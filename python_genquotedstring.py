# Objective: Take any string of words separated by variable spaces as input
# output a quoted string suitable for R.

# Usage cat file_with_words_of_interest | python python_genquotedstring.py
import re
import fileinput

example_input = ""
for line in fileinput.input():
    example_input += line.rstrip()
# print(example_input)

nocomma = re.sub(r",+", "", example_input)
noleadingtrailing = re.sub(r"^\s*(.*)\s*$", r"\1", nocomma)
wordsonly =  re.sub(r"\s+([A-Za-z0-9]+)\s+", r'", "\1", "', noleadingtrailing)
notrailing = re.sub(r"(.*?)\s*$", r"\1", wordsonly)
rvector = 'c("' + notrailing + '")'

print(rvector)

# gsub(",", "", example_input)
# gsub("^\s*(.*)\s*$", "\1", example_input)
# gsub("\s+", ",", example_input)
