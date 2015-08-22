# Import required modules
import re
import os
from sys import argv
script, inputcsv = argv

# Functions for this script
# Checking for existence of directories, else create them
def makedirectory(path):
    try:
        # makedirs makes all intermediate directories
        os.makedirs(path)
        print "Created", path
    except OSError:
        if not os.path.isdir(path):
            raise

# Access functions scoped by their module name if the from module import library
csvhandle = open(inputcsv, "r")

# Tuple of relevant DataTypes to capture
datatypeint = ("Median", "Avg Net MFI", "Net MFI", "Count", "\%Recovery", "\%CV Replicates", "Dilution Factor")
# join the tuple with pipe, |
typeregex = "|".join(datatypeint)
# print out

# Go through the file and match two patterns
ifoundit = 0
opennewcsv = 0
for line in csvhandle:
    if re.search("^DataType:", line):
        if not re.search("Bead", line):
            # the output of re.findall is a list
            out = re.findall(typeregex, line)
            if len(out)>0:
                ifoundit = 1
                dirname = inputcsv.split("_")[0]
                # make new filename
                outputcsv = dirname+"/"+inputcsv.split("_")[0]+"_"+out[0]+".csv"
                outputcsv = re.sub("\s+","_", outputcsv)
                outputcsv = re.sub("%", "", outputcsv)
                makedirectory(dirname)
                # open the new csv for writing
                opennewcsv = open(outputcsv, "w")
    # if the DataType string is not found, check ifoundit value.
    elif ifoundit == 1:
        if not re.search("^\,", line):
            # start writing out the lines to the new csv
            opennewcsv.write(line)
        elif re.search("^\,", line):
            # stop writing and close file
            ifoundit = 0
            opennewcsv.close()
