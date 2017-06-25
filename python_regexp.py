# Import regexp library
import re

# re.match(pattern, string, flags=0)
# returns a re.MatchObject on success, None on failure.
# re.search(pattern, string, flags=0)
# returns a re.MatchObject on success, none on failure.
# re.sub(pattern, repl, string, max=0)

# Always use raw strings in regular expressions
# Raw strings begin with prefix r: tells python not to interpret backslashes and metacharacters
# So r"\n\w" instead of "\\n\\w" in R.

regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string

    # If we want, we can use the MatchObject's start() and end() methods
    # to retrieve where the pattern matches in the input string, and the
    # group() method to get all the matches and captured groups.
    match = re.search(regex, "June 24")

    # This will print [0, 7), since it matches at the beginning and end of the
    # string
    print("Match at index %s, %s" % (match.start(), match.end()))

    # The groups contain the matched values.  In particular:
    #    match.group(0) always returns the fully matched string
    #    match.group(1) match.group(2), ... will return the capture
    #            groups in order from left to right in the input string
    #    match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: %s" % (match.group(0)))
    # So this will print "June"
    print("Month: %s" % (match.group(1)))
    # So this will print "24"
    print("Day: %s" % (match.group(2)))
else:
    # If re.search() does not match, then None is returned
    print("The regex pattern does not match.")


# matchList = re.findall(pattern, input_str, flags=0)
# matchList = re.finditer(pattern, input_str, flags=0)

matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    # " ".join(list) will join the elements of a list with a space
    print("Full match: %s" % (" ".join(match)))

# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print("Match month: %s" % (match))

# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print("Match at index: %s, %s" % (match.start(), match.end()))

# replacedString = re.sub(pattern, replacement_pattern, input_str, count, flags=0)
regex = r"([a-zA-Z]+) (\d+)"

# This will reorder the string and print:
#   24 of June, 9 of August, 12 of Dec
print(re.sub(regex, r"\2 of \1", "June 24, August 9, Dec 12"))

# flags
# re.IGNORECASE makes the pattern case insensitive so that it matches strings of
# different capitalizations
# re.MULTILINE is necessary if your input string has newline characters (\n) and
# allows the start and end metacharacter (^ and $ respectively) to match at the
# beginning and end of each line instead of at the beginning and end of the
# whole input string
# re.DOTALL allows the dot (.) metacharacter match all characters, including
# the newline character (\n)

# Compile a regular expression for speed
# regexObject = re.compile(pattern, flags=0)
# Lets create a pattern and extract some information with it
# \w+ is any character
regex = re.compile(r"(\w+) World")
result = regex.search("Hello World is the easiest")
if result:
    # This will print:
    #   0 11
    # for the start and end of the match
    print(result.start(), result.end())

# This will print:
#   Hello
#   Bonjour
# for each of the captured groups that matched
for result in regex.findall("Hello World, Bonjour World"):
    print(result)

# This will substitute "World" with "Earth" and print:
#   Hello Earth
print(regex.sub(r"\1 Earth", "Hello World"))
