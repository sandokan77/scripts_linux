# How to use:
# python3 ~/Projects/scripts_linux/cpmd.py /lib/x86_64-linux-gnu/libgpg-error.so.0 ./unix/

import os
import sys

SOURCE_PATHWITHFILE = None 
DEST_DIR = None

def init():
    global SOURCE_PATHWITHFILE, DEST_DIR
    
    SOURCE_PATHWITHFILE = sys.argv[1]
    DEST_DIR = sys.argv[2]

def makedir():
    print ("SOURCE_PATHWITHFILE:",SOURCE_PATHWITHFILE)
    print("DEST_DIR:",DEST_DIR)
    os.makedirs(os.path.dirname(DEST_DIR + SOURCE_PATHWITHFILE), exist_ok=True)

def copyfile():
    global SOURCE_PATHWITHFILE, DEST_DIR
    os.system('cp ' + SOURCE_PATHWITHFILE + ' ' + DEST_DIR + SOURCE_PATHWITHFILE)

if (len(sys.argv) != 3):
    #print (sys.argv[1])
    print ("I need a SOURCE_PATHWITHFILE and a DEST_DIR. DEST_DIR must not end with slash or backslash!")
else:
    init()
    makedir()
    copyfile()