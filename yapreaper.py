##### Import modules (or libraries) for shell functionality
import os, sys, shutil, errno
from sys import argv

##### Invocation: yapreaper.py source_directory destination_directory
## On the left side is a tuple
script, sourcedir, destdir = argv

##### Defining functions for the reaper
## Checking for existence of directories, else create them
def makedirectory(path):
    try:
        # makedirs makes all intermediate directories
        os.makedirs(path)
        print "Created", path
    except OSError:
        if not os.path.isdir(path):
            raise

##### Variables for the reaper
# TODO not sure if I need 'segments', 'matrix' files. Add them if necessary for the paper.
stringsofinterest = ['taxsummary', 'taxonomy', 'groupstats', 'phylotax', 'annotated.fasta',
                     'good.group', 'good.name', 'alsummary']

##### Reaping steps
# Start the directory walk from the very bottom of the directory tree.
# os.walk is returning a tuple and the for loop iterates over the element of the tuple
for root, dirs, files in os.walk(sourcedir, topdown=False):
    for filename in files:
        # Only the filesnames that end with the strings specified in stringsofinterest
        for stringint in stringsofinterest:
            # .abspath uses absolute path
            if (filename.endswith(stringint)):
                # check if directory exists and if not, create directories in destdir
                sourcefile = os.path.join(os.path.abspath(root),filename)
                # get the path of the sourcefile
                sourcepathstring = os.path.abspath(root).split("/")
                subdirname = sourcepathstring[len(sourcepathstring)-1]
                # make an identical file structure in the destination_directory
                makedirectory(os.path.join(destdir,stringint,subdirname))
                # make the newfile name
                newfile = os.path.join(destdir, stringint, subdirname, filename)
                # if the file does not exist, copy it
                try:
                    # this is a check
                    assert(not os.path.exists(newfile))
                    shutil.copy2(sourcefile, newfile)
                    print "Copied", sourcefile, "as", newfile
                except:
                    print(newfile, "already exists!")
